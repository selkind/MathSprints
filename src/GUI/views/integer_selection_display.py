from PyQt5 import QtWidgets


class IntegerSelectionDisplay(QtWidgets.QWidget):
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
        self.layout.addWidget(self.min_val, 0, 0)

        min_label = QtWidgets.QLabel("Min")
        self.layout.addWidget(min_label, 0, 1)

    def config_max_val(self):
        self.max_val = QtWidgets.QSpinBox()
        self.layout.addWidget(self.max_val, 0, 2)

        max_label = QtWidgets.QLabel("Max")
        self.layout.addWidget(max_label, 0, 3)

    def config_int_list(self):
        self.int_list = QtWidgets.QListWidget()
        self.int_list.setSelectionMode(QtWidgets.QListWidget.SingleSelection)

        self.layout.addWidget(self.int_list, 1, 0, 1, 4)
