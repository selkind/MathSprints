class Problem:
    def __init__(self, term_count):
        self.term_count = term_count
        self.terms = []
        self.operators = []
        self.answer = None

    def add_term(self, term):
        self.terms.append(term)

    def add_operator(self, op):
        self.operators.append(op)