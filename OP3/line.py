# '''The Line class'''
# class Line:
#     '''The Line class'''
#     def __init__(self, line1: 'Point', line2:"Point"):
#         '''The initializer'''
#         self.line1 = line1
#         self.line2 = line2
#     def intersect(self, other):
#         x1, y1 = self.line1.coor1, self.line1.coor2
#         x2, y2 = self.line2.coor1, self.line2.coor2
#         x3, y3 = other.line1.coor1, other.line1.coor2
#         x4, y4 = other.line2.coor1, other.line2.coor2

#         # Compute determinants
#         denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

#         if denominator == 0:
#             return None  # Parallel or identical lines

#         x_numerator = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
#         y_numerator = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)

#         x = x_numerator / denominator
#         y = y_numerator / denominator

#         return Point(x, y)  # Returns the intersection point

# class Point:
#     '''The point class'''
#     def __init__(self, coor1:float, coor2:float):
#         self.coor1 = coor1
#         self.coor2 = coor2







# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return isinstance(other, Point) and self.x == other.x and self.y == other.y

#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"

# class Line:
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2

#     def intersect(self, other):
#         x1, y1, x2, y2 = self.p1.x, self.p1.y, self.p2.x, self.p2.y
#         x3, y3, x4, y4 = other.p1.x, other.p1.y, other.p2.x, other.p2.y
        
#         denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        
#         if denominator == 0:
#             # Перевіряємо, чи прямі збігаються
#             if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
#                 return self  # Прямі збігаються
#             return None  # Прямі паралельні
        
#         px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
#         py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
        
#         return Point(px, py)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

# class Line:
#     def __init__(self, point1, point2):
#         self.point1 = point1
#         self.point2 = point2

#     def intersect(self, other):
#         # Визначення коефіцієнтів для ліній
#         a1 = self.point2.y - self.point1.y
#         b1 = self.point1.x - self.point2.x
#         c1 = a1 * self.point1.x + b1 * self.point1.y

#         a2 = other.point2.y - other.point1.y
#         b2 = other.point1.x - other.point2.x
#         c2 = a2 * other.point1.x + b2 * other.point1.y

#         determinant = a1 * b2 - a2 * b1

#         if determinant == 0:  # Лінії паралельні або збігаються
#             if c1 == c2:  # Лінії збігаються
#                 return self.point1
#             return None  # Лінії паралельні

#         # Обчислення точки перетину
#         x = (b2 * c1 - b1 * c2) / determinant
#         y = (a1 * c2 - a2 * c1) / determinant
#         return Point(x, y)

# """Line"""
# class Point:
#     """Class for representing a point."""
#     def __init__(self, x, y):
#         """
#         Initializes a point with coordinates (x, y).
#         """
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         """
#         Checks equality between two Point objects.
        
#         :param other: Another Point object to compare
#         :return: True if both objects have the same coordinates, otherwise False
#         """
#         return isinstance(other, Point) and self.x == other.x and self.y == other.y

#     def __repr__(self):
#         """
#         Returns the official string representation of the Point object,
#         which can be used to recreate the object.
#         """
#         return f"Point({self.x}, {self.y})"
















# """Line"""
# class Point:
#     """Class for representing a point."""
#     def __init__(self, x, y):
#         """
#         Initializes a point with coordinates (x, y).
#         """
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         """
#         Checks equality between two Point objects.
        
#         :param other: Another Point object to compare
#         :return: True if both objects have the same coordinates, otherwise False
#         """
#         return isinstance(other, Point) and self.x == other.x and self.y == other.y

#     def __repr__(self):
#         """
#         Returns the official string representation of the Point object,
#         which can be used to recreate the object.
#         """
#         return f"Point({self.x}, {self.y})"

# class Line:
#     """Class for representing a line."""
#     def __init__(self, p1: Point, p2: Point):
#         """
#         Initializes a line by two points.
#         """
#         if p1 == p2:
#             raise ValueError("A line cannot be by two identical points")
#         self.p1 = p1
#         self.p2 = p2

#     def get_slope_and_intercept(self):
#         """
#         Checks if two lines intersect.
#         """
#         x1, y1, x2, y2 = self.p1.x, self.p1.y, self.p2.x, self.p2.y
#         if x1 == x2:
#             return None, x1
#         k = (y2 - y1) / (x2 - x1)
#         b = y1 - k * x1
#         return k, b

#     def intersect(self, other):
#         """
#         Determines the intersection point of two lines.
#         """
#         if self.p1 == other.p1 and self.p2 == other.p2:
#             return self.p1
#         if self.p2 == other.p1:
#             return self.p2
#         if self.p1 == other.p2:
#             return self.p1
#         k1, b1 = self.get_slope_and_intercept()
#         k2, b2 = other.get_slope_and_intercept()
#         if k1 is None and k2 is None:
#             return self if b1 == b2 else None

#         if k1 is None:
#             return Point(b1, k2 * b1 + b2)
#         if k2 is None:
#             return Point(b2, k1 * b2 + b1)

#         if k1 == k2:
#             return self if b1 == b2 else None

#         x = (b2 - b1) / (k1 - k2)
#         y = k1 * x + b1
#         return Point(x, y)

class Point:
    """Represents a point in 2D space."""
    
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Line:
    """Represents a line defined by two distinct points."""
    
    def __init__(self, p1: Point, p2: Point):
        if p1 == p2:
            raise ValueError("A line cannot be defined by two identical points")
        self.p1, self.p2 = p1, p2

    def get_slope_and_intercept(self):
        x1, y1, x2, y2 = self.p1.x, self.p1.y, self.p2.x, self.p2.y
        if x1 == x2:
            return None, x1  # Vertical line
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1
        return slope, intercept

    def intersect(self, other):
        if (self.p1 == other.p1 and self.p2 == other.p2) or (self.p1 == other.p2 and self.p2 == other.p1):
            return self.p1
        
        k1, b1 = self.get_slope_and_intercept()
        k2, b2 = other.get_slope_and_intercept()
        
        if k1 is None and k2 is None:
            return self if b1 == b2 else None
        if k1 is None:
            return Point(b1, k2 * b1 + b2)
        if k2 is None:
            return Point(b2, k1 * b2 + b1)
        if k1 == k2:
            return self if b1 == b2 else None
        
        x = (b2 - b1) / (k1 - k2)
        y = k1 * x + b1
        return Point(round(x, 10), round(y, 10))