import math

class Calculator: 
  def add(self, a, b):
    return a+b
  def subtract(self, a, b):
    return a-b
  def squareRoot(self, a):
    return math.sqrt(a)
  def multiply(self,a, b):
    return a*b

import unittest

class CalculatorTests(unittest.TestCase):
  def setUp(self):
    self.calc = Calculator()
  
  def test_add(self):
    self.assertEqual(10, self.calc.add(7, 3), "Addition is wrong")

  def test_subtract(self):
    self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")

  def test_multiply(self):
    self.assertEqual(5, self.calc.multiply(5,1), "Multiplication is wrong")

  

if __name__ == '__main__':
    unittest.main()
