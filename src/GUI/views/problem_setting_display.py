from PyQt5 import QtWidgets, QtCore


class ProblemSettingDisplay(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.test_term_list = ["Integer", "Fraction", "Decimal"]
        self.test_op_list = ["+", "-", "X", "/"]

        self.problem_elements = None

        self.term_count_label_min = None
        self.term_count_label_max = None
        self.variable_term_count = None
        self.term_count_min = None
        self.term_count_max = None

        self.multiple_term_type_option = None
        self.term_check = None
        self.term_radio = None

        self.multiple_op_option = None
        self.op_check = None
        self.op_radio = None

        self.prob_element_layout = None
        self.prob_element_widget = None

        self.config_problem_element_frame()
        self.term_count()
        self.create_problem_elements()
        self.term_type()
        self.op_type()

    def term_count(self):
        self.variable_term_count = QtWidgets.QCheckBox("Variable Number of Terms")
        self.variable_term_count.setCheckable(True)
        self.layout.addWidget(self.variable_term_count, 0, 0, 1, 2)

        term_count_label = QtWidgets.QLabel("Terms per Problem")
        self.term_count_label_min = QtWidgets.QLabel("Minimum")
        self.term_count_label_max = QtWidgets.QLabel("Maximum")
        self.layout.addWidget(term_count_label, 1, 0, 1, 2)
        self.layout.addWidget(self.term_count_label_min, 2, 1)
        self.layout.addWidget(self.term_count_label_max, 3, 1)

        self.term_count_min = QtWidgets.QSpinBox()
        self.term_count_max = QtWidgets.QSpinBox()
        self.layout.addWidget(self.term_count_min, 2, 0)
        self.layout.addWidget(self.term_count_max, 3, 0)

    def config_problem_element_frame(self):
        self.prob_element_layout = QtWidgets.QGridLayout()
        self.prob_element_widget = QtWidgets.QWidget()
        self.prob_element_widget.setLayout(self.prob_element_layout)
        self.layout.addWidget(self.prob_element_widget, 4, 0)

    def create_problem_elements(self):
        self.problem_elements = QtWidgets.QListWidget()
        self.problem_elements.setSelectionMode(QtWidgets.QListWidget.SingleSelection)

        size = QtWidgets.QSizePolicy()
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Minimum)
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)

        self.problem_elements.setSizePolicy(size)

        self.prob_element_layout.addWidget(self.problem_elements, 1, 0, 1, 2)
        self.prob_element_layout.addWidget(self.integer_selection([0, 1, 2, 3, 4]), 4, 0)

    def term_type(self):
        self.term_check = self.list_check(self.test_term_list)
        self.prob_element_layout.addWidget(self.term_check, 3, 0)

    def integer_selection(self, vals=[]):
        minimum = min(vals)
        maximum = max(vals)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(widget)

        min_val = QtWidgets.QSpinBox()
        min_val.setValue(minimum)
        layout.addWidget(min_val, 0, 0)
        min_label = QtWidgets.QLabel("Min")
        layout.addWidget(min_label, 0, 1)

        max_val = QtWidgets.QSpinBox()
        max_val.setValue(maximum)
        layout.addWidget(max_val, 0, 2)
        max_label = QtWidgets.QLabel("Max")
        layout.addWidget(max_label, 0, 3)

        int_list = QtWidgets.QListWidget()
        int_list.setSelectionMode(QtWidgets.QListWidget.SingleSelection)

        for i in range(minimum, maximum + 1):
            val = QtWidgets.QListWidgetItem(str(i))
            if i in vals:
                val.setCheckState(QtCore.Qt.Checked)
            int_list.addItem(val)
        layout.addWidget(int_list, 1, 0, 1, 2)
        return widget


    def op_type(self):
        self.op_check = self.list_check(self.test_op_list)
        self.prob_element_layout.addWidget(self.op_check, 2, 0)

    def list_check(self, vals):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QGridLayout(frame)
        for i in range(len(vals)):
            layout.addWidget(QtWidgets.QCheckBox(vals[i]), 0, i)

        return frame

    def get_term_checks(self):
        return [i for i in self.term_check.children() if isinstance(i, QtWidgets.QCheckBox)]

    def get_op_checks(self):
        return [i for i in self.op_check.children() if isinstance(i, QtWidgets.QCheckBox)]
