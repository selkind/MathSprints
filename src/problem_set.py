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
        self.term_map = {"Integer": lambda x: self.make_integer(x),
                         "Fraction": lambda x: self.make_fraction(x),
                         "Decimal": lambda x: self.make_decimal(x)}

    def build_set(self):
        self.problems = []
        for i in range(self.problem_count):
            self.make_problem()

    def make_problem(self):
        term_count = 0
        if self.settings.variable_term_count:
            term_count = randrange(self.settings.term_count_min, self.settings.term_count_max)
        else:
            term_count = self.settings.term_count_min

        prob = Problem(term_count)
        element_group = choice(self.settings.problem_elements)
        for i in range(term_count):
            term = self.make_term(element_group["terms"])
            prob.terms.append(term)
            if i != term_count - 1:
                operator = self.choose_operator(element_group["operators"])
                prob.operators.append(operator)
        self.problems.append(prob)

    def make_term(self, terms):
        term_type = self.get_term_type(terms)
        return self.term_map[term_type](terms[term_type])

    def get_term_type(self, type_dict):
        return choice(list(type_dict.keys()))

    def choose_rand(self, term_set):
        if type(term_set) == str:
            return term_set
        return self.choose_rand(choice(term_set))

    def choose_operator(self, operators):
        return self.choose_rand(operators)

    def make_integer(self, int_settings):
        chosen_set = choice(int_settings)
        if chosen_set["range"]:
            return randrange(chosen_set["vals"][0], chosen_set["vals"][1] + 1)
        else:
            return choice(chosen_set["vals"])

    def make_fraction(self, frac_settings):
        numerator = self.make_term(frac_settings["Numerator"])
        denominator = self.make_term(frac_settings["Denominator"])

        return Fraction(numerator, denominator)

    def make_decimal(self, dec_settings):
        chosen_set = choice(dec_settings)

        adjustment = chosen_set["precision"]
        low = chosen_set["vals"][0] * (10 ** (adjustment))
        high = chosen_set["vals"][1] * (10 ** (adjustment))

        return randrange(low, high) / (10 ** adjustment)

    def get_largest_problem(self):
        return max(self.problems, key=lambda item: len(item.__str__()))

