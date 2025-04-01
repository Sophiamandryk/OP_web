'''The cafeteria module '''
RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }
class Track:
    '''The class that tracks changes
    Attributes:
        date(type:str)
        order
        new_limit
    Methods:
        __str__(), is responsible for returning string representation
        place_order(),
        total_revenue()
        total_milk()
        total_beansf()
        set_limit_milk, class method

    '''
    __beans = 5000
    __milk = 20000
    safety = True
    MENU = {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60
    }
    orders = []
    def __init__(self, date:str):
        self.date = date
        self.orders = []
    def place_order(self, order):
        """Places an order and processes payment."""
        if not isinstance(order, Coffee):
            return "We can't create anything that is not a Coffee instance."
        if not Track.safety:
            return 'Unfortunately, now it is not safe to make coffee.'
        if order.name in self.MENU:
            if self.milk < order.milk:
                return "Unfortunately, we don't have enough ingredients."
            order.price = self.MENU[order.name] * order.count
            order.is_paid = True
            self.orders.append(order)
            return "Done!"
        else:
            return "Unfortunately, we don't have such kind of coffee in the menu."
        
    def total_revenue(self):
        """Calculates total revenue from orders."""
        total_revenue = 0
        for order in self.orders:
            total_revenue += order.price
        return total_revenue
    def total_milk(self):
        """Calculates total milk used."""
        total_milk = 0
        for order in self.orders:
            total_milk += order.milk
        return total_milk
    def total_beans(self):
        """Calculates total coffee beans used (6g per espresso shot)."""
        #6 grams for one espresso
        total_beans = 0
        for order in self.orders:
            total_beans += order.espresso
        return (total_beans / 30)*6
    @property
    def beans(self):
        """Returns remaining beans after orders."""
        return self.__beans - self.total_beans()
    @property
    def milk(self):
        """Returns remaining milk after orders."""
        if self.__milk >=  self.total_milk():
            return self.__milk - self.total_milk()
        return 0
    def milk_spoil(self, grams):
        if self.__milk >= grams:
            self.__milk = self.__milk - grams
        else:
            self.__milk = 0
    @classmethod
    def set_limit_milk(cls, new_limit):
        """Sets a new limit for milk storage."""
        if new_limit > 0:
            cls.__milk = new_limit
    @classmethod
    def change_air_state(cls):
        """Toggles safety state for coffee-making."""
        cls.safety = not cls.safety

class Coffee:
    """Represents a basic coffee order.
    Attributes:
        name(type:str)
        count
        recipe
    Methods:
        __str__(), is responsible for returning string representation
        set_recipe(), class method
    """
    __recipe = {}
    def __init__(self, name, count = 1):
        '''The initializer'''
        self.name = name
        self.count = count
        if self.name in self.__recipe:
            self.is_paid = False
      
    def __str__(self):
        '''Returns the string representation of the class'''
        if self.__recipe == {}:
            return "Order cannot be created. Recipe has not been set."
        if self.name not in self.__recipe:
            return "Order cannot be created. We don't have recipe for it."
        if not self.is_paid:
            return f'Order "{self.count} {self.name}" is created.'
        return f'Preparing {self.count} {self.name}...'
    @classmethod
    def set_recipe(cls, recipe):
        """Sets the recipe for coffee preparation."""
        cls.__recipe = recipe

    @property
    def espresso(self):
        """Returns the amount of espresso required."""
        return self.__recipe.get(self.name, {}).get('espresso', 0) * self.count

    @property
    def milk(self):
        """Returns the amount of milk required."""
        milk_count = 0
        if self.name in self.__recipe:
            for ingr, count in self.__recipe[self.name].items():
                if 'milk' in ingr:
                    milk_count += count
        return milk_count * self.count
    
    def __repr__(self):
        return f'{self.count} {self.name}'
    
    def __eq__(self, other_order):
        """Checks if two orders are equivalent."""

        return isinstance(other_order, Coffee) and self.name == other_order.name and self.count == other_order.count
class FlavorMixin:
    """Adds flavor customization to coffee.
    Attributes:
        sugar(type:int)
        cinammon(type:bool)
        suryp(type:str)
        other_order
    Mehods:
        __str__(), is responsible for returning string representation
        add_flavor(),
        __eq__(), dunder method
    """
    def add_flavor(self, sugar, cinammon, syrup):
        """Adds a flavor to the coffee."""
        if self.is_paid:
            self.sugar = sugar*self.count
            self.cinammon = cinammon
            self.syrup = syrup
            self.flavor = True
        return 'Done!' if self.is_paid else 'Please, pay for it.'

class CustomCoffee(Coffee, FlavorMixin):
    """Represents a custom coffee order with flavors.
    Attributes:
        name(type:str)
        count(type:int)
        flavor(type:bool)
        sugar(type: int)
        cinammon(type:bool)
        suryp(type:bool)
    Methods:
    """
    def __init__(self, name, count = 1, flavor = False, sugar=0, cinammon=False, suryp=None):
        '''The initializer'''
        super().__init__(name, count)
        self.flavor = flavor
    def __str__(self):
        if self.flavor:
            return FlavorMixin.__str__(self)
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        if not self.is_paid:
            if isinstance(self, CustomCoffee):
                return f'Order "{self.count} custom {self.name}" is created.'
            else:
                return f'Order "{self.count} {self.name}" is created.'
        else:
            coffee_desc = f'Your best {self.name} is ready!'
            if self.flavor:
                flavor_desc = f' It has: {self.sugar} stickers of sugar, '
                flavor_desc += 'cinammon, ' if self.cinammon else ''
                flavor_desc += f'{self.syrup} syrup.' if self.syrup else ''
                if self.sugar >= 1:
                    return coffee_desc + flavor_desc
            return coffee_desc
    def __repr__(self):
        return f'{self.count} custom {self.name}'
    def __eq__(self, other):
        if self.flavor:
            return super().__eq__(other) and isinstance(other, CustomCoffee) and self.flavor  == other.flavor
        else:
            return super().__eq__(other)
    
