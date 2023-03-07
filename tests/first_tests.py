from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiple_calc_passed(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_add_calc_passed(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_division_calc_passed(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction_calc_passed(self):
        assert self.calc.subtraction(self, 4, 2) == 2
