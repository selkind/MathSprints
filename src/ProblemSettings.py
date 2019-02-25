class ProblemSettings:
    def __init__(self):
        self.term_count_min = None
        self.term_count_max = None

        self.allowed_terms = {"integer": False, "decimal": False, "fraction": False}
        self.int_value_manual = False
        self.int_values = []
        self.numerator_value_manual = False
        self.numerator_values = []
        self.denominator_value_manual = False
        self.denominator_values = []
        self.decimal_value_manual = False
        self.decimal_values = []

        self.allowed_operators = {"+": False, "-": False, "*": False, "/": False}
        self.mixed_operators = False
        self.operator_sets = []

        self.allow_mixed_terms = False
        self.term_sets = []
