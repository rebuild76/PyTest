from app.calculator import Calculator
import pytest

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_division_calculator_correct(self):
        assert self.calc.division(self, 10, 2) == 5.0

    def test_multify_calculation_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_adding_calculator_correct(self):
        assert 100 + 100 == 200

    def test_subst_calculator_correct(self):
        assert 100 - 100 == 0


