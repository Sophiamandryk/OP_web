''' First time classes practice, OOP '''

class Markets:
    '''
    This class contains information about the shop
    Attributes:
        shop_name(str): the name of the shop
        shop_area(int): the area of the shop
        categories(list[str]): what the shop sells
    Methods:
    __str__():
        Returns a string representation of the supermarket in a readable format.
    '''
    def __init__(self, shop_name, shop_area, categories):
        '''
        Is responsible for market 
        Args:
            shop_name(str): the name of the shop
            shop_area(int): the area of the shop
            categories(list[str]): what the shop sells
        >>> market_family_food = Markets('Family Food', 80, \
        ['Bread and Bakery', 'Dairy', 'Beverages'])
        >>> market_family_food.name
        'Family Food'
        >>> market_family_food.area
        80
        >>> market_family_food.categories
        ['Bread and Bakery', 'Dairy', 'Beverages']
        '''
        self.name = shop_name
        self.area = shop_area
        self.categories = categories
    def __str__(self):
        '''
        Is responsible for building a string 
        
        >>> market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy', \
     'Beverages'])
        >>> print(market_family_food)
        Supermarket Family Food has an area of 80 m2 and has the following categories:\
 Bread and Bakery, Dairy, Beverages.
        '''
        str_categories = ', '.join(self.categories)
        return f'Supermarket {self.name} has an area of {self.area} \
m2 and has the following categories: {str_categories}.'
# market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy', 'Beverages'])
# print(market_family_food.name)
# print(market_family_food.area)
# print(market_family_food.categories)
# print(market_family_food)
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

# # 333333333333333333333333333333333333333333333333333333333333333333333333
# class Item():
#     '''For describing the item you buy'''
#     def __init__(self, name:str, price:float):
#         self.name = name
#         self.price = price
#     def __str__(self):
#         pass


# class Vehicle:
#     '''Shows the transport used and wether it's available'''
#     def __init__(self, vehicle_no:int, is_available: bool = True):
#         self.vehicle_no = vehicle_no
#         self.is_available = is_available


# class Location:
#     ''' Describes the location (the city and Ukr post department)'''
#     def __init__(self, city:str, post_office: int):
#         self.city = city
#         self.post_office = post_office


# class Order:
#     '''Has all the information about the user and the item, generates an ID'''
#     def __init__(self, order_id:int, user_name:str, location: Location, items: list[Item]):
#         self.order_id = order_id
#         self.user_name = user_name
#         self.location = location
#         self.item = items
#     def __str__(self):
#         pass
#     def calculate_amount(self):
#         pass
#     def assign_vehicle(self, vehicle:Vehicle):
#         pass


# class LogisticSystem:
#     ''' Saves all the information about the item, transportation and the user'''
#     def __init__(self, vehicles:list[Vehicle]):
#         self.orders = []
#         self.vehicles = []
#     def place_order(self, order:Order):
#         self.orders.append(order)
#     def track_order(self, order_id: int) -> str:
#         pass



# vehicles = [Vehicle(1), Vehicle(2)]
# logSystem = LogisticSystem(vehicles)
# my_items = [Item('book', 110), Item('chupachups', 44)]
# order_location = Location(city='Lviv', post_office=53)
# my_order = Order(order_id=165488695, user_name='Oleg', location=order_location, items=my_items)
# logSystem.place_order(my_order)
# # print(logSystem.track_order(165488695))




# def print_information(person: PersonWithMethods) -> None:
#     print(f"A person with name {person.name} is {person.age} years old.")
#     print(f"Their email: {person.email}")
#     print(f"Their phone number: {person.phone_number}")

# print_information(petro1)
# print()
# petro1.print_information()




class Car:
    def __init__(self, make: str, price: int):
        self.make = make
        self._price = price  # Store the price in a private variable

    @property
    def price_value(self):
        if self._price >= 20000:
            return self._price * 0.9  # Apply 10% discount if price is >= 20,000
        return self._price

    @price_value.setter
    def price_value(self, value):
        if value < 0:
            raise ValueError("Can't set to a negative number")
        self._price = value  # Update the private price without triggering the discount

# # Testing the class
# car = Car("Toyota", 25000)
# print(f"Car price (with discount if applicable): {car.price_value}")  # Should apply the discount
# car.price_value = 18000
# print(f"Updated car price: {car.price_value}")  # No discount applied for 18,000


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        return self.length * self.width
    @area.setter
    def area(self, value):
        if value < 0 :
            return 'Can"t set'
    @property
    def perimetr(self):
        return (self.length * self.width) * 2
    @perimetr.setter
    def perimetr(self, value):
        if value < 0 :
            return 'Can"t set'
        
