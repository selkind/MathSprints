from PyQt5 import QtWidgets, QtCore


class IntegerSelectionDisplay(QtWidgets.QWidget):
    MINIMUM = -100000
    MAXIMUM = 100000

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)
        self.min_val = None
        self.max_val = None
        self.int_list = None

        self.config_min_val()
        self.config_max_val()
        self.config_int_list()

    def config_min_val(self):
        self.min_val = QtWidgets.QSpinBox()
        self.min_val.setMinimum(self.MINIMUM)
        self.min_val.setMaximum(self.MAXIMUM)
        self.layout.addWidget(self.min_val, 0, 0)

        min_label = QtWidgets.QLabel("Min")
        self.layout.addWidget(min_label, 0, 1)

    def config_max_val(self):
        self.max_val = QtWidgets.QSpinBox()
        self.max_val.setMinimum(self.MINIMUM)
        self.max_val.setMaximum(self.MAXIMUM)
        self.layout.addWidget(self.max_val, 0, 2)

        max_label = QtWidgets.QLabel("Max")
        self.layout.addWidget(max_label, 0, 3)

    def config_int_list(self):
        self.int_list = QtWidgets.QListWidget()
        self.int_list.setSelectionMode(QtWidgets.QListWidget.SingleSelection)

        self.layout.addWidget(self.int_list, 1, 0, 1, 4)

    def populate_list(self, vals):
        checked_ptr = 0
        for i in range(vals[0], vals[-1] + 1):
            item = QtWidgets.QListWidgetItem(self.int_list)
            item.setText(str(i))
            if i == vals[checked_ptr]:
                item.setCheckState(QtCore.Qt.Checked)
                checked_ptr += 1
            else:
                item.setCheckState(QtCore.Qt.Unchecked)

    def clear_list(self):
        self.int_list.clear()
        self.min_val.setMaximum(self.MAXIMUM)
        self.min_val.setMinimum(self.MINIMUM)
        self.min_val.setValue(0)
        self.max_val.setMaximum(self.MAXIMUM)
        self.max_val.setMinimum(self.MINIMUM)
        self.max_val.setValue(0)
