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
                flavor_desc = f'It has: '
                sugar_word = 'stickers of sugar, ' if self.sugar > 1 else 'sticker'
                sug = f'{self.sugar} {sugar_word}'
                sin = 'cinammon, ' if self.cinammon else ''
                sur = f'{self.syrup} syrup.' if self.syrup else ''
                if self.sugar >= 1:
                    return flavor_desc + sug + sin + sur
                return flavor_desc + sin + sur
            return coffee_desc
    def __repr__(self):
        return f'{self.count} custom {self.name}'
    def __eq__(self, other):
        if self.flavor:
            return super().__eq__(other) and isinstance(other, CustomCoffee) and self.flavor  == other.flavor
        else:
            return super().__eq__(other)
    

