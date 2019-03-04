from PyQt5 import QtWidgets


class Page(QtWidgets.QWidget):
    def __init__(self, width, height):
        QtWidgets.QWidget.__init__(self)
        self.available_width = width
        self.available_height = height
        self.layout = QtWidgets.QVBoxLayout()
