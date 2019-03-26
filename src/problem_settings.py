class ProblemSettings:
    def __init__(self):
        self.variable_term_count = False
        self.term_count_min = 2
        self.term_count_max = self.term_count_min

        # supported terms integer, fraction
        self.int_value_manual = False
        self.int_values = [0, 100]

        self.numerator_value_manual = False
        self.numerator_values = []

        self.denominator_value_manual = False
        self.denominator_values = []

        self.decimal_value_manual = False
        self.decimal_values = []

        # supported operators +, -, *, /
        self.operator_sets = [["+"]]

        self.term_sets = [["Integer"]]
