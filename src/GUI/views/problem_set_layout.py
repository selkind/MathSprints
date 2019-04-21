from PyQt5 import QtWidgets


class ProblemSetLayout(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.test_col_options = ["Auto", "1", "2", "3", "4"]

        answer_label = QtWidgets.QLabel("Set Answer Space Minimum Size:")
        self.layout.addWidget(answer_label, 0, 0, 1, 3)

        self.v_space = None
        self.h_space = None
        self.col_number = None
        self.page_prob_count = None
        self.point_val = None

        self.add_v_space()
        self.add_h_space()
        self.add_col_limiter()
        self.add_problem_limiter()
        self.add_point_val()

    def add_v_space(self):
        self.v_space = QtWidgets.QSpinBox()
        self.v_space.setMinimum(0)
        self.v_space.setMaximum(300)

        v_label = QtWidgets.QLabel("Vertical")
        v_unit = QtWidgets.QLabel("Pixels")

        self.layout.addWidget(v_label, 1, 0)
        self.layout.addWidget(self.v_space, 1, 1)
        self.layout.addWidget(v_unit, 1, 2)

    def add_h_space(self):
        self.h_space = QtWidgets.QSpinBox()
        self.h_space.setMinimum(0)
        self.h_space.setMaximum(300)

        h_label = QtWidgets.QLabel("Horizontal")
        h_unit = QtWidgets.QLabel("Pixels")

        self.layout.addWidget(h_label, 1, 3)
        self.layout.addWidget(self.h_space, 1, 4)
        self.layout.addWidget(h_unit, 1, 5)

    def add_col_limiter(self):
        col_label = QtWidgets.QLabel("Set Number of Columns:")
        self.col_number = QtWidgets.QComboBox()
        self.col_number.addItems(self.test_col_options)

        self.layout.addWidget(col_label, 2, 2)
        self.layout.addWidget(self.col_number, 2, 3)

    def add_problem_limiter(self):
        page_prob_count_label = QtWidgets.QLabel("Maximum Problems Per Page:")
        self.page_prob_count = QtWidgets.QSpinBox()
        self.page_prob_count.setMaximum(200)
        self.page_prob_count.setMinimum(1)

        self.layout.addWidget(page_prob_count_label, 2, 0)
        self.layout.addWidget(self.page_prob_count, 2, 1)

    def add_point_val(self):
        point_label = QtWidgets.QLabel("Points per Problem:")
        self.point_val = QtWidgets.QSpinBox()
        self.point_val.setMaximum(100)
        self.point_val.setMinimum(1)

        self.layout.addWidget(point_label, 3, 0)
        self.layout.addWidget(self.point_val, 3, 1)

