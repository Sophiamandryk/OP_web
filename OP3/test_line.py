# '''The module that tests the line.py'''
# import unittest
# from line import Line, Point

# class TestLine(unittest.TestCase):
#     def setUp(self):
#         self.line1 = Line(Point(0, 0), Point(2, 2))
#         self.line2 = Line(Point(0, 2), Point(2, 0))  # Перетинається у (1,1)
#         self.line3 = Line(Point(0, 1), Point(2, 3))  # Не перетинається
#         self.line4 = Line(Point(1, 1), Point(3, 3))  # Колінеарна з line1, але не збігається
#         self.line5 = Line(Point(0, 0), Point(2, 2))  # Повністю збігається з line1
#         self.line6 = Line(Point(1, 1), Point(4, 4))  # Перетинається з line1 у (1,1)

#     def test_intersection_exists(self):
#         result = self.line1.intersect(self.line2)
#         self.assertIsInstance(result, Point)
#         self.assertAlmostEqual(result.coor1, 1.0)
#         self.assertAlmostEqual(result.coor2, 1.0)

#     def test_no_intersection(self):
#         result = self.line1.intersect(self.line3)
#         self.assertIsNone(result)

#     def test_parallel_lines(self):
#         result = self.line1.intersect(self.line4)
#         self.assertIsNone(result)

#     def test_identical_lines(self):
#         result = self.line1.intersect(self.line5)
#         self.assertEqual(result, self.line1.line1)  # Має повернути першу точку

#     def test_intersection_at_one_point(self):
#         result = self.line1.intersect(self.line6)
#         self.assertIsInstance(result, Point)
#         self.assertAlmostEqual(result.coor1, 1.0)
#         self.assertAlmostEqual(result.coor2, 1.0)

# if __name__ == "__main__":
#     unittest.main()



import unittest
from line import Point, Line

class TestLine(unittest.TestCase):
    def setUp(self):
        self.l1 = Line(Point(0, 0), Point(1, 1))
        self.l2 = Line(Point(0, 1), Point(1, 0))
        self.l3 = Line(Point(0, 0), Point(2, 2))  # Збігається з l1
        self.l4 = Line(Point(0, 0), Point(0, 1))  # Вертикальна
        self.l5 = Line(Point(1, 0), Point(1, 1))  # Вертикальна
        self.l6 = Line(Point(2, 0), Point(2, 2))  # Вертикальна
    
    def tearDown(self):
        pass
    
    def test_intersection(self):
        self.assertEqual(self.l1.intersect(self.l2), Point(0.5, 0.5))
    
    def test_no_intersection(self):
        self.assertIsNone(self.l4.intersect(self.l5))
    
    def test_coincident_lines(self):
        self.assertEqual(self.l1.intersect(self.l3), self.l1)
    
    def test_parallel_lines(self):
        self.assertIsNone(self.l4.intersect(self.l6))
    
    def test_intersection_vertical_horizontal(self):
        self.assertEqual(self.l4.intersect(self.l2), Point(0, 0.5))
    
    def test_intersection_diagonal(self):
        self.assertEqual(self.l2.intersect(self.l3), Point(0.5, 0.5))

if __name__ == "__main__":
    unittest.main()



# import unittest
# from line import Point, Line

# class TestLine(unittest.TestCase):

#     def setUp(self):
#         # Створення тестових ліній
#         self.line1 = Line(Point(0, 0), Point(1, 1))  # y = x
#         self.line2 = Line(Point(0, 1), Point(1, 0))  # y = 1 - x
#         self.line3 = Line(Point(0, 0), Point(1, 1))  # y = x (збігається з line1)
#         self.line4 = Line(Point(0, 2), Point(1, 2))  # y = 2 (паралельна line1)
#         self.line5 = Line(Point(0, 0), Point(0, 1))  # вертикальна лінія
#         self.line6 = Line(Point(1, 0), Point(1, 1))  # вертикальна лінія, паралельна line5

#     def tearDown(self):
#         pass  # Тут можна очистити ресурси, якщо потрібно

#     def test_intersect(self):
#         # Тест на перетин
#         intersection = self.line1.intersect(self.line2)
#         self.assertEqual(intersection, Point(0.5, 0.5))

#     def test_no_intersect(self):
#         # Тест на відсутність перетину
#         intersection = self.line4.intersect(self.line1)
#         self.assertIsNone(intersection)

#     def test_coincide(self):
#         # Тест на збігання
#         intersection = self.line1.intersect(self.line3)
#         self.assertEqual(intersection, self.line1.point1)

#     def test_parallel_lines(self):
#         # Тест на паралельні лінії
#         intersection = self.line4.intersect(self.line6)
#         self.assertIsNone(intersection)

#     def test_vertical_lines_intersect(self):
#         # Тест на перетин вертикальних ліній
#         line7 = Line(Point(0, 0), Point(0, 1))  # вертикальна лінія
#         intersection = self.line5.intersect(line7)
#         self.assertEqual(intersection, Point(0, 0))

#     def test_vertical_lines_no_intersect(self):
#         # Тест на відсутність перетину вертикальних ліній
#         intersection = self.line5.intersect(self.line6)
#         self.assertIsNone(intersection)

# if __name__ == '__main__':
#     unittest.main()