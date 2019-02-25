from src.ProblemSet import *

settings = ProblemSettings()
settings.term_count_min = 2
settings.term_count_max = 2
settings.allowed_terms["integer"] = True
settings.int_values.append(1)
settings.int_values.append(3)
settings.allowed_operators["+"] = True
settings.operator_sets.append(["+"])
settings.term_sets.append("integer")

prob_set = ProblemSet(settings)
problem_count = 5
for i in range(problem_count):
    prob_set.make_problem(settings.term_sets[0], settings.operator_sets[0])

for i in range(problem_count):
    print(prob_set.problems[i])
