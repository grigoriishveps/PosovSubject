import unittest
from binary_search import binary_search


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.test_array = [1, 2, 2, 4, 8, 8, 8, 10, 11, 12, 17, 18, 21]

    def test_left(self):
        self.assertEqual(0, binary_search(self.test_array, 1))

    def test_right(self):
        self.assertEqual(12, binary_search(self.test_array, 21))

    def test_2(self):
        self.assertEqual(1, binary_search(self.test_array, 2))

    def test_4(self):
        self.assertEqual(3, binary_search(self.test_array, 4))

    def test_8(self):
        self.assertEqual(4, binary_search(self.test_array, 8))

    def test_12(self):
        self.assertEqual(9, binary_search(self.test_array, 12))

    def test_18(self):
        self.assertEqual(11, binary_search(self.test_array, 18))

    def test_not(self):
        self.assertEqual(-1, binary_search(self.test_array, 3))
