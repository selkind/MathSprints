from src import problem_set, problem_settings

settings = problem_settings.ProblemSettings()
problem_set = problem_set.ProblemSet(settings, "test")
problem_set.problem_count = 5
test_terms = ['Integer']
op_test = '+'
print(problem_set.choose_rand_term(test_terms))
print(problem_set.choose_rand_operator(op_test))