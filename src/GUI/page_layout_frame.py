from PyQt5 import QtGui, QtWidgets


class PageLayout(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.group = QtWidgets.QGroupBox()
