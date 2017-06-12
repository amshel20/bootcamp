import unittest
from converter import converter

class Test_converter(unittest.TestCase):
    def test_conversion(self):
        actual=converter(10)
        expected =50

        self.assertEqual(actual, expected)
        pass
