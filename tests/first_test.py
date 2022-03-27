# import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division(self):
        assert self.calc.division(self, 6, 3) == 2.0

    def test_subtraction(self):
        assert self.calc.subtraction(self, 6, 3) == 3

    def test_adding(self):
        assert self.calc.adding(self, 6, 3) == 9
