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

#     assert day_track.total_revenue() == 200
#     assert day_track.total_milk() == 390
class Track:
    '''Doc'''
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
        if not Track.safety:
            return 'Unfortunately, now it is not safe to make coffee.'
        if order.name in self.MENU:
            order.price = self.MENU[order.name] * order.count
            order.is_paid = True
            self.orders.append(order)
            return "Done!"
        else:
            return "Unfortunately, we don't have such kind of coffee in the menu."
        
    def total_revenue(self):
        total_revenue = 0
        for order in self.orders:
            total_revenue += order.price  # Use the order's price, which was set in place_order
        return total_revenue
    def total_milk(self):
        total_milk = 0
        for order in self.orders:
            total_milk += order.milk
        return total_milk
    def total_beans(self):
        #6 grams for one espresso
        total_beans = 0
        for order in self.orders:
            total_beans += order.espresso
        return (total_beans / 30)*6
    @property
    def beans(self):
        return self.__beans - self.total_beans()
    @property
    def milk(self):
        return self.__milk - self.total_milk()
    # def milk_spoil(self, grams):

    # @property
    # def sugar(self):
    #     return self.sugar * 2
    @classmethod
    def set_limit_milk(cls, new_limit):
        if new_limit > 0:
            cls.__milk = new_limit

    def __str__(self):
        if not isinstance(self, Coffee):
            return "We can't create anything that is not a Coffee instance."
    @classmethod
    def change_air_state(cls):
        cls.safety = not cls.safety
        return f"Safety is now {'safe' if cls.safety else 'not safe'}."

    #@property?
    # def __str__(self):
    #     '''Return a string representation of all orders in the track'''
    #     order_list = [
    #         f"{order.count} {'custom ' if isinstance(order, CustomCoffee) else ''}{order.name}"
    #         for order in self.orders
    #     ]
    #     return f"[{', '.join(order_list)}]"

class Coffee:
    '''Doc'''
    __recipe = {}
    def __init__(self, name, count = 1):
        '''The initializer'''
        self.name = name
        self.count = count
        if self.name in self.__recipe:
            self.is_paid = False

            
    def __str__(self):
        if self.__recipe == {}:
            return "Order cannot be created. Recipe has not been set."
        if self.name not in self.__recipe:
            return "Order cannot be created. We don't have recipe for it."
        if not self.is_paid:
            return f'Order "{self.count} {self.name}" is created.'
        
        
        # if isinstance(self, CustomCoffee) and self.flavor and self.is_paid:
        #     coffee_desc = f'Your best {self.name} is ready!'
        #     flavor_desc = f' It has: {self.sugar} stickers of sugar, '
        #     flavor_desc += 'cinammon, ' if self.cinammon else ''
        #     flavor_desc += f'{self.syrup} syrup.' if self.syrup else ''
        #     return coffee_desc + flavor_desc
        
        return f'Preparing {self.count} {self.name}...'
    @classmethod
    def set_recipe(cls, recipe):
        cls.__recipe = recipe

    @property
    def espresso(self):
        return self.__recipe.get(self.name, {}).get('espresso', 0) * self.count

    @property
    def milk(self):
        milk_count = 0
        if self.name in self.__recipe:
            for ingr, count in self.__recipe[self.name].items():
                if 'milk' in ingr:
                    milk_count += count
        return milk_count * self.count

   
   
   

    
    
class FlavorMixin:
    '''DOC'''
    def __init__(self, sugar:int, cinammon:bool, suryp:str):
        self.sugar = sugar
        self.cinnamom = cinammon
        self.suryp = suryp
        self.flavor = False
    def add_flavor(self, sugar, cinammon, syrup):
        self.sugar = sugar
        self.cinammon = cinammon
        self.syrup = syrup
        self.flavor = True
        return 'Done!'
    
    def __eq__(self, other_order):
        return isinstance(self, Coffee) and isinstance(other_order, Coffee)
    
class CustomCoffee(Coffee, FlavorMixin):
    '''Doc'''
    def __init__(self, name, count = 1, flavor = False, sugar=0, cinammon=False, suryp=None):
        '''The initializer'''
        super().__init__(name, count)
        FlavorMixin.__init__(self, sugar, cinammon, suryp)
        self.flavor = flavor