import unittest
from app import calculate

class TestApp(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate(10, 2), 5)

    def test_calculate_float(self):
        self.assertEqual(calculate(9, 3), 3)

if __name__ == '__main__':
    unittest.main()
