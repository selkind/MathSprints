class ProblemSetPageSettings:
    def __init__(self):
        self.h_answer_space = 50
        self.v_answer_space = 100
        self.auto_columns = True
        self.columns = 1
        self.max_problems_per_page = 50
        self.problem_value = 1

    def __str__(self):
        return "PROBLEM LAYOUT\n" \
                "h_space: {}\n" \
                "v_space: {}\n" \
                "auto_columns: {}\n" \
                "columns: {}\n" \
                "max_problems: {}\n" \
                "problem_value: {}\n".format(self.h_answer_space, self.v_answer_space, self.auto_columns,
                                             self.columns, self.max_problems_per_page, self.problem_value)