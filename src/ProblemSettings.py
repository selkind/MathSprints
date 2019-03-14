class ProblemSettings:
    def __init__(self):
        self.variable_term_count = False
        self.term_count_min = None
        self.term_count_max = None

        # supported terms integer, fraction
        self.int_value_manual = False
        self.int_values = []

        self.numerator_value_manual = False
        self.numerator_values = []

        self.denominator_value_manual = False
        self.denominator_values = []

        self.decimal_value_manual = False
        self.decimal_values = []

        # supported operators +, -, *, /
        self.mixed_operators = False
        self.operator_sets = []

        self.allow_mixed_terms = False
        self.term_sets = []
