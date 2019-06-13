class ProblemSettings:
    def __init__(self):
        self.variable_term_count = False
        self.term_count_min = 2
        self.term_count_max = self.term_count_min

        '''
        draft of problem element data structure.
        
        self.problem_elements = \
        [
            {
            "terms":
                {
                    "Integer": [{"range": True, "vals": [0, 100]}, 
                                 {"range": False, "vals": [-1, -2, -5]}], 
                    "Fraction": {"Numerator": {"Integer": {"range": True, "vals": [-3, 10]}, 
                                "Denominator": {"Integer": {"range": True, "vals": [-3, 10]}}}}
                    "Decimal": {"precision": 3, "vals": [0, 100]}
                },
            "operators": ["+", "-"]
            },
            {
            "terms":
                {
                    "Integer": {"range": True, "vals": [100, 200]}
                },
            "operators": ["/", "*"]
            }
        ]
        
        **Notes:
            Numerators and denominators will initially only support Integer values, but can be expanded to be
            recursive fractions (to a limited depth) and have Decimal values.
            
            Decimal values will eventually need to support ranges and discrete options for precision. 
            Also a good idea to support integer-like user controlled selection/limitation of decimal values. 
        '''
        # supported terms integer, fraction
        self.problem_elements = [
            {"terms":
                 {
                     "Integer": [{"range": True, "vals": [0, 100]}]
                 },
             "operators": ["+"]
            },
            {"terms":
                 {
                     "Fraction": {
                         "Numerator": {"Integer": [{"range": False, "vals": [0, 5, 10]}]},
                         "Denominator": {"Integer": [{"range": True, "vals": [-30, -20]}]}
                     }
                 },
             "operators": ["-"]
             },
            {"terms":
                 {
                     "Decimal": [{"precision": 3, "range": True, "vals": [-4, -1]}]
                 },
             "operators": ["X"]
             }
        ]
