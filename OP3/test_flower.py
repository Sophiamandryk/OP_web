import unittest
from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket

class TestFlower(unittest.TestCase):
    def setUp(self):
        self.flower = Flower('blue', 3, 12)
        self.flower_negative_price = Flower('blue', 3, -12)
        self.flower_negative_petals = Flower('blue', -3, 12)
        self.flower_color_str = Flower([12], 3, 12)
        self.flower_valid_price = Flower('red', '4', 10)  # valid flower with price of 10
        self.flower_valid_petals = Flower('yellow', '5', 15)  # valid flower with valid petals
    def test_simple(self):
        '''Checks the simplest algorythm work'''
        self.assertEqual(self.flower.color, 'blue')
    def test_negativeprice(self):
        with self.assertRaises(ValueError):
            self.flower_negative_price.price = -12
    def test_negativepetals(self):
        with self.assertRaises(ValueError):
            self.flower_negative_petals.petals = -3
    def test_color_str(self):
        with self.assertRaises(ValueError):
            self.flower_color_str.color = [12]
    def test_set_valid_price(self):
        '''Checks if valid price can be set'''
        self.flower_valid_price.price = 20
        self.assertEqual(self.flower_valid_price.price, 20)

    def test_set_valid_petals(self):
        '''Checks if valid petals can be set'''
        self.flower_valid_petals.petals = 6
        self.assertEqual(self.flower_valid_petals.petals, 6)

    def test_set_valid_color(self):
        '''Checks if valid color can be set'''
        self.flower.color = 'green'
        self.assertEqual(self.flower.color, 'green')

    def test_create_flower(self):
        '''Test flower initialization'''
        new_flower = Flower('purple', 7, 25)
        self.assertEqual(new_flower.color, 'purple')
        self.assertEqual(new_flower.petals, 7)
        self.assertEqual(new_flower.price, 25)

    def test_tulip_init(self):
        tulip = Tulip(5, 20)
        self.assertEqual(tulip.color, 'pink')
        self.assertEqual(tulip.petals, 5)
        self.assertEqual(tulip.price, 20)
    def test_rose_init(self):
        rose = Rose(3,12)
        self.assertEqual(rose.color, 'red')
        self.assertEqual(rose.petals, 3)
        self.assertEqual(rose.price, 12)
    def test_chamomile_init(self):
        chamomile = Chamomile(3,12)
        self.assertEqual(chamomile.color, 'white')
        self.assertEqual(chamomile.petals, 3)
        self.assertEqual(chamomile.price, 12)
    def test_flowerset_init(self):
        flowerset = FlowerSet()
        self.assertEqual(flowerset.flowers, set())
    # def test_addflower_isinstance(self):
    #     with self.assertRaises(ValueError):
    #         flower = Bucket()
    def test_add_flower_isinstance(self):
        '''Test that only Flower instances can be added to FlowerSet'''
        flower_set = FlowerSet()
        flower = Flower('red', 5, 10)
        flower_set.add_flower(flower)
        
        # Invalid addition (Bucket is not a Flower)
        with self.assertRaises(ValueError):
            flower_set.add_flower(Bucket())

    def test_bucket_add_set(self):
        '''Test adding FlowerSet to Bucket'''
        flower_set = FlowerSet()
        flower_set.add_flower(self.flower)
        bucket = Bucket()
        bucket.add_set(flower_set)
        self.assertIn(flower_set, bucket.flower_sets)

    def test_bucket_total_price(self):
        '''Test total price calculation in bucket'''
        flower_set = FlowerSet()
        flower_set.add_flower(self.flower)
        bucket = Bucket()
        bucket.add_set(flower_set)
        self.assertEqual(bucket.total_price(), 12)


if __name__ == '__main__':
    unittest.main()
# coverage run test_flower.py


# import unittest
# from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket

# class TestFlower(unittest.TestCase):
#     def setUp(self):
#         self.flower = Flower('blue', 3, 12)

#     def test_initialization(self):
#         '''Test Flower class initialization'''
#         flower = Flower('red', 5, 15)
#         self.assertEqual(flower.color, 'red')
#         self.assertEqual(flower.petals, 5)
#         self.assertEqual(flower.price, 15)

#     def test_set_valid_price(self):
#         '''Check valid price can be set'''
#         self.flower.price = 20
#         self.assertEqual(self.flower.price, 20)

#     def test_set_price_zero(self):
#         '''Check if price can be set to zero'''
#         self.flower.price = 0
#         self.assertEqual(self.flower.price, 0)

#     def test_invalid_price(self):
#         '''Ensure invalid price raises ValueError'''
#         with self.assertRaises(ValueError):
#             self.flower.price = -5
#         with self.assertRaises(ValueError):
#             self.flower.price = "ten"

