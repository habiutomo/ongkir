import uuid
import logging
from flask import jsonify, request, render_template, abort
from functools import wraps
from sqlalchemy import and_

from app import app, db, limiter
from models import Courier, CourierService, Province, City, ShippingCost, ApiKey, ApiRequest
from utils import calculate_shipping_cost

logger = logging.getLogger(__name__)

# Authentication decorator
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key') or request.args.get('api_key')
        
        if not api_key:
            return jsonify({'status': 'error', 'message': 'API key is required'}), 401
        
        key_record = ApiKey.query.filter_by(key=api_key, is_active=True).first()
        if not key_record:
            return jsonify({'status': 'error', 'message': 'Invalid API key'}), 401
        
        # Log the API request
        api_request = ApiRequest(
            api_key_id=key_record.id,
            endpoint=request.path,
            method=request.method,
            status_code=200,
            ip_address=request.remote_addr
        )
        db.session.add(api_request)
        db.session.commit()
        
        return f(*args, **kwargs)
    return decorated_function

# Web routes for documentation and homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

# API Routes
@app.route('/api/couriers', methods=['GET'])
@require_api_key
@limiter.limit("10/minute")
def get_couriers():
    try:
        couriers = Courier.query.all()
        return jsonify({
            'status': 'success',
            'results': len(couriers),
            'couriers': [courier.to_dict() for courier in couriers]
        })
    except Exception as e:
        logger.error(f"Error fetching couriers: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/provinces', methods=['GET'])
@require_api_key
@limiter.limit("10/minute")
def get_provinces():
    try:
        provinces = Province.query.all()
        return jsonify({
            'status': 'success',
            'results': len(provinces),
            'provinces': [province.to_dict() for province in provinces]
        })
    except Exception as e:
        logger.error(f"Error fetching provinces: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/cities', methods=['GET'])
@require_api_key
@limiter.limit("10/minute")
def get_cities():
    try:
        province_id = request.args.get('province_id')
        
        if province_id:
            cities = City.query.filter_by(province_id=province_id).all()
        else:
            cities = City.query.all()
            
        return jsonify({
            'status': 'success',
            'results': len(cities),
            'cities': [city.to_dict() for city in cities]
        })
    except Exception as e:
        logger.error(f"Error fetching cities: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/cost', methods=['POST'])
@require_api_key
@limiter.limit("30/minute")
def calculate_cost():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400
            
        # Validate required fields
        required_fields = ['origin', 'destination', 'weight', 'courier']
        for field in required_fields:
            if field not in data:
                return jsonify({'status': 'error', 'message': f'Missing required field: {field}'}), 400
                
        origin_id = data.get('origin')
        destination_id = data.get('destination')
        weight = data.get('weight', 1000)  # in grams, default 1kg
        courier_code = data.get('courier')
        
        # Validate weight
        try:
            weight = int(weight)
            if weight <= 0:
                return jsonify({'status': 'error', 'message': 'Weight must be greater than 0'}), 400
        except ValueError:
            return jsonify({'status': 'error', 'message': 'Weight must be a number'}), 400
        
        # Get courier
        courier = Courier.query.filter_by(code=courier_code).first()
        if not courier:
            return jsonify({'status': 'error', 'message': f'Courier not found: {courier_code}'}), 404
            
        # Calculate shipping cost
        shipping_costs = calculate_shipping_cost(origin_id, destination_id, weight, courier.id)
        
        if not shipping_costs:
            return jsonify({
                'status': 'error',
                'message': 'No shipping costs found for the given parameters'
            }), 404
            
        return jsonify({
            'status': 'success',
            'origin_details': shipping_costs['origin_details'],
            'destination_details': shipping_costs['destination_details'],
            'results': shipping_costs['results']
        })
    except Exception as e:
        logger.error(f"Error calculating shipping cost: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/register', methods=['POST'])
def register_api_key():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400
            
        # Validate required fields
        required_fields = ['email', 'name']
        for field in required_fields:
            if field not in data:
                return jsonify({'status': 'error', 'message': f'Missing required field: {field}'}), 400
                
        email = data.get('email')
        name = data.get('name')
        
        # Check if email already exists
        existing_key = ApiKey.query.filter_by(email=email).first()
        if existing_key:
            return jsonify({'status': 'error', 'message': 'Email already registered'}), 400
            
        # Generate API key
        api_key = str(uuid.uuid4()).replace('-', '')
        
        # Create new API key
        new_key = ApiKey(
            key=api_key,
            email=email,
            name=name
        )
        db.session.add(new_key)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'API key generated successfully',
            'data': {
                'api_key': api_key
            }
        })
    except Exception as e:
        logger.error(f"Error registering API key: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({'status': 'error', 'message': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'status': 'error', 'message': 'Internal server error'}), 500

@app.errorhandler(429)
def ratelimit_error(e):
    return jsonify({'status': 'error', 'message': 'Rate limit exceeded'}), 429
