import unittest
from src.models.problem_settings import ProblemSettings
from src.models.problem_set import ProblemSet


class ProblemSetTest(unittest.TestCase):
    def setUp(self):
        settings = ProblemSettings()
        self.ps = ProblemSet(settings, "test_set")
        self.ps.problem_count = 5

    def test_choose_rand_single_set_single_term(self):
        test_terms = [['Integer']]
        result = self.ps.choose_rand(test_terms)
        self.assertEqual("Integer", result)

    def test_choose_rand_single_set_multi_term(self):
        test_terms = [["Integer", "Decimal", "Fraction"]]
        supported_terms = self.ps.term_map.keys()
        result = self.ps.choose_rand(test_terms) in supported_terms

        self.assertTrue(result)

    def test_choose_rand_multi_set_single_term(self):
        test_terms = [["Integer"], ["Decimal"], ["Fraction"]]
        supported_terms = self.ps.term_map.keys()
        result = self.ps.choose_rand(test_terms) in supported_terms

        self.assertTrue(result)

    def test_choose_rand_multi_set_multi_term(self):
        test_terms = [["Integer", "Decimal"], ["Decimal"], ["Fraction", "Integer"]]
        supported_terms = self.ps.term_map.keys()
        result = self.ps.choose_rand(test_terms) in supported_terms

        self.assertTrue(result)
