import unittest
from main import divide_numbers

class TestDivideNumbers(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide_numbers(12, 3), 4)
        self.assertEqual(divide_numbers(10, 2), 5)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(3, 0)
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            divide_numbers('numerator', 2)
            divide_numbers(10, 'denominator')
            divide_numbers('numerator', 'denominator')

if __name__ == '__main__':
    unittest.main()
