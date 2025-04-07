import logging
from models import ShippingCost, CourierService, City, Courier
from app import db

logger = logging.getLogger(__name__)

def calculate_shipping_cost(origin_id, destination_id, weight, courier_id=None):
    """
    Calculate shipping cost based on origin, destination, weight, and courier
    
    Args:
        origin_id (int): Origin city ID
        destination_id (int): Destination city ID
        weight (int): Package weight in grams
        courier_id (int, optional): Courier ID. If None, calculate for all couriers.
        
    Returns:
        dict: Shipping cost information
    """
    try:
        origin = City.query.get(origin_id)
        destination = City.query.get(destination_id)
        
        if not origin or not destination:
            logger.error(f"Origin or destination not found: {origin_id} -> {destination_id}")
            return None
            
        # Prepare response structure
        result = {
            'origin_details': origin.to_dict(),
            'destination_details': destination.to_dict(),
            'results': []
        }
        
        # Query shipping costs
        if courier_id:
            courier = Courier.query.get(courier_id)
            if not courier:
                logger.error(f"Courier not found: {courier_id}")
                return None
                
            courier_services = CourierService.query.filter_by(courier_id=courier_id).all()
            if not courier_services:
                logger.error(f"No services found for courier: {courier_id}")
                return None
                
            result['results'] = get_shipping_costs_by_courier(
                origin_id, 
                destination_id, 
                weight, 
                courier,
                courier_services
            )
        else:
            # Calculate for all couriers
            couriers = Courier.query.all()
            for courier in couriers:
                courier_services = CourierService.query.filter_by(courier_id=courier.id).all()
                if courier_services:
                    courier_costs = get_shipping_costs_by_courier(
                        origin_id, 
                        destination_id, 
                        weight, 
                        courier,
                        courier_services
                    )
                    if courier_costs:
                        result['results'].append(courier_costs)
                        
        if not result['results']:
            logger.warning(f"No shipping costs found for params: origin={origin_id}, dest={destination_id}, weight={weight}")
            return None
            
        return result
    except Exception as e:
        logger.error(f"Error calculating shipping cost: {str(e)}")
        return None

def get_shipping_costs_by_courier(origin_id, destination_id, weight, courier, courier_services):
    """
    Get shipping costs for a specific courier
    
    Args:
        origin_id (int): Origin city ID
        destination_id (int): Destination city ID
        weight (int): Package weight in grams
        courier (Courier): Courier object
        courier_services (list): List of CourierService objects
        
    Returns:
        dict: Courier shipping cost information
    """
    try:
        courier_result = {
            'code': courier.code,
            'name': courier.name,
            'costs': []
        }
        
        for service in courier_services:
            # Find applicable shipping cost for the weight range
            shipping_cost = ShippingCost.query.filter(
                ShippingCost.origin_city_id == origin_id,
                ShippingCost.destination_city_id == destination_id,
                ShippingCost.courier_service_id == service.id,
                ShippingCost.weight_start <= weight,
                ShippingCost.weight_end >= weight
            ).first()
            
            if shipping_cost:
                # Calculate cost (some couriers charge per kg)
                total_cost = shipping_cost.cost
                if weight > 1000:  # If more than 1kg
                    # Calculate additional weight in kg (rounded up)
                    additional_kg = (weight - 1000 + 999) // 1000
                    total_cost += additional_kg * shipping_cost.cost
                
                service_cost = {
                    'service': service.code,
                    'description': service.name,
                    'cost': total_cost,
                    'etd': shipping_cost.etd  # estimated time of delivery
                }
                courier_result['costs'].append(service_cost)
        
        # If no costs were found for any service, return None
        if not courier_result['costs']:
            return None
            
        return courier_result
    except Exception as e:
        logger.error(f"Error getting shipping costs for courier {courier.code}: {str(e)}")
        return None
