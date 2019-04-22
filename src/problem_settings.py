class ProblemSettings:
    def __init__(self):
        self.variable_term_count = False
        self.term_count_min = 2
        self.term_count_max = self.term_count_min

        '''
        draft of problem element data structure.
        [
            [{"Integer": {"range": True, "vals": [0, 100]}, 
            "Integer": {"range": False, "vals": [-1, 2, 5]},
            "Fraction": {"Numerator": ["Integer": {"range": True, "vals": [-3, 10]}], 
                        "Denominator": ["Integer": {"range": True, "vals": [-3, 10]}, ]}
            }],
            [{"Decimal": {"precision": 3, "vals": [0, 100]}
            }]
        ]
        
        **Notes:
            Numerators and denominators will initially only support Integer values, but can be expanded to be
            recursive fractions (to a limited depth) and have Decimal values.
            
            Decimal values will eventually need to support ranges and discrete options for precision. 
            Also a good idea to support integer-like user controlled selection/limitation of decimal values. 
        '''
        # supported terms integer, fraction
        self.int_values = [{"range": True, "vals": [0, 100]}]

        self.numerator_value_manual = False
        self.numerator_values = []

        self.denominator_value_manual = False
        self.denominator_values = []

        self.decimal_value_manual = False
        self.decimal_values = []

        # supported operators +, -, *, /
        self.operator_sets = [["+"]]

        self.term_sets = [["Integer"]]
