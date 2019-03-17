from PyQt5 import QtWidgets


class ProblemSettingControls(QtWidgets.QFrame):
    def __init__(self, problemsettings):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)
        self.settings = problemsettings

        self.test_term_list = ["Integer", "Fraction", "Decimal"]
        self.test_op_list = ["+", "-", "X", "/"]

        self.term_check = None
        self.term_radio = None

        self.op_check = None
        self.op_radio = None

        self.term_count()
        self.term_type()
        self.op_type()

    def term_count(self):
        variable_term_count = QtWidgets.QCheckBox("Variable Number of Terms")
        variable_term_count.setCheckable(True)
        variable_term_count.setChecked(self.settings.variable_term_count)
        self.layout.addWidget(variable_term_count, 0, 0, 1, 2)

        term_count_label = QtWidgets.QLabel("Terms per Problem")
        term_count_label_min = QtWidgets.QLabel("Minimum")
        term_count_label_max = QtWidgets.QLabel("Maximum")
        self.layout.addWidget(term_count_label, 1, 0, 1, 2)
        self.layout.addWidget(term_count_label_min, 2, 0)
        self.layout.addWidget(term_count_label_max, 3, 0)

        term_count_min = QtWidgets.QSpinBox()
        term_count_max = QtWidgets.QSpinBox()
        term_count_min.setValue(self.settings.term_count_min)
        term_count_min.setMinimum(2)
        term_count_max.setValue(self.settings.term_count_max)
        term_count_max.setMinimum(term_count_min.value())
        self.layout.addWidget(term_count_min, 2, 1)
        self.layout.addWidget(term_count_max, 3, 1)

    def term_type(self):
        multiple_type_option = QtWidgets.QCheckBox("Multiple Term Types")
        multiple_type_option.setCheckable(True)
        multi_term_types = len(self.settings.term_sets[0]) > 1 or len(self.settings.term_sets) > 1
        multiple_type_option.setChecked(multi_term_types)

        self.layout.addWidget(multiple_type_option, 4, 0)
        self.term_check = self.list_check(self.test_term_list, self.settings.term_sets)
        self.term_radio = self.list_radio(self.test_term_list, self.settings.term_sets[0])
        self.layout.addWidget(self.term_check, 5, 0)
        self.layout.addWidget(self.term_radio, 5, 0)

        if multi_term_types:
            self.term_radio.hide()
        else:
            self.term_check.hide()

    def op_type(self):
        multiple_op_option = QtWidgets.QCheckBox("Multiple Operators")
        multiple_op_option.setCheckable(True)
        multi_ops = len(self.settings.operator_sets[0]) > 1 or len(self.settings.operator_sets) > 1
        multiple_op_option.setChecked(multi_ops)

        self.layout.addWidget(multiple_op_option, 4, 1)
        self.op_check = self.list_check(self.test_op_list, self.settings.operator_sets)
        self.op_radio = self.list_radio(self.test_op_list, self.settings.operator_sets[0])
        self.layout.addWidget(self.op_check, 5, 1)
        self.layout.addWidget(self.op_radio, 5, 1)

        if multi_ops:
            self.op_radio.hide()
        else:
            self.op_check.hide()

    def list_radio(self, vals, selected_val):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        for i in vals:
            but = QtWidgets.QRadioButton(i)
            if i == selected_val[0]:
                but.setChecked(True)
            layout.addWidget(but)

        return frame

    def list_check(self, vals, selected_vals):
        checked = []
        for i in selected_vals:
            checked.append(i[0])
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)

        for i in vals:
            but = QtWidgets.QCheckBox(i)
            if i in checked:
                but.setChecked(True)
            layout.addWidget(but)

        return frame
