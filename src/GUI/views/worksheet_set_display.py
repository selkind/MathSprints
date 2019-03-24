from PyQt5 import QtWidgets, QtGui


class WorksheetSetDisplay(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.set_list = None
        self.set_name = None
        self.update_button = None
        self.add_button = None
        self.del_button = None
        self.up_button = None
        self.down_button = None
        self.create_set_name()
        self.create_set_list()
        self.create_update_button()
        self.create_list_mod_buttons()
        self.create_shift_buttons()

    def create_set_list(self):
        self.set_list = QtWidgets.QListWidget()
        self.set_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        size = QtWidgets.QSizePolicy()
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Minimum)
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)
        self.set_list.setSizePolicy(size)

        for i in self.worksheet.problem_sets:
            QtWidgets.QListWidgetItem(i.name, self.set_list)

        self.set_list.setCurrentRow(self.set_list.count() - 1)

        self.layout.addWidget(self.set_list, 0, 1)

    def add_item_to_set_list(self, name):
        QtWidgets.QListWidgetItem(name, self.set_list)

    def create_set_name(self):
        self.set_name = QtWidgets.QLineEdit()

        self.layout.addWidget(self.set_name, 1, 1)

    def create_update_button(self):
        self.update_button = QtWidgets.QPushButton("Update Problem Set")
        self.layout.addWidget(self.update_button, 1, 2)

    def create_list_mod_buttons(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        label = QtWidgets.QLabel("Problem Set")
        self.add_button = QtWidgets.QPushButton("+")
        self.del_button = QtWidgets.QPushButton("-")

        size = QtWidgets.QSizePolicy()
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
        self.add_button.setSizePolicy(size)
        self.del_button.setSizePolicy(size)
        label.setSizePolicy(size)

        layout.addWidget(self.add_button)
        layout.addWidget(label)
        layout.addWidget(self.del_button)

        self.layout.addWidget(frame, 0, 0)

    def create_shift_buttons(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        label = QtWidgets.QLabel("Shift Selected")
        arrow_font = QtGui.QFont()
        arrow_font.setPointSize(12)
        self.up_button = QtWidgets.QPushButton('\u02C4')
        self.down_button = QtWidgets.QPushButton('\u02C5')
        self.up_button.setFont(arrow_font)
        self.down_button.setFont(arrow_font)

        size = QtWidgets.QSizePolicy()
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
        self.up_button.setSizePolicy(size)
        self.down_button.setSizePolicy(size)
        label.setSizePolicy(size)

        layout.addWidget(self.up_button)
        layout.addWidget(label)
        layout.addWidget(self.down_button)

        self.layout.addWidget(frame, 0, 2)
