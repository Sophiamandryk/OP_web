'''This module is for parent class Furniture and child class Chair'''
class Furniture:
    '''Furniture class
    Attributes:
        style(type: str)
        assign(type: str)
    Methods:
        __str__(), return string representation 
        __eq__(), dunder
        get_assign(),returns whatever is in the assign attribute

    '''
    def __init__(self, style:str, assign:str):
        '''the initializer
        >>> furniture1 = Furniture("empire", "bedroom")
        >>> furniture1.assign
        'bedroom'
        '''
        self.style = style
        self.assign = assign
    def __eq__(self, other):
        '''Compares
        >>> furniture1 = Furniture("empire", "bedroom")
        >>> furniture2 = Furniture("modern", "bathroom")
        >>> not (furniture1 == furniture2)
        True
        '''
        return self.style == other.style and self.assign == other.assign
    def __str__(self) -> str:
        '''Returns string representation
        >>> furniture1 = Furniture("empire", "bedroom")
        >>> str(furniture1)
        '<furniture style is empire>'
        '''
        return f"<furniture style is {self.style}>"
    # @property
    # def get_assign(self):
    #     '''The getter for assign attribute

    #     '''
    #     return self._assign
    def get_assign(self):
        '''Getting the assign attribute
        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> chair1.get_assign() == "bedroom"
        True
        '''
        return self.assign

class Chair(Furniture):
    '''
    Chair class, inherits from Furniture class
    Attributes:
        n(type:)
    Methods:
        __str__(), return string representation 
    '''
    def __init__(self, style:str, assign:str, tipe:str):
        '''the initializer
        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> chair1.tipe
        'armchair'
        '''
        super().__init__(style, assign)
        self.tipe = tipe
    def __str__(self):
        '''Returns a string representation
        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> str(chair1)
        '<This armchair furniture style is empire>'
        '''
        return f"<This {self.tipe} furniture style is {self.style}>"

# furniture1 = Furniture("empire", "bedroom")

# furniture2 = Furniture("modern", "bathroom")

# assert(not (furniture1 == furniture2))

# assert(furniture1.style == "empire")

# assert(furniture1.assign == "bedroom")

# assert(str(furniture1) == "<furniture style is empire>")

# chair1 = Chair("empire", "bedroom", "armchair")

# assert(chair1.tipe == "armchair")

# assert(isinstance(chair1, Furniture))

# assert(str(chair1) == "<This armchair furniture style is empire>")

# assert(chair1.get_assign() == "bedroom")

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())