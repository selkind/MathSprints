from src.problem_settings import ProblemSettings
from src.problem import Problem
from src.fraction import Fraction
from random import randrange, choice, sample, random


class ProblemSet:
    def __init__(self, settings, name):
        self.name = name
        self.settings = settings
        self.problem_count = 0
        self.problems = []

    def build_set(self):
        for i in range(self.problem_count):
            self.problems.append(self.make_problem())

    def make_problem(self):
        term_count = 0
        if self.settings.term_count_min == self.settings.term_count_max:
            term_count = self.settings.term_count_min
        else:
            term_count = randrange(self.settings.term_count_min, self.settings.term_count_max)
        prob = Problem(term_count)
        for i in range(term_count):
            term = self.make_term()
            prob.terms.append(term)
            if i != term_count - 1:
                operator = self.choose_operator()
                prob.operators.append(operator)
        self.problems.append(prob)

    def make_term(self):
        term_map = {"Integer": self.make_integer, "Fraction": self.make_fraction, "Decimal": self.make_decimal}
        term = self.choose_rand_term(self.settings.term_sets)
        return term_map[term]()

    def choose_rand_term(self, term_set):
        if type(term_set) != list:
            return term_set
        term = choice(term_set)
        self.choose_rand_term(term)

    def choose_operator(self):
        return self.choose_rand_operator(self.settings.operator_sets)

    def choose_rand_operator(self, operator_set):
        if type(operator_set) == str:
            return operator_set
        op = choice(operator_set)
        self.choose_rand_operator(op)

    def make_integer(self):
        if self.settings.int_value_manual:
            return choice(self.settings.int_values)
        else:
            return randrange(self.settings.int_values[0], self.settings.int_values[1] + 1)

    def make_fraction(self):
        numerator = None
        denominator = None

        if self.settings.numerator_value_manual:
            numerator = choice(self.settings.numerator_values)
        else:
            numerator = randrange(self.settings.numerator_values[0], self.settings.numerator_values[1] + 1)

        if self.settings.denominator_value_manual:
            denominator = choice(self.settings.denominator_values)
        else:
            if self.settings.denominator_values[0] > 0:
                denominator = randrange(self.settings.denominator_values[0], self.settings.denominator_values[1] + 1)
            else:
                neg = list(range(self.settings.denominator_values[0], 0))
                pos = list(range(1, self.settings.denominator_values[1] + 1))
                denominator = choice(neg + pos)

        return Fraction(numerator, denominator)

    def make_decimal(self):
        return 0

    def get_largest_problem(self):
        return max(self.problems, key=lambda item: len(item.__str__()))

