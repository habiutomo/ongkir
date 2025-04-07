from app import db
from datetime import datetime

class Courier(db.Model):
    """Courier service provider model"""
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(255))
    services = db.relationship('CourierService', backref='courier', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'website': self.website
        }

class CourierService(db.Model):
    """Specific service types offered by couriers"""
    id = db.Column(db.Integer, primary_key=True)
    courier_id = db.Column(db.Integer, db.ForeignKey('courier.id'), nullable=False)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'courier_id': self.courier_id,
            'code': self.code,
            'name': self.name,
            'description': self.description
        }

class Province(db.Model):
    """Indonesian province model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cities = db.relationship('City', backref='province', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class City(db.Model):
    """Indonesian city model"""
    id = db.Column(db.Integer, primary_key=True)
    province_id = db.Column(db.Integer, db.ForeignKey('province.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20))  # 'kabupaten' or 'kota'
    postal_code = db.Column(db.String(10))
    
    def to_dict(self):
        return {
            'id': self.id,
            'province_id': self.province_id,
            'name': self.name,
            'type': self.type,
            'postal_code': self.postal_code
        }

class ShippingCost(db.Model):
    """Shipping cost data"""
    id = db.Column(db.Integer, primary_key=True)
    origin_city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    destination_city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    courier_service_id = db.Column(db.Integer, db.ForeignKey('courier_service.id'), nullable=False)
    weight_start = db.Column(db.Integer, nullable=False, default=1)  # in grams
    weight_end = db.Column(db.Integer, nullable=False, default=1000)  # in grams
    cost = db.Column(db.Integer, nullable=False)  # in IDR
    etd = db.Column(db.String(20))  # estimated time of delivery (e.g., "1-2")
    
    origin_city = db.relationship('City', foreign_keys=[origin_city_id])
    destination_city = db.relationship('City', foreign_keys=[destination_city_id])
    courier_service = db.relationship('CourierService')
    
    def to_dict(self):
        return {
            'id': self.id,
            'origin_city_id': self.origin_city_id,
            'destination_city_id': self.destination_city_id,
            'courier_service_id': self.courier_service_id,
            'weight_start': self.weight_start,
            'weight_end': self.weight_end,
            'cost': self.cost,
            'etd': self.etd
        }

class ApiKey(db.Model):
    """API key for authentication"""
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'key': self.key,
            'email': self.email,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }

class ApiRequest(db.Model):
    """Log of API requests"""
    id = db.Column(db.Integer, primary_key=True)
    api_key_id = db.Column(db.Integer, db.ForeignKey('api_key.id'), nullable=False)
    endpoint = db.Column(db.String(100), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    status_code = db.Column(db.Integer, nullable=False)
    ip_address = db.Column(db.String(50))
    request_time = db.Column(db.DateTime, default=datetime.utcnow)
    
    api_key = db.relationship('ApiKey')
    
    def to_dict(self):
        return {
            'id': self.id,
            'api_key_id': self.api_key_id,
            'endpoint': self.endpoint,
            'method': self.method,
            'status_code': self.status_code,
            'ip_address': self.ip_address,
            'request_time': self.request_time.isoformat()
        }