class Person:
    def __init__(self, name, age):
        self._age = age
        self.name = name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value <= 0:
            return 'No'
        self._age = value
    def birthday(self):
        self.age = self.age + 1
    

# # Task 2: Rectangle instance
# rectangle = Rectangle(5, 3)
# print(f"Rectangle area: {rectangle.area}")
# print(f"Rectangle perimeter: {rectangle.perimetr}")
# rectangle.length = 6
# rectangle.width = 4
# print(f"Updated area: {rectangle.area}")
# print(f"Updated perimeter: {rectangle.perimetr}")

# # Task 3: Person instance
# person = Person("Alice", 25)
# print(f"Person's age: {person.age}")
# person.birthday()
# print(f"Person's age after birthday: {person.age}")
# person.age = 30
# print(f"Updated age: {person.age}")


def sum_series(N):
    total = 0.0
    for n in range(1, N+1):
        total += 1 / (9 * n**2 + 3 * n - 20)
    return total

# Set a large N for a good approximation
N = 10**6  # One million terms
result = sum_series(N)

# print(f"Approximate sum after {N} terms: {result:.10f}")

import time

class Clock:
    start = time.time()

    def __init__(self, time):
        self.time = time

    def print_time(self):
        return self.time - self.start

clock = Clock(time.time())

# print(clock.print_time() == clock.print_time())
# стек черга дерево граф
import array
import ctypes
ArrayType = ctypes.py_object * 5
slots = ArrayType()
slots[1] = 'shit'
print(slots[1])
# print(slots[1])

compact_array = array.array('u', [])
arr_int = array.array('i', [0]*10)
arr_char = array.array('u', ['A']*10)
arr_float = array.array('f', [0.0]*10)
# print(arr_float)

class Array2D:
    def __init__(self, nrows, ncols):
        """Створює 2D масив розміру nrows x ncols, заповнений None."""
        self._nrows = nrows
        self._ncols = ncols
        self._array = [[None] * ncols for _ in range(nrows)]

    def num_rows(self):
        """Повертає кількість рядків у масиві."""
        return self._nrows

    def num_cols(self):
        """Повертає кількість стовпців у масиві."""
        return self._ncols

    def clear(self, value):
        """Очищає масив, присвоюючи всім елементам значення value."""
        for i in range(self._nrows):
            for j in range(self._ncols):
                self._array[i][j] = value

    def getitem(self, i, j):
        """Повертає значення у позиції (i, j)."""
        if 0 <= i < self._nrows and 0 <= j < self._ncols:
            return self._array[i][j]
        else:
            raise IndexError("Індекс виходить за межі масиву")

    def setitem(self, i, j, value):
        """Змінює значення у позиції (i, j) на value."""
        if 0 <= i < self._nrows and 0 <= j < self._ncols:
            self._array[i][j] = value
        else:
            raise IndexError("Індекс виходить за межі масиву")

    def __repr__(self):
        """Повертає рядкове представлення масиву."""
        return "\n".join(str(row) for row in self._array)
matrix = Array2D(3, 4)
matrix.setitem(1, 2, 42)
# print(matrix.getitem(1, 2))
matrix.clear(0)
# matrix[1, 2] = 42
# print(matrix)





import ctypes
class Array:
    def init(self, size):
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)
    def len(self):
        return self._size
    def getitem(self, index):
        return self._elements[index]
    def setitem(self, index, value):
        self._elements[index] = value
    def clear(self, value):
        for i in  range(len(self)):
            self._elements[i] = value
    def iter(self):
        return ArrayIterator(self._elements)
class ArrayIterator:
    def init(self, the_array):
        self._ref = the_array
        self._cur_index = 0
    def iter(self):
        return self
    def next(self):
        if self._cur_index < len(self._ref):
            entry = self._ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration
        

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = Node(4)

# new_head = Node(2)
# new_head.next = head
# head = new_head

# current = head
# while current.next:
#     current = current.next
# current.next = Node(8)

# node_10 = Node(10)
# node_10.next = current.next
# current.next = node_10

# current = head
# while current:
#     print(current.data, end=",")
#     current = current.next
# print("None")


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    result.append("None")
    return " -> ".join(result)
print(stringify(Node(1, Node(2, Node(3)))))