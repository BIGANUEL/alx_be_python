import unittest
from simple_calculator import SimpleCalculator

class TestCase(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(3,5), 8)
        self.assertEqual(self.calc.add(4,6), 10)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3,5),-2)
        self.assertEqual(self.calc.subtract(9,9),0)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3,5),15)
        self.assertEqual(self.calc.multiply(9,9),81)
    def test_division(self):
        self.assertEqual(self.calc.divide(15,3),5)
        self.assertEqual(self.calc.divide(9,9),1)
        self.assertEqual(self.calc.divide(9,0),None)
