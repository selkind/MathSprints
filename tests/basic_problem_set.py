from src.ProblemSet import *

settings = ProblemSettings()
settings.term_count_min = 2
settings.term_count_max = 4
settings.allowed_terms["fraction"] = True
settings.numerator_values.append(1)
settings.numerator_values.append(2)
settings.denominator_value_manual = True
settings.denominator_values.append(11)
settings.denominator_values.append(12)
settings.denominator_values.append(13)

settings.allowed_operators["*"] = True
settings.operator_sets.append(["*"])
settings.term_sets.append(["fraction"])

prob_set = ProblemSet(settings)
problem_count = 5
for i in range(problem_count):
    prob_set.make_problem(settings.term_sets[0], settings.operator_sets[0])

for i in range(problem_count):
    print(prob_set.problems[i])
