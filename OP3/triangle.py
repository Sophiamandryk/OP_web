'''Class that is called Triangle'''
import point

class Triangle:
    '''
    The class is responsible for holding info about the coordinates of the point
    Attibutes:
        vertex1(Point), the coordinates of the first point
        vertex2(Point), the coordinates of the first point
        vertex3(Point), the coordinates of the first point
    Mathods:
        __str__() is responsible for returning a string
        is_triangle(), checks whether three points form a triangle

    '''
    def __init__(self, vertex1, vertex2, vertex3):
        '''
        The initializer
        Attributes:
            vertex1(Point), the coordinates of the first point
            vertex2(Point), the coordinates of the first point
            vertex3(Point), the coordinates of the first point
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        '''
        # assert isinstance(vertex1, Point)
        # assert isinstance(vertex2, Point)
        # assert isinstance(vertex3, Point)
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
    def is_triangle(self):
        '''
        Function checks whether three given points form an existing triangle.
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.is_triangle()
        True
        '''
        x1, y1 = self.vertex1.x, self.vertex1.y
        x2, y2 = self.vertex2.x, self.vertex2.y
        x3, y3 = self.vertex3.x, self.vertex3.y
        area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        return area > 0
    def perimeter(self):
        '''
        Calculates the perimeter of the triangle.
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.perimeter()
        6.47213595499958
        '''
        a = ((self.vertex2.x - self.vertex1.x) ** 2 + (self.vertex2.y - self.vertex1.y) ** 2) ** 0.5
        b = ((self.vertex3.x - self.vertex2.x) ** 2 + (self.vertex3.y - self.vertex2.y) ** 2) ** 0.5
        c = ((self.vertex1.x - self.vertex3.x) ** 2 + (self.vertex1.y - self.vertex3.y) ** 2) ** 0.5
        return a + b + c

    def area(self):
        '''
        Calculates the area of the triangle.
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.area()
        2.0
        '''
        a = ((self.vertex2.x - self.vertex1.x) ** 2 + (self.vertex2.y - self.vertex1.y) ** 2) ** 0.5
        b = ((self.vertex3.x - self.vertex2.x) ** 2 + (self.vertex3.y - self.vertex2.y) ** 2) ** 0.5
        c = ((self.vertex1.x - self.vertex3.x) ** 2 + (self.vertex1.y - self.vertex3.y) ** 2) ** 0.5
        s = (a + b + c) / 2 #півпериметр
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
