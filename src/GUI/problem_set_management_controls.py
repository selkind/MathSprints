from PyQt5 import QtWidgets


class ProblemSetManagementControls(QtWidgets.QFrame):
    def __init__(self, worksheet):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.worksheet = worksheet
        self.set_list()

    def set_list(self):
        set_list = QtWidgets.QListWidget()
        set_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        size = QtWidgets.QSizePolicy()
        size.setVerticalPolicy(QtWidgets.QSizePolicy.Maximum)
        size.setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
        set_list.setSizePolicy(size)

        for i in self.worksheet.problem_sets:
            QtWidgets.QListWidgetItem(i.name, set_list)

        self.layout.addWidget(set_list, 0, 0)
