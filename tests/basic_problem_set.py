from src.models.problem_set import *


class BasicProblemSet:
    def __init__(self, problem_count, name):
        settings = ProblemSettings()

        self.prob_set = ProblemSet(settings, name)
        self.prob_set.problem_count = problem_count
        for i in range(problem_count):
            self.prob_set.make_problem()
