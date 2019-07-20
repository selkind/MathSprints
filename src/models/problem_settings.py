class ProblemSettings:
    def __init__(self):
        self.variable_term_count = False
        self.term_count_min = 3
        self.term_count_max = self.term_count_min
        self.ordered = True

        # supported terms integer, fraction

        self.ordered_terms = [
            [
                {
                    "Integer": [{"range": True, "vals": [0, 100]}],
                    "Decimal": [{"precision": 3, "range": True, "vals": [-4, -1]}]
                },
                {
                    "Fraction": {
                        "Numerator": {"Integer": [{"range": False, "vals": [0, 5, 10]}]},
                        "Denominator": {"Integer": [{"range": True, "vals": [-30, -20]}]}
                         }
                }
            ],
            [
                {
                     "Integer": [{"range": True, "vals": [0, 100]}]
                 }
            ],
            [
                {
                     "Decimal": [{"precision": 3, "range": True, "vals": [-4, -1]}]
                 }
            ]

        ]
        self.ordered_operators = [[["+"], ["-"]], [["*"]]]

    def __str__(self):
        return "PROBLEM_SETTINGS\n" \
                "var term count: {}\n" \
                "min term: {}\n" \
                "max term: {}\n" \
                "terms: {}\n" \
                "operators: {}\n".format(self.variable_term_count, self.term_count_min, self.term_count_max,
                                         self.ordered_terms, self.ordered_operators)
