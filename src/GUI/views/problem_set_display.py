from PyQt5 import QtWidgets


class ProblemSetDisplay(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.set_name = None
        self.update_but = None
        self.problem_count = None
        self.create_set_name()
        self.create_update_button()
        self.create_problem_count()

    def create_set_name(self):
        self.set_name = QtWidgets.QLineEdit()
        self.layout.addWidget(self.set_name, 0, 0)

    def create_update_button(self):
        self.update_but = QtWidgets.QPushButton("Update Problem Set")
        self.layout.addWidget(self.update_but, 0, 1)

    def create_problem_count(self):
        problem_count_label = QtWidgets.QLabel("Number of Problems")
        self.layout.addWidget(problem_count_label, 1, 0)
        self.problem_count = QtWidgets.QSpinBox()
        self.layout.addWidget(self.problem_count, 1, 1)