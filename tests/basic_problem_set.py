from src.ProblemSet import *


class TestSet:
    def __init__(self, problem_count):
        settings = ProblemSettings()
        settings.term_count_min = 2
        settings.term_count_max = 5
        settings.numerator_values.append(1)
        settings.numerator_values.append(100)
        settings.denominator_value_manual = True
        settings.denominator_values.append(11)
        settings.denominator_values.append(12)
        settings.denominator_values.append(13)

        settings.allowed_operators["*"] = True
        settings.operator_sets.append(["+"])
        settings.term_sets.append(["fraction"])

        self.prob_set = ProblemSet(settings)
        for i in range(problem_count):
            self.prob_set.make_problem(settings.term_sets[0], settings.operator_sets[0])
