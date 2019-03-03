from src.ProblemSettings import ProblemSettings
from src.Problem import Problem
from src.Fraction import Fraction
from random import randrange, choice, sample, random


class ProblemSet:
    def __init__(self, settings):
        self.settings = settings
        self.problem_count = 0
        self.problems = []

    def make_problem(self, term_set, operator_set):
        term_count = 0
        if self.settings.term_count_min == self.settings.term_count_max:
            term_count = self.settings.term_count_min
        else:
            term_count = randrange(self.settings.term_count_min, self.settings.term_count_max)
        prob = Problem(term_count)
        for i in range(term_count):
            term = self.make_term(term_set)
            prob.terms.append(term)
            if i != term_count - 1:
                operator = choice(operator_set)
                prob.operators.append(operator)
        self.problems.append(prob)

    def make_term(self, term_set):
        terms = {"integer": self.make_integer, "fraction": self.make_fraction, "decimal": self.make_decimal}
        return terms[choice(term_set)]()

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

