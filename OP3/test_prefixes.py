'''Tests the prefixes function'''
import unittest
from all_prefixes import all_prefixes
class TestPrefixes(unittest.TestCase):
    '''Tests the function called all_prefixes'''
    def setUp(self):
        '''Sets up the instances to work with'''
        self.simple_case = all_prefixes('lead')
        self.hard_case = all_prefixes('авангард')
        self.one_letter = all_prefixes('h')
        self.same_letter = all_prefixes('lll')
    def test_simple_case(self):
        '''Tests the case with four letters, no repetition, one first'''
        result = {"l", "le", "lea", "lead"}
        self.assertEqual(self.simple_case, result)
    def test_hard_case(self):
        '''Tests the case with more than one first letter'''
        result = {"а", "ав", "ава", "аван", "аванг", "аванга", "авангар", "авангард", "ан", "анг", "анга", "ангар", "ангард", "ар", "ард"}
        self.assertEqual(self.hard_case, result)
    def test_one_letter(self):
        '''Tests the case with one letter'''
        result = {'h'}
        self.assertEqual(self.one_letter, result)
    def test_same_letters(self):
        '''Tests the case with one repetitive letter'''
        result = {'l', 'll', 'lll'}
        self.assertEqual(self.same_letter, result)
if __name__ == '__main__':
    unittest.main()