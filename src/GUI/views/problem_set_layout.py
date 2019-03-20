from PyQt5 import QtWidgets


class ProblemSetLayout(QtWidgets.QFrame):
    def __init__(self, problem_set_page_settings):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.settings = problem_set_page_settings

        self.test_col_options = ["Auto", "1", "2", "3", "4"]

        answer_label = QtWidgets.QLabel("Set Answer Space Minimum Size:")
        self.layout.addWidget(answer_label, 0, 0, 3, 3)

        self.add_v_space()
        self.add_h_space()
        self.add_col_limiter()
        self.add_problem_limiter()
        self.add_point_val()

    def add_v_space(self):
        v_space = QtWidgets.QSpinBox()
        v_space.setMinimum(0)
        v_space.setMaximum(300)
        v_space.setValue(self.settings.v_answer_space)

        v_label = QtWidgets.QLabel("Vertical")
        v_unit = QtWidgets.QLabel("Pixels")

        self.layout.addWidget(v_label, 1, 0)
        self.layout.addWidget(v_space, 1, 1)
        self.layout.addWidget(v_unit, 1, 2)

    def add_h_space(self):
        h_space = QtWidgets.QSpinBox()
        h_space.setMinimum(0)
        h_space.setMaximum(300)
        h_space.setValue(self.settings.h_answer_space)

        h_label = QtWidgets.QLabel("Horizontal")
        h_unit = QtWidgets.QLabel("Pixels")

        self.layout.addWidget(h_label, 2, 0)
        self.layout.addWidget(h_space, 2, 1)
        self.layout.addWidget(h_unit, 2, 2)

    def add_col_limiter(self):
        col_label = QtWidgets.QLabel("Set Number of Columns:")
        col_number = QtWidgets.QComboBox()
        col_number.addItems(self.test_col_options)
        if self.settings.auto_columns:
            col_number.setCurrentText(self.test_col_options[0])
        else:
            col_number.setCurrentText(self.test_col_options[self.settings.columns])

        self.layout.addWidget(col_label, 3, 0)
        self.layout.addWidget(col_number, 3, 1)

    def add_problem_limiter(self):
        page_prob_count_label = QtWidgets.QLabel("Maximum Problems Per Page:")
        page_prob_count = QtWidgets.QSpinBox()
        page_prob_count.setMaximum(200)
        page_prob_count.setMinimum(1)
        page_prob_count.setValue(self.settings.max_problems_per_page)

        self.layout.addWidget(page_prob_count_label, 4, 0)
        self.layout.addWidget(page_prob_count, 4, 1)

    def add_point_val(self):
        point_label = QtWidgets.QLabel("Points per Problem:")
        point_val = QtWidgets.QSpinBox()
        point_val.setMaximum(100)
        point_val.setMinimum(1)
        point_val.setValue(self.settings.problem_value)

        self.layout.addWidget(point_label, 5, 0)
        self.layout.addWidget(point_val, 5, 1)

