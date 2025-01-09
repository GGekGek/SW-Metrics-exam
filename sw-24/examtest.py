import unittest
import math

class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(math.sqrt(36), 6)
        self.assertEqual(math.sqrt(16), 4)
        self.assertEqual(math.sqrt(9), 3)
        self.assertEqual(math.sqrt(0), 0)

if __name__ == '__main__':
    unittest.main()