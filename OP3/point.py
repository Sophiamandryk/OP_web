'''The class called Point'''
class Point:
    '''
    The class is responsible for holding info about the coordinates of the point
    Attibutes:
        x(int), the x coordinate
        y(int), the y coordinate
    Mathods:
        __str__() is responsible for returning a string
    '''
    def __init__(self, x, y):
        '''
        The initializer
        Attributes:
            x(Point), the first coordinate
            y(Point), the second coordinate
        >>> point = Point(1, 2)
        >>> point.x
        1
        >>> point.y
        2
        '''
        self.x = x
        self.y = y
    def __str__(self):
        '''
        The __str__() method, returns a string
        >>> point = Point(1, 2)
        >>> print(point)
        x-coordinate of the point is 1, and y-coordinate is 2.
        '''
        return f'x-coordinate of the point is {self.x}, and y-coordinate is {self.y}.'
    
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
