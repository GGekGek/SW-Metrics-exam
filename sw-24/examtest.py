import unittest
import math


def sqrt(val):
    if not isinstance(val, int):
        return TypeError
    if val < 0:
        return ValueError
    return math.sqrt(val)


class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqrt(36), 6)  # Test for positive numbers
        self.assertEqual(sqrt(16), 4)
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)  # Test for 0
        self.assertAlmostEqual(sqrt(2), 1.41421356, places=8)
        # Test for non integrer number
        self.assertEqual(sqrt(-1), ValueError)
        # Test for negative number
        self.assertEqual(sqrt("a"), TypeError)
        # Test for a value different than a number


if __name__ == '__main__':
    unittest.main()
