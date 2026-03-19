import unittest
from app import calculate

class TestApp(unittest.TestCase):

    def test_calculate(self):
        self.assertEqual(calculate(10, 2), 5)

    def test_calculate_float(self):
        self.assertEqual(calculate(9, 3), 3)

    def test_negative_numbers(self):
        self.assertEqual(calculate(-10, 2), -5)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0)

    def test_zero_result(self):
        self.assertEqual(calculate(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
