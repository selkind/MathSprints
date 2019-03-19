from PyQt5 import QtWidgets


class ProblemSetManagementControls(QtWidgets.QFrame):
    def __init__(self, worksheet):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.worksheet = worksheet
        self.set_list = None
        self.create_set_list()
        self.set_name = None
        self.create_set_name()

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

        self.layout.addWidget(self.set_list, 0, 0)

    def create_set_name(self):
        self.set_name = QtWidgets.QLineEdit()

        size = QtWidgets.QSizePolicy()
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)

        self.set_name.setSizePolicy(size)
        self.layout.addWidget(self.set_name, 1, 0)

    def load_selected_set(self):
        selected_set = self.set_list.selectedItems()[0]
        self.set_name.setText(selected_set.text())
