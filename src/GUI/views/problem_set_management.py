from PyQt5 import QtWidgets


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
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
        self.set_list.setSizePolicy(size)

        for i in self.worksheet.problem_sets:
            QtWidgets.QListWidgetItem(i.name, self.set_list)

        self.set_list.itemSelectionChanged.connect(lambda: self.load_selected_set())
        self.set_list.setCurrentRow(self.set_list.count() - 1)

        self.layout.addWidget(self.set_list, 0, 1)

    def create_set_name(self):
        self.set_name = QtWidgets.QLineEdit()

        size = QtWidgets.QSizePolicy()
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)

        self.set_name.setSizePolicy(size)
        self.layout.addWidget(self.set_name, 1, 1)

    def create_update_button(self):
        update_button = QtWidgets.QPushButton("Update Selected Problem Set")
        self.layout.addWidget(update_button, 1, 2)

    def create_list_mod_buttons(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        add_but = QtWidgets.QPushButton("Add A New Problem Set")
        del_but = QtWidgets.QPushButton("Delete Selected Problem Set")
        layout.addWidget(add_but)
        layout.addWidget(del_but)

        self.layout.addWidget(frame, 0, 0)

    def create_shift_buttons(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)
        up_but = QtWidgets.QPushButton("Shift Problem Set Up")
        down_but = QtWidgets.QPushButton("Shift Problem Set Down")
        layout.addWidget(up_but)
        layout.addWidget(down_but)

        self.layout.addWidget(frame, 0, 2)

    def load_selected_set(self):
        selected_set = self.set_list.selectedItems()[0]
        self.set_name.setText(selected_set.text())
