from PyQt5 import QtWidgets


class SprintViewer(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.problem_sets = []
        self.problem_set_settings = []
