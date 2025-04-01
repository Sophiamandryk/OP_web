'''Lalala'''

class Point:
    def __init__(self, x:float, y:float) -> None:
        self.x, self.y = x, y
    def __str__(self) -> str:
        return f"Point in two-dimensional space with coordinates ({self.x}, {self.y})"
    def __repr__(self) -> str:
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other: 'Point') -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

class Point2D(Point):
    def __init__(self, x:float, y:float, z:float) -> None:
        super().__init__(x,y)
        self.z = z
    def __str__(self) -> str:
        return f"Point in three-dimensional space with coordinates ({self.x}, {self.y}, {self.x})"
    def __repr__(self) -> str:
        return f'Point{x=}'


point1 =Point(17, 2)
assert (point1.y, point1.x) == (2, 17)
assert str(point1) == "Point in two-dimensional space with coordinates (17, 2)"

point2 = Point3D(17, 4, 2)
assert (point2.y, point2.z, point2.x) == (4, 2, 17)
assert str(point2) == "Point in three-dimensional space with coordinates (17, 4, 2)"
assert str([point1, point2]) == "[Point(x=17, y=2), Point(x=17, y=4, z=2)]"

assert Point(3, 4) == Point(3, 4)
assert Point(3, 4) != Point(2, 3)

assert Point(5, 4) == Point3D(5, 4, 0)
assert Point3D(5, 4, 0) == Point(5, 4)

assert Point(5, 4) != Point3D(5, 4, 1)
assert Point3D(5, 4, 1) != Point(5, 4)

assert Point3D(8, 7, 0) == Point3D(8, 7)

assert Point(3, 4).vector_length() == 5
assert Point(4, 5).vector_length() == 6.4
assert Point(6, -12).vector_length() == 13.42
assert Point(100, 0).vector_length() == 100

assert Point3D(-6, -12, 0).vector_length() == 13.42
assert Point3D(3, 4, 12).vector_length() == 13
assert Point3D(-13, 14, -15).vector_length() == 24.29