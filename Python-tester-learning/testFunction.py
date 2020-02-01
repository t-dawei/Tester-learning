import unittest
from func import Func


class MyTestCase(unittest.TestCase):
    def test_twosum(self):
        fc = Func()
        self.assertEqual(fc.two_sum(2, 3), 5)
        self.assertEqual(fc.two_sum(2, 4), 6)
        self.assertEqual(fc.two_sum(2, 5), 7)
        self.assertEqual(fc.two_sum(2, 6), 8)

    def test_twomul(self):
        fc = Func()
        self.assertEqual(fc.two_mul(2, 3), 6)


if __name__ == '__main__':
    unittest.main()
