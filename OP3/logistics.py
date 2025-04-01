'''This module holds the information about shipping \
and logistics of particular orders'''
import random
class Item:
    '''For describing the item you buy
    Attributes:
    name (type: str) – the name of an item.
    price (type: float) – the price of an item.

    '''
    def __init__(self, name: str, price: float):
        '''Initializer
        >>> pen = Item('pen', 12.12)
        >>> pen.price
        12.12
        >>> pen.name
        'pen'
        >>> pen.__str__()
        'Item: pen, Price: 12.12 UAH'
        '''
        self.name = name
        self.price = price

    def __str__(self):
        '''Returns a string representation
        >>> laptop = Item('laptop', 1500.00)
        >>> str(laptop)
        'Item: laptop, Price: 1500.0 UAH'
        '''
        return f"Item: {self.name}, Price: {self.price} UAH"  # No period at the end


class Vehicle:
    '''Shows the transport used and wether it's available
    Attributes:
    vehicle_no (type: int) – the unique number transportation.
    is_available (type: bool) – to determine whether it's available. 
    '''
    def __init__(self, vehicle_no:int, is_available: bool = True):
        '''The initializer
        >>> truck = Vehicle(123456)
        >>> truck.vehicle_no
        123456
        '''
        self.vehicle_no = vehicle_no
        self.is_available = is_available
    def __str__(self):
        '''Returns the string representation
        >>> truck = Vehicle(123456)
        >>> str(truck)
        'Vehicle number: 123456'
        '''
        return f'Vehicle number: {self.vehicle_no}'



class Location:
    ''' Describes the location (the city and Ukr post department)
    Attributes:
    city (type: str) – the city to ship to.
    post_office (type: int) – the number of post department.
    '''
    def __init__(self, city:str, post_office: int):
        '''The initializer
        >>> place = Location('Frankivsk', 1)
        >>> place.city
        'Frankivsk'
        '''
        self.city = city
        self.post_office = post_office


class Order:
    '''Has all the information about the user and the item, generates an ID
    Attributes:
    order_id (type: int) – the unique number of an item.
    user_name (type: str) – username.
    location (type: Location) - an address where to ship.
    items (type: list[item]) - list of goods in the order
    vehicle (type: Vehicle or None) - transport for shipping
    '''
    def __init__(self, user_name:str, city, post_office, items: list[Item], vehicle=None):
        '''The initializer
        >>> order1 = Order('sofiya', 'Lviv', post_office = 1, items = [Item('book', 12)])
        >>> order1.user_name
        'sofiya'
        '''
        self.order_id = random.randint(1, 1_000_000_000)
        self.user_name = user_name
        self.location = Location(city, post_office)
        self.items = items
        self.vehicle = None
    def calculate_amount(self) -> float:
        '''Calculates the general sum of the order
        >>> random.seed(0)
        >>> items = [Item('pen', 15.5), Item('book', 120.0)]
        >>> order = Order('John', 'Lviv', 1, items)
        >>> print(order)
        Your order number is 906691060.
        >>> order.calculate_amount()
        135.5
        '''
        amount = 0
        for item in self.items:
            amount+= item.price
        return amount
    def __str__(self):
        '''Returns a string representation
        >>> random.seed(0)
        >>> my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
        >>> my_order2 = Order('Andrii', 'Odesa', 3, my_items2)
        >>> print(my_order2)
        Your order number is 906691060.
        '''
        return f'Your order number is {self.order_id}.'
    def assign_vehicle(self, vehicle:Vehicle) -> None:
        '''Assigns vehicle for shipping
        param vehicle: type - vehicle, vehicle 
        >>> truck = Vehicle(123)
        >>> items = [Item('pen', 10)]
        >>> order = Order('John', 'Kyiv', 2, items)
        >>> order.order_id = 1
        >>> order.assign_vehicle(truck)
        >>> order.vehicle.vehicle_no
        123
        >>> order.vehicle.is_available
        False
        '''
        self.vehicle = vehicle
        vehicle.is_available = False


class LogisticSystem:
    ''' Saves all the information about the item, transportation and the user
    Attributes:
    orders (type: list[Order]) – the list of all orders.
    vehicle (type: list[Vehicle]) – the list of transportation.
    '''
    def __init__(self, vehicles:list[Vehicle]):
        '''The initializer
        >>> vehicle1 = Vehicle(1)
        >>> vehicles = [vehicle1]
        >>> logSystem = LogisticSystem(vehicles)
        >>> logSystem.vehicles == [vehicle1]
        True
        '''
        self.orders = []
        self.vehicles = vehicles
    def place_order(self, order: Order) -> None:
        """
        Accepts orders if transport is available.
        # >>> random.seed(45)
        # >>> Order.order_id = 1
        >>> vehicle1 = Vehicle(1)
        >>> vehicles = [vehicle1]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('laptop', 1500), Item('headphones', 200)]
        >>> my_order = Order(user_name='Alice', city='Kyiv', post_office=12, items=my_items)
        >>> my_order in logSystem.orders
        False
        """
        for vehicle in self.vehicles:
            if vehicle.is_available:
                order.assign_vehicle(vehicle)
                self.orders.append(order)
                break
                # return f'Your order number is {order.order_id}.'
        return 'There is no available vehicle to deliver an order.'
    def track_order(self, order_id: int) -> str:
        '''Tracks the order buy its number/id
        param id:type - int, the number of the order
        >>> vehicle1 = Vehicle(1)
        >>> vehicles = [vehicle1]
        >>> logSystem = LogisticSystem(vehicles)
        >>> logSystem.track_order(999999)
        'No such order.'
        '''
        for order in self.orders:
            if order_id == order.order_id:
                return f'Your order #{order_id} is sent to {order.location.city}. Total price: \
{order.calculate_amount()} UAH.'
            # if getattr(order, 'order_id', None) == order_id:
            #     return str(order)
        return 'No such order.'


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
