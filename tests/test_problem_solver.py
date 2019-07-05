import unittest
from src.models.problem_solver import ProblemSolver


class ProblemSolverTest(unittest.TestCase):
    def setUp(self):
        self.test_ob = ProblemSolver()

    def test_integer_addition_positive(self):
        test = "1+1"
        res = self.test_ob.solve_problem(test)
        self.assertEqual(2, res)

    def test_integer_addition_neg_and_pos(self):
        test = "-1+1"
        res = self.test_ob.solve_problem(test)
        self.assertEqual(0, res)

    def test_integer_addition_negative(self):
        test = "-1+-1"
        res = self.test_ob.solve_problem(test)
        self.assertEqual(-2, res)

    def test_integer_subtraction_positive(self):
        test = "1-1"
        res = self.test_ob.solve_problem(test)
        self.assertEqual(0, res)

    def test_integer_subtraction_pos_neg(self):
        test = "1--1"
        res = self.test_ob.solve_problem(test)
        self.assertEqual(2, res)

    def test_integer_subtraction_negative(self):
        test = "-1--1"
        res = self.test_ob.solve_problem(test)
        self.assertEqual(0, res)

    def test_fraction_addition(self):
        test = "1/3 + 1/3 + 1/3"
        res = self.test_ob.solve_problem(test)
        self.assertEqual(1, res)
