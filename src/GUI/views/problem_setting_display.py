from PyQt5 import QtWidgets
from src.GUI.views.integer_selection_display import IntegerSelectionDisplay


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
        self.add_button = None
        self.del_button = None

        self.integer_option = None
        self.integer_selection = None

        self.fraction_option = None
        self.numerator_selection = None
        self.denominator_selection = None

        self.decimal_option = None
        self.decimal_selection = None

        self.config_problem_element_frame()
        self.term_count()
        self.create_list_mod_buttons()
        self.create_problem_elements()
        self.op_type()
        self.config_integer_selection()
        self.config_fraction_selection()
        self.config_decimal_selection()

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

        self.prob_element_layout.addWidget(self.problem_elements, 0, 1, 1, 2)

    def create_list_mod_buttons(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)

        self.add_button = QtWidgets.QPushButton("+")
        label = QtWidgets.QLabel("Problem Elements")
        self.del_button = QtWidgets.QPushButton("-")

        layout.addWidget(self.add_button)
        layout.addWidget(label)
        layout.addWidget(self.del_button)
        self.prob_element_layout.addWidget(frame, 0, 0)

    def add_problem_element_item(self, text):
        item = QtWidgets.QListWidgetItem(self.problem_elements)
        item.setText(text)

    def remove_selected_element_item(self, row):
        self.problem_elements.takeItem(row).deleteLater()


    def config_integer_selection(self):
        self.integer_option = QtWidgets.QCheckBox("Integer")
        self.prob_element_layout.addWidget(self.integer_option, 2, 0)

        self.integer_selection = IntegerSelectionDisplay()
        self.prob_element_layout.addWidget(self.integer_selection, 4, 0)

    def config_fraction_selection(self):
        self.fraction_option = QtWidgets.QCheckBox("Fraction")
        self.prob_element_layout.addWidget(self.fraction_option, 2, 1, 1, 2)

        numerator_label = QtWidgets.QLabel("Numerator Values")
        self.prob_element_layout.addWidget(numerator_label, 3, 1)
        self.numerator_selection = IntegerSelectionDisplay()
        self.prob_element_layout.addWidget(self.numerator_selection, 4, 1)

        denominator_label = QtWidgets.QLabel("Denominator Values")
        self.prob_element_layout.addWidget(denominator_label, 3, 2)
        self.denominator_selection = IntegerSelectionDisplay()
        self.prob_element_layout.addWidget(self.denominator_selection, 4, 2)

    def config_decimal_selection(self):
        self.decimal_option = QtWidgets.QCheckBox("Decimal")
        self.prob_element_layout.addWidget(self.decimal_option, 2, 3)

        self.decimal_selection = IntegerSelectionDisplay()
        self.prob_element_layout.addWidget(self.decimal_selection, 4, 3)

    def op_type(self):
        self.op_check = self.list_check(self.test_op_list)
        self.prob_element_layout.addWidget(self.op_check, 1, 0, 1, 3)

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