#     def test_set_valid_petals(self):
#         '''Check valid petals can be set'''
#         self.flower.petals = 6
#         self.assertEqual(self.flower.petals, 6)

#     def test_set_petals_zero(self):
#         '''Check if petals can be set to zero'''
#         self.flower.petals = 0
#         self.assertEqual(self.flower.petals, 0)

#     def test_invalid_petals(self):
#         '''Ensure invalid petals raise ValueError'''
#         with self.assertRaises(ValueError):
#             self.flower.petals = -3
#         with self.assertRaises(ValueError):
#             self.flower.petals = "five"

#     def test_set_valid_color(self):
#         '''Check valid color can be set'''
#         self.flower.color = 'green'
#         self.assertEqual(self.flower.color, 'green')

#     def test_invalid_color(self):
#         '''Ensure non-string colors raise ValueError'''
#         with self.assertRaises(ValueError):
#             self.flower.color = 123

#     def test_change_properties_multiple_times(self):
#         '''Test changing properties multiple times'''
#         self.flower.color = 'red'
#         self.flower.petals = 10
#         self.flower.price = 30
#         self.assertEqual(self.flower.color, 'red')
#         self.assertEqual(self.flower.petals, 10)
#         self.assertEqual(self.flower.price, 30)

# class TestFlowerSubclasses(unittest.TestCase):
#     def test_tulip(self):
#         '''Check Tulip initialization'''
#         tulip = Tulip(7, 20)
#         self.assertEqual(tulip.color, 'pink')
#         self.assertEqual(tulip.petals, 7)
#         self.assertEqual(tulip.price, 20)

#     def test_rose(self):
#         '''Check Rose initialization'''
#         rose = Rose(10, 30)
#         self.assertEqual(rose.color, 'red')
#         self.assertEqual(rose.petals, 10)
#         self.assertEqual(rose.price, 30)

#     def test_chamomile(self):
#         '''Check Chamomile initialization'''
#         chamomile = Chamomile(12, 5)
#         self.assertEqual(chamomile.color, 'white')
#         self.assertEqual(chamomile.petals, 12)
#         self.assertEqual(chamomile.price, 5)

# class TestFlowerSet(unittest.TestCase):
#     def setUp(self):
#         self.flower_set = FlowerSet()
#         self.flower1 = Flower('yellow', 6, 10)
#         self.flower2 = Flower('red', 8, 15)

#     def test_add_flower(self):
#         '''Test adding a Flower to FlowerSet'''
#         self.flower_set.add_flower(self.flower1)
#         self.assertIn(self.flower1, self.flower_set.flowers)

#     def test_add_multiple_flowers(self):
#         '''Test adding multiple flowers'''
#         self.flower_set.add_flower(self.flower1)
#         self.flower_set.add_flower(self.flower2)
#         self.assertIn(self.flower1, self.flower_set.flowers)
#         self.assertIn(self.flower2, self.flower_set.flowers)

#     def test_add_invalid_flower(self):
#         '''Ensure non-Flower objects raise ValueError'''
#         with self.assertRaises(ValueError):
#             self.flower_set.add_flower("Not a flower")

# class TestBucket(unittest.TestCase):
#     def setUp(self):
#         self.bucket = Bucket()
#         self.flower_set1 = FlowerSet()
#         self.flower_set2 = FlowerSet()
#         self.flower_set1.add_flower(Flower('red', 5, 20))
#         self.flower_set1.add_flower(Flower('blue', 8, 15))
#         self.flower_set2.add_flower(Flower('white', 12, 5))

#     def test_add_flower_set(self):
#         '''Test adding FlowerSet to Bucket'''
#         self.bucket.add_set(self.flower_set1)
#         self.assertIn(self.flower_set1, self.bucket.flower_sets)

#     def test_add_multiple_flower_sets(self):
#         '''Test adding multiple FlowerSets'''
#         self.bucket.add_set(self.flower_set1)
#         self.bucket.add_set(self.flower_set2)
#         self.assertIn(self.flower_set1, self.bucket.flower_sets)
#         self.assertIn(self.flower_set2, self.bucket.flower_sets)

#     def test_add_invalid_set(self):
#         '''Ensure non-FlowerSet objects raise ValueError'''
#         with self.assertRaises(ValueError):
#             self.bucket.add_set("Not a flower set")

#     def test_total_price(self):
#         '''Check total price calculation in Bucket'''
#         self.bucket.add_set(self.flower_set1)
#         self.bucket.add_set(self.flower_set2)
#         self.assertEqual(self.bucket.total_price(), 40)  # 20 + 15 + 5

#     def test_empty_bucket_price(self):
#         '''Check price for an empty Bucket'''
#         self.assertEqual(self.bucket.total_price(), 0)

# if __name__ == '__main__':
#     unittest.main()
