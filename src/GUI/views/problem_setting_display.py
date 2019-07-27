from PyQt5 import QtWidgets, QtCore
from src.GUI.views.problem_element_display import ProblemElementDisplay


class ProblemSettingDisplay(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.test_term_list = ["Integer", "Fraction", "Decimal"]
        self.test_op_list = ["+", "-", "*", "/"]

        self.problem_elements = None

        self.ordered_term_check = None
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

        self.add_button = None
        self.del_button = None

        self.problem_element_selection = None

        self.config_ordered_term_check()
        self.term_count()
        self.create_problem_elements()
        self.create_list_mod_buttons()
        self.config_problem_element_selection()

    def term_count(self):
        self.variable_term_count = QtWidgets.QCheckBox("Variable Number of Terms")
        self.variable_term_count.setCheckable(True)
        self.layout.addWidget(self.variable_term_count, 1, 0)

        term_count_label = QtWidgets.QLabel("Terms per Problem")
        self.term_count_label_min = QtWidgets.QLabel("Minimum")
        self.term_count_label_max = QtWidgets.QLabel("Maximum")
        self.layout.addWidget(term_count_label, 2, 0, 1, 2)
        self.layout.addWidget(self.term_count_label_min, 3, 1)
        self.layout.addWidget(self.term_count_label_max, 4, 1)

        size = QtWidgets.QSizePolicy()
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
        self.term_count_min = QtWidgets.QSpinBox()
        self.term_count_min.setSizePolicy(size)
        self.term_count_max = QtWidgets.QSpinBox()
        self.term_count_min.setSizePolicy(size)

        self.layout.addWidget(self.term_count_min, 3, 0)
        self.layout.addWidget(self.term_count_max, 4, 0)

    def config_ordered_term_check(self):
        self.ordered_term_check = QtWidgets.QCheckBox("Assign Settings to Terms")
        self.ordered_term_check.setCheckable(True)
        self.layout.addWidget(self.ordered_term_check, 0, 0)

    def create_problem_elements(self):
        self.problem_elements = QtWidgets.QTreeWidget()
        self.problem_elements.setColumnCount(1)

        size = QtWidgets.QSizePolicy()
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Minimum)
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Minimum)

        self.problem_elements.setSizePolicy(size)

        self.layout.addWidget(self.problem_elements, 5, 1)

    def create_list_mod_buttons(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)

        size = QtWidgets.QSizePolicy()
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)

        frame.setSizePolicy(size)
        self.add_button = QtWidgets.QPushButton("+")
        label = QtWidgets.QLabel("Problem Elements")
        self.del_button = QtWidgets.QPushButton("-")

        layout.addWidget(self.add_button)
        layout.addWidget(label)
        layout.addWidget(self.del_button)
        self.layout.addWidget(frame, 5, 0, 1, 1)

    def add_problem_element_item(self, text):
        item = QtWidgets.QListWidgetItem(self.problem_elements)
        item.setText(text)

    def add_ordered_term_group(self, text):
        item = QtWidgets.QListWidgetItem(self.problem_elements)
        item.setText(text)

    def add_term_element_item(self, text):
        item = QtWidgets.QListWidgetItem(self.problem_elements)
        item.setText(text)

    def add_ordered_operator_group(self, text):
        item = QtWidgets.QListWidgetItem(self.problem_elements)
        item.setText(text)

    def add_operator_element_item(self, text):
        item = QtWidgets.QListWidgetItem(self.problem_elements)
        item.setText(text)

    def remove_selected_element_item(self, row):
        self.problem_elements.takeItem(row)

    def config_problem_element_selection(self):
        self.problem_element_selection = ProblemElementDisplay()
        self.layout.addWidget(self.problem_element_selection, 6, 0, 1, 2)
