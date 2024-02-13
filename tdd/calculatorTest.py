import unittest

import self

from PythonExercise import calculator


class MyCalculatorTest(unittest.TestCase):
    def test_that_calculator_can_add(self):
        result = calculator.addition(12, 13)
        self.assertEqual(25, result)


class MySubtractorTest(unittest.TestCase):
    def test_that_subtractor_can_subtract(self):
        result = calculator.subtraction(20, 15)
        self.assertEqual(5, result)


def test_that_divider_can_divide():
    result = calculator.divider(50,2)
    self.assertEqual(25,result)

def test_that_multiplication_can_multiply():
    result = calculator.multiplication(5,5)
    self.assertEqual(25,result)

