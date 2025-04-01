'''Tests the function square_preceding'''
import unittest
from square_preceding import square_preceding

class TestSquare(unittest.TestCase):
    '''TestVector '''
    # def setUp(self):
    #     self.l = [1, 2, 3]
    #     square_preceding(self.l)
    def test_simple(self):
        '''Tests the whole ides'''
        l = [1, 2, 3]
        square_preceding(l)
        self.assertEqual(l, [0, 1, 4])
    def test_zerofirst(self):
        '''Tests whether the first one is 0'''
        l = [1, 2, 3]
        square_preceding(l)
        self.assertEqual(l[0], 0)
    def test_emptylist(self):
        '''Tests what happens on an empty list'''
        l = []
        square_preceding(l)
        self.assertEqual(l, [])
    def test_allzeros(self):
        '''Checks what happens when every item is zero'''
        l = [0,0,0]
        square_preceding(l)
        self.assertEqual(l, [0,0,0])
    def test_onenumber(self):
        '''Checks what happens when there's only one number'''
        l = [2]
        square_preceding(l)
        self.assertEqual(l, [0])
    def test_samenumbers(self):
        '''Checks on the same numbers'''
        l = [2,2,2]
        square_preceding(l)
        self.assertEqual(l, [0, 4, 4])


if __name__ == "__main__":
    unittest.main()



# test_square_preceding.py

# import unittest
# from square_preceding import square_preceding

# class TestSquare(unittest.TestCase):
#     '''TestSquare class'''
    
#     def test_simple(self):
#         '''Tests the basic functionality'''
#         l = [1, 2, 3]
#         square_preceding(l)
#         self.assertEqual(l, [0, 1, 4])
    
#     def test_zerofirst(self):
#         '''Tests whether the first item is 0'''
#         l = [1, 2, 3]
#         square_preceding(l)
#         self.assertEqual(l[0], 0)
    
#     def test_emptylist(self):
#         '''Tests what happens on an empty list'''
#         l = []
#         square_preceding(l)
#         self.assertEqual(l, [])
    
#     def test_allzeros(self):
#         '''Checks what happens when every item is zero'''
#         l = [0, 0, 0]
#         square_preceding(l)
#         self.assertEqual(l, [0, 0, 0])
    
#     def test_onenumber(self):
#         '''Checks what happens when there's only one number'''
#         l = [2]
#         square_preceding(l)
#         self.assertEqual(l, [0])
    
#     def test_samenumbers(self):
#         '''Checks on the same numbers'''
#         l = [2, 2, 2]
#         square_preceding(l)
#         self.assertEqual(l, [0, 4, 4])
    
#     def test_negative_numbers(self):
#         '''Checks behavior with negative numbers'''
#         l = [-1, -2, -3]
#         square_preceding(l)
#         self.assertEqual(l, [0, -1, 1])
    
#     def test_large_numbers(self):
#         '''Checks behavior with large numbers'''
#         l = [1000, 2000, 3000]
#         square_preceding(l)
#         self.assertEqual(l, [0, 1000000, 4000000000])
    
#     def test_floats(self):
#         '''Checks behavior with float numbers'''
#         l = [1.5, 2.5, 3.5]
#         square_preceding(l)
#         self.assertEqual(l, [0, 2.25, 6.25])

# if __name__ == "__main__":
#     unittest.main()

# class TestVector(unittest.TestCase):
#     def setUp(self):
#         self.a = Vector([1, 2, 3])
#         self.b = Vector([4, 5, 6])
#         self.short_b = Vector([4, 5])

#     def test_add(self):
#         c = self.a + self.b
#         self.assertEqual(c.values, [5, 7, 9])

#     def test_add_different_lengths(self):
#         self.assertRaises(ValueError, lambda: self.a + self.short_b)

#     def test_mul(self):
#         c = self.a * self.b
#         self.assertEqual(c, 32)

#     def test_mul_different_lengths(self):
#         self.assertRaises(ValueError, lambda: self.a * self.short_b)
