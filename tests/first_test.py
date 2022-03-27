# import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_correctly(self):
        assert self.calc.division(self, 6, 3) == 2.0

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 6, 3) == 3

    def test_adding_correctly(self):
        assert self.calc.adding(self, 6, 3) == 9
