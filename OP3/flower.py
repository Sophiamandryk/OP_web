'''The flower class'''
class Flower:
    '''Class Flower'''
    def __init__(self, color, petals, price):
        self._color = color
        self._petals = petals
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not (isinstance(value, int) and value >= 0):
            raise ValueError
        self._price = value
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, other):
        if not (isinstance(other, str)):
            raise ValueError
        self._color = other
    @property
    def petals(self):
        return self._petals
    @petals.setter
    def petals(self, other):
        if not (isinstance(other, int) and other >= 0):
            raise ValueError
        self._petals = other

class Tulip(Flower):
    """Tulip class with fixed color 'pink'."""
    def __init__(self, petals: int, price: int):
        super().__init__('pink', petals, price)

class Rose(Flower):
    """Rose class with fixed color 'red'."""
    def __init__(self, petals: int, price: int):
        super().__init__('red', petals, price)

class Chamomile(Flower):
    """Chamomile class with fixed color 'white'."""

    def __init__(self, petals: int, price: int):
        super().__init__('white', petals, price)

class FlowerSet:
    '''FlowerSet class'''
    def __init__(self):
        self.flowers = set()
    def add_flower(self, flower):
        if not isinstance(flower, Flower):
            raise ValueError
        self.flowers.add(flower)

class Bucket:
    '''Bucket class'''
    def __init__(self):
        self.flower_sets = []
    def add_set(self, new_set):
        if not isinstance(new_set, FlowerSet):
            raise ValueError
        self.flower_sets.append(new_set)
    def total_price(self):
        total_price = 0
        for sset in self.flower_sets:
            for flower in sset.flowers:
                total_price += flower.price
        return total_price