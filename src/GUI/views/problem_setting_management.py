from PyQt5 import QtWidgets


class ProblemSettingManagement(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.test_term_list = ["Integer", "Fraction", "Decimal"]
        self.test_op_list = ["+", "-", "X", "/"]

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

        self.term_count()
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

    def term_type(self):
        self.multiple_term_type_option = QtWidgets.QCheckBox("Multiple Term Types")
        self.multiple_term_type_option.setCheckable(True)

        self.layout.addWidget(self.multiple_term_type_option, 4, 0)
        self.term_check = self.list_check(self.test_term_list)
        self.term_radio = self.list_radio(self.test_term_list)
        self.layout.addWidget(self.term_check, 5, 0)
        self.layout.addWidget(self.term_radio, 5, 0)

    def op_type(self):
        self.multiple_op_option = QtWidgets.QCheckBox("Multiple Operators")
        self.multiple_op_option.setCheckable(True)

        self.layout.addWidget(self.multiple_op_option, 4, 1)
        self.op_check = self.list_check(self.test_op_list)
        self.op_radio = self.list_radio(self.test_op_list)
        self.layout.addWidget(self.op_check, 5, 1)
        self.layout.addWidget(self.op_radio, 5, 1)

    def list_radio(self, vals):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        for i in vals:
            layout.addWidget(QtWidgets.QRadioButton(i))

        return frame

    def list_check(self, vals):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        for i in vals:
            layout.addWidget(QtWidgets.QCheckBox(i))

        return frame

    def get_term_radios(self):
        r = []
        for i in self.term_radio.children():
            if type(i) == QtWidgets.QRadioButton:
                r.append(i)
        return r

    def get_term_checks(self):
        c = []
        for i in self.term_check.children():
            if type(i) == QtWidgets.QCheckBox:
                c.append(i)
        return c

    def get_op_radios(self):
        r = []
        for i in self.op_radio.children():
            if type(i) == QtWidgets.QRadioButton:
                r.append(i)
        return r

    def get_op_checks(self):
        c = []
        for i in self.op_check.children():
            if type(i) == QtWidgets.QCheckBox:
                c.append(i)
        return c
