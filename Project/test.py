import unittest
from utils import add_numbers, subtract_numbers

class TestUtils(unittest.TestCase):
    
    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        print("Addition test passed")

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(10, 5), 5)
        self.assertEqual(subtract_numbers(0, 3), -3)
        print("Subtraction test passed")

if __name__ == '__main__':
    unittest.main()
