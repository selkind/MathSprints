class Problem:
    def __init__(self, term_count):
        self.term_count = term_count
        self.terms = []
        self.operators = []
        self.answer = None

    def __str__(self):
        problem = ""
        for i in range(self.term_count):
            if i != self.term_count - 1:
                problem += str(self.terms[i]) + " " + self.operators[i] + " "
            else:
                problem += str(self.terms[i]) + " = "
        return problem