def test_CafeteriaClass():
    """
    Print Done if all tests passed
    """
    print("Testing Cafeteria class...")
    day_track = Track('07.02.2024')
    day_track.date = '07.02.2024'
    order1 = Coffee('latte')
    order2 = Coffee("macchiato")
    assert str(order1) == 'Order cannot be created. Recipe has not been set.'
    assert order1.__dict__ == {'name': 'latte', 'count': 1}
    Coffee.set_recipe(RECIPE)
    order1 = Coffee('latte', 2)
    assert order1.name == 'latte'
    assert order1.count == 2
    assert order1.is_paid is False
    assert order1.espresso == 120
    assert order1.milk == 270
    assert Coffee._Coffee__recipe[order1.name] == {'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15}
    assert str(order1) == 'Order "2 latte" is created.'
    assert Track.MENU == {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    assert day_track.place_order(order1) == 'Done!'
    assert order1.price == 140
    assert order1.is_paid == True
    assert str(order1) == 'Preparing 2 latte...'
    assert len(day_track.orders) == 1
    order2 = Coffee("macchiato")
    assert str(order2) == 'Order "1 macchiato" is created.'
    assert order2.__dict__ == {'name': 'macchiato', 'count': 1, 'is_paid': False}
    assert day_track.place_order(order2) == "Unfortunately, we don't have such kind of coffee in the menu."
    assert len(day_track.orders) == 1

    order2 = Coffee("mocca")
    assert str(order2) == "Order cannot be created. We don't have recipe for it."
    assert order2.__dict__ == {'name': 'mocca', 'count': 1}

    order2 = CustomCoffee('cappuccino')
    assert isinstance(order2, CustomCoffee)
    assert isinstance(order2, Coffee)
    assert isinstance(order2, FlavorMixin)
    assert not isinstance(order1, CustomCoffee)
    assert not isinstance(order1, FlavorMixin)

    assert order2.name == 'cappuccino'
    assert order2.count == 1
    assert order2.espresso == 60
    assert order2.milk == 120
    assert order2.flavor == False

    assert day_track.place_order(order2) == 'Done!'
    assert len(day_track.orders) == 2
    assert str(order2) == 'Preparing 1 cappuccino...', str(order2)
    assert order2.price == 60

    assert order2.add_flavor(2, True, 'almond') == 'Done!'
    assert order2.sugar == 2, order2.sugar
    assert order2.cinammon == True
    assert order2.syrup == 'almond'
    assert str(order2) == 'Your best cappuccino is ready! It has: 2 stickers of sugar, cinammon, almond syrup.',str(order2)


    assert str(day_track.orders) == '[2 latte, 1 custom cappuccino]', str(day_track.orders)
    assert day_track.total_revenue() == 200
    assert day_track.total_milk() == 390

    assert day_track.total_beans() == 36
    assert not isinstance(order2, Track)
    assert Track._Track__beans == 5000
    assert Track._Track__milk == 20000
    assert day_track.beans == 4964
    assert day_track.milk == 19610,  day_track.milk

    order3 = Coffee('Irish Coffee', 3)
    assert day_track.orders == [order1, order2]

    # print(order3 == '5')

    order3 = CustomCoffee('latte', 2)
    assert order3 == order1
    assert order3.add_flavor(3, False, 'green banana') == 'Please, pay for it.'
    assert day_track.place_order(order3) == 'Done!'
    assert order3.add_flavor(3, False, 'green banana') == 'Done!'
    assert order3.sugar == 6, order3.sugar
    assert str(order3) == 'Your best latte is ready! It has: 6 stickers of sugar, green banana syrup.'
    assert order3 != order1
    

    day_track.milk_spoil(19340)
    assert day_track.milk == 0
    order4 = Coffee('latte', 2)
    assert day_track.place_order(order4) == "Unfortunately, we don't have enough ingredients.", day_track.place_order(order4)
    assert len(day_track.orders) == 3
    Track.set_limit_milk(30000)
    assert Track._Track__milk == 30000


    order5 = "Coffee"
    assert not isinstance(order5, CustomCoffee)
    assert day_track.place_order(order5) == "We can't create anything that is not a Coffee instance."

    Track.change_air_state()
    assert Track.safety == False
    order6 = CustomCoffee('lungo', 2)
    assert day_track.place_order(order6) == 'Unfortunately, now it is not safe to make coffee.'
    Track.change_air_state()
    assert Track.safety == True
    order6 = CustomCoffee('lungo')
    assert str(order6) == 'Order "1 custom lungo" is created.', str(order6)
    assert day_track.place_order(order6) == 'Done!'
    assert day_track.total_revenue() ==  390
    assert day_track.total_milk() == 660
    assert day_track.total_beans() == 78
    # print('Done!')


if __name__ == '__main__':
    test_CafeteriaClass()