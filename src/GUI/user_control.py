from PyQt5 import QtGui, QtWidgets
from src.GUI.problem_set_layout_controls import ProblemSetLayoutControls
from src.GUI.ProblemSetPageSettings import ProblemSetPageSettings


class UserControl(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.test_term_list = ["Integer", "Fraction", "Decimal"]
        self.test_op_list = ["+", "-", "X", "/"]
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.page_layout_input(), 0, 0)
        self.layout.addWidget(self.problem_set_settings(), 1, 0)
        self.layout.addWidget(self.term_type_settings(), 2, 0)
        self.layout.addWidget(self.op_type_settings(), 2, 1)
        set_settings = ProblemSetPageSettings()
        self.layout.addWidget(ProblemSetLayoutControls(set_settings), 3, 0)

    def page_layout_input(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QGridLayout(frame)

        size_label = QtWidgets.QLabel("Select Page Size")
        layout.addWidget(size_label, 0, 0, 1, 3)
        layout.addWidget(self.create_page_size_menu(), 1, 0, 1, 3)

        margin_label = QtWidgets.QLabel("Margin Size:")
        margin_input = QtWidgets.QLineEdit("51")
        margin_unit = QtWidgets.QLabel("Pixels")

        layout.addWidget(margin_label, 2, 0)
        layout.addWidget(margin_input, 2, 1)
        layout.addWidget(margin_unit, 2, 2)

        font_label = QtWidgets.QLabel("Font Size:")
        font_input = QtWidgets.QLineEdit("8")
        font_unit = QtWidgets.QLabel("pt")

        layout.addWidget(font_label, 3, 0)
        layout.addWidget(font_input, 3, 1)
        layout.addWidget(font_unit, 3, 2)

        return frame

    def create_page_size_menu(self):
        page_sizes = {}
        for key in dir(QtGui.QPageSize):
            value = getattr(QtGui.QPageSize, key)
            if isinstance(value, int):
                page_sizes[key] = value

        page_size_menu = QtWidgets.QComboBox()

        page_size_menu.addItems(page_sizes.keys())
        page_size_menu.setCurrentText("Letter")
        return page_size_menu

    def problem_set_settings(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QGridLayout(frame)

        layout.addWidget(self.term_count_settings(), 0, 0)

        return frame

    def term_count_settings(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QGridLayout(frame)

        variable_term_count = QtWidgets.QCheckBox("Variable Number of Terms")
        variable_term_count.setCheckable(True)
        variable_term_count.setChecked(False)
        layout.addWidget(variable_term_count, 0, 0, 1, 2)

        term_count_label = QtWidgets.QLabel("Terms per Problem")
        term_count_label_min = QtWidgets.QLabel("Minimum")
        term_count_label_max = QtWidgets.QLabel("Maximum")
        layout.addWidget(term_count_label, 1, 0, 1, 2)
        layout.addWidget(term_count_label_min, 2, 0)
        layout.addWidget(term_count_label_max, 3, 0)

        term_count_min = QtWidgets.QSpinBox()
        term_count_max = QtWidgets.QSpinBox()
        term_count_min.setValue(2)
        term_count_min.setMinimum(2)
        term_count_max.setValue(term_count_min.value())
        term_count_max.setMinimum(term_count_min.value())

        layout.addWidget(term_count_min, 2, 1)
        layout.addWidget(term_count_max, 3, 1)

        return frame

    def term_type_settings(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)

        multiple_type_option = QtWidgets.QCheckBox("Multiple Term Types")
        multiple_type_option.setCheckable(True)
        multiple_type_option.setChecked(False)

        layout.addWidget(multiple_type_option)
        layout.addWidget(self.term_list_radio(self.test_term_list))

        return frame

    def term_list_radio(self, term_types):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        for i in term_types:
            layout.addWidget(QtWidgets.QRadioButton(i))

        return frame

    def term_list_check(self, term_types):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        for i in term_types:
            layout.addWidget(QtWidgets.QCheckBox(i))

        return frame

    def op_type_settings(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)

        multiple_op_option = QtWidgets.QCheckBox("Multiple Operators")
        multiple_op_option.setCheckable(True)
        multiple_op_option.setChecked(False)

        layout.addWidget(multiple_op_option)
        layout.addWidget(self.op_list_radio(self.test_op_list))

        return frame

    def op_list_radio(self, op_types):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        for i in op_types:
            layout.addWidget(QtWidgets.QRadioButton(i))

        return frame

    def op_list_check(self, op_types):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        for i in op_types:
            layout.addWidget(QtWidgets.QCheckBox(i))

        return frame
