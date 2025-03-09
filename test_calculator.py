import unittest
from calculator import add, subtract, multiply, divide, square_root

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(1, 1), 0)
        
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-1, 1), -1)
        
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(2), 2 ** 0.5)
        with self.assertRaises(ValueError):
            square_root(-1)

if __name__ == '__main__':
    unittest.main() 