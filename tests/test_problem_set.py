import unittest
from src.problem_settings import ProblemSettings
from src.problem_set import ProblemSet


class ProblemSetTest(unittest.TestCase):
    def setUp(self):
        settings = ProblemSettings()
        self.ps = ProblemSet(settings, "test_set")
        self.ps.problem_count = 5

    def test_choose_rand_term_single_set_single_term(self):
        test_terms = ['Integer']
        self.assertEqual("Integer", self.ps.choose_rand_term(test_terms))

    def test_choose_rand_op_single_set_single_op(self):
        test_ops = ["+"]
        self.assertEqual("+", self.ps.choose_rand_operator(test_ops))
