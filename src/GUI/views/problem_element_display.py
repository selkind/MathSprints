from PyQt5 import QtWidgets
from src.GUI.views.integer_selection_display import IntegerSelectionDisplay


class ProblemElementDisplay(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.test_term_list = ["Integer", "Fraction", "Decimal"]
        self.test_op_list = ["+", "-", "*", "/"]

        self.op_check = None

        self.integer_option = None
        self.integer_selection = None

        self.fraction_option = None
        self.numerator_selection = None
        self.numerator_label = None
        self.denominator_selection = None
        self.denominator_label = None

        self.decimal_option = None
        self.decimal_selection = None

        self.element_save = None

        self.op_type()
        self.config_integer_selection()
        self.config_fraction_selection()
        self.config_decimal_selection()
        self.config_element_save()

    def config_integer_selection(self):
        self.integer_option = QtWidgets.QCheckBox("Integer")
        self.layout.addWidget(self.integer_option, 2, 0)

        self.integer_selection = IntegerSelectionDisplay()
        self.layout.addWidget(self.integer_selection, 4, 0)

    def config_fraction_selection(self):
        self.fraction_option = QtWidgets.QCheckBox("Fraction")
        self.layout.addWidget(self.fraction_option, 2, 1, 1, 2)

        self.numerator_label = QtWidgets.QLabel("Numerator Values")
        self.layout.addWidget(self.numerator_label, 3, 1)
        self.numerator_selection = IntegerSelectionDisplay()
        self.layout.addWidget(self.numerator_selection, 4, 1)

        self.denominator_label = QtWidgets.QLabel("Denominator Values")
        self.layout.addWidget(self.denominator_label, 3, 2)
        self.denominator_selection = IntegerSelectionDisplay()
        self.layout.addWidget(self.denominator_selection, 4, 2)

    def config_decimal_selection(self):
        self.decimal_option = QtWidgets.QCheckBox("Decimal")
        self.layout.addWidget(self.decimal_option, 2, 3)

        self.decimal_selection = IntegerSelectionDisplay()
        self.layout.addWidget(self.decimal_selection, 4, 3)

    def op_type(self):
        self.op_check = self.list_check(self.test_op_list)
        self.layout.addWidget(self.op_check, 1, 0, 1, 3)

    def config_element_save(self):
        self.element_save = QtWidgets.QPushButton("Save Changes")
        self.layout.addWidget(self.element_save, 5, 0)

    def list_check(self, vals):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QGridLayout(frame)
        for i in range(len(vals)):
            layout.addWidget(QtWidgets.QCheckBox(vals[i]), 0, i)

        return frame

    def get_op_checks(self):
        return [i for i in self.op_check.children() if isinstance(i, QtWidgets.QCheckBox)]

    def clear_op_checks(self):
        for i in self.get_op_checks():
            i.setChecked(False)
