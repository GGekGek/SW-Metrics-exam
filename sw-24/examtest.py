import unittest
import math


class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(math.sqrt(36), 6)  # Test for positive numbers
        self.assertEqual(math.sqrt(16), 4)
        self.assertEqual(math.sqrt(9), 3)
        self.assertEqual(math.sqrt(0), 0)  # Test for 0
        self.assertAlmostEqual(math.sqrt(2), 1.41421356, places=8)
        # Test for non integrer number
        with self.assertRaises(ValueError):  # Test for negative number
            math.sqrt(-1)
        with self.assertRaises(TypeError):
            # Test for a value different than a number
            math.sqrt("a")


if __name__ == '__main__':
    unittest.main()
