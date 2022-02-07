import unittest
from main import suma


class TestSuma(unittest.TestCase):
    def test_positive_negative_result_zero(self):
        a = 9
        b = -9
        c = suma(a, b)

        self.assertTrue(c == 0)
