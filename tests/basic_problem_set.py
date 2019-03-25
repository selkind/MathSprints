from src.problem_set import *


class BasicProblemSet:
    def __init__(self, problem_count, name):
        name = name
        settings = ProblemSettings()

        self.prob_set = ProblemSet(settings, name)
        for i in range(problem_count):
            self.prob_set.make_problem(settings.term_sets[0], settings.operator_sets[0])
