

class Worksheet:
    def __init__(self):
        self.name = ""
        self.total_points = 0
        # Each item has the structure {"name": "name", "set": ProblemSet, "settings": ProblemSetPageSettings}
        self.problem_sets = []
