from PyQt5 import QtWidgets, QtGui


class ProblemSetManagement(QtWidgets.QFrame):
    def __init__(self, worksheet):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.worksheet = worksheet
        self.set_list = None
        self.set_name = None
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

        self.set_list.itemSelectionChanged.connect(lambda: self.load_selected_set())
        self.set_list.setCurrentRow(self.set_list.count() - 1)

        self.layout.addWidget(self.set_list, 0, 1)

    def create_set_name(self):
        self.set_name = QtWidgets.QLineEdit()

        self.layout.addWidget(self.set_name, 1, 1)

    def create_update_button(self):
        update_button = QtWidgets.QPushButton("Update Problem Set")
        self.layout.addWidget(update_button, 1, 2)

    def create_list_mod_buttons(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        label = QtWidgets.QLabel("Problem Set")
        add_but = QtWidgets.QPushButton("+")
        del_but = QtWidgets.QPushButton("-")

        size = QtWidgets.QSizePolicy()
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
        add_but.setSizePolicy(size)
        del_but.setSizePolicy(size)
        label.setSizePolicy(size)

        layout.addWidget(add_but)
        layout.addWidget(label)
        layout.addWidget(del_but)

        self.layout.addWidget(frame, 0, 0)

    def create_shift_buttons(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        label = QtWidgets.QLabel("Shift Selected")
        arrow_font = QtGui.QFont()
        arrow_font.setPointSize(12)
        up_but = QtWidgets.QPushButton('\u02C4')
        down_but = QtWidgets.QPushButton('\u02C5')
        up_but.setFont(arrow_font)
        down_but.setFont(arrow_font)

        size = QtWidgets.QSizePolicy()
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
        up_but.setSizePolicy(size)
        down_but.setSizePolicy(size)
        label.setSizePolicy(size)

        layout.addWidget(up_but)
        layout.addWidget(label)
        layout.addWidget(down_but)

        self.layout.addWidget(frame, 0, 2)

    def load_selected_set(self):
        selected_set = self.set_list.selectedItems()[0]
        self.set_name.setText(selected_set.text())
