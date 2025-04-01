'''bird'''

import types
class Bird:
    '''The Bird class'''
    def __init__(self, name):
        '''The initializer
        >>> bird1 = Bird("Parrot")
        >>> bird1.name
        'Parrot'
        >>> bird1.count_eggs()
        0
        '''
        self.name = name
        self.eggs = []
        self.layed_eggs = 0
    def fly(self):
        '''If it's a bird, it says that it can fly
        >>> bird1 = Bird("Parrot")
        >>> bird1.fly() == "I can fly!"
        True
        '''
        return 'I can fly!'
    # def swim(self):
    #     '''Returns whether it can swim'''
    #     if isinstance(self, Penguin):
    #         return "I can swim!"
    def count_eggs(self):
        '''Cound the eggs
        >>> bird1 = Bird("Parrot")
        >>> bird1.count_eggs()
        0
        >>> bird1.lay_egg()
        >>> bird1.count_eggs()
        1
        '''
        return self.layed_eggs
    # def __str__(self):
    #     '''Returns the string representation
    #     >>> bird1 = Bird("Parrot")
    #     >>> str(bird1)
    #     'Parrot has 0 eggs'
    #     >>> bird1.lay_egg()
    #     >>> str(bird1)
    #     'Parrot has 1 egg'
    #     '''
    #     egg_name = 'egg' if self.layed_eggs == 1 else 'eggs'
    #     return f'{self.name} has {self.layed_eggs} {egg_name}'
    def lay_egg(self):
        '''Lays the eggs
        >>> bird1 = Bird("Parrot")
        >>> bird1.count_eggs()
        0
        >>> bird1.lay_egg()
        >>> bird1.count_eggs()
        1
        '''
        egg = Egg()
        self.eggs.append(egg)
        self.layed_eggs += 1
    def get_eggs(self):
        '''Gets the eggs
        >>> bird1 = Bird("Parrot")
        >>> bird1.get_eggs()
        []
        >>> bird1.lay_egg()
        >>> len(bird1.get_eggs())
        1
        '''
        return self.eggs
    def __repr__(self):
        '''Returns a representation for the developer
        >>> bird1 = Bird("Parrot")
        >>> repr(bird1)
        'Bird'
        '''
        egg_name = 'egg' if self.layed_eggs == 1 else 'eggs'
        return f'{self.name} has {self.layed_eggs} {egg_name}'
        # return self.__class__.__name__


class Egg:
    '''The Egg class'''

class Penguin(Bird):
    '''The Penguin class'''
    # def __init__(self, name):
    #     super().__init__(name)
    def fly(self):
        '''Penguins cannot fly
        >>> penguin = Penguin("Emperor")
        >>> penguin.fly()
        'No flying for me.'
        '''
        return "No flying for me."
    def swim(self):
        '''Returns whether it can swim
        >>> penguin = Penguin("Emperor")
        >>> penguin.swim()
        'I can swim!'
        '''
        if isinstance(self, Penguin):
            return "I can swim!"

class MessengerBird(Bird):
    '''The MessengerBird class'''
    def __init__(self, name, message = ''):
        '''The initializer
        >>> bird = MessengerBird("War Pigeon", "Secret Message")
        >>> bird.name
        'War Pigeon'
        >>> bird.message
        'Secret Message'
        '''
        super().__init__(name)
        self.message = message
    def deliver_message(self):
        '''Delivers the message
        >>> bird = MessengerBird("War Pigeon", "Secret Message")
        >>> bird.deliver_message()
        'Secret Message'
        '''
        return f'{self.message}'


def get_local_methods(clss):
    '''local methods
    '''
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = []
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if isinstance(val, types.FunctionType):
            result.append(var)
    return sorted(result)


def test_bird_classes():
    print("Testing Bird classes...")
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert isinstance(bird1, Bird)
    assert bird1.fly() == "I can fly!"
    assert bird1.count_eggs() == 0
    assert str(bird1) == "Parrot has 0 eggs"

    # here changes
    # bird1.lay_egg()
    assert bird1.lay_egg() is None
    eggs = bird1.get_eggs()
    egg = eggs.pop()
    assert isinstance(egg, Egg)
    #here changes ends
    assert bird1.count_eggs() == 1
    assert str(bird1) == "Parrot has 1 egg"
    assert bird1.lay_egg() is None
    assert bird1.count_eggs() == 2
    assert str(bird1) == "Parrot has 2 eggs"
    assert get_local_methods(Bird) == ['__init__', '__repr__', 'count_eggs', 'fly', 'get_eggs', 'lay_egg']

    # # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert isinstance(bird2, Penguin)
    assert isinstance(bird2, Bird)
    assert bird2.fly() == "No flying for me."
    assert bird2.swim() == "I can swim!"
    bird2.lay_egg()
    assert bird2.count_eggs() == 1
    assert str(bird2) == "Emperor Penguin has 1 egg"
    assert get_local_methods(Penguin) == ['fly', 'swim']

    # # A MessengerBird is a Bird that can optionally carry a message
    bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
    assert isinstance(bird3, MessengerBird)
    assert isinstance(bird3, Bird)
    assert not isinstance(bird3, Penguin)
    assert bird3.deliver_message() == "Top-Secret Message!"
    assert str(bird3) == "War Pigeon has 0 eggs"
    assert bird3.fly() == "I can fly!"

    bird4 = MessengerBird("Homing Pigeon")
    assert bird4.deliver_message() == ""
    bird4.lay_egg()
    assert bird4.count_eggs() == 1
    assert get_local_methods(MessengerBird) == ['__init__', 'deliver_message']
    # print("Done!")


if __name__ == '__main__':
    # import doctest
    # print(doctest.testmod())
    test_bird_classes()