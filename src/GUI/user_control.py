from PyQt5 import QtGui, QtWidgets


class UserControl(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.page_layout_input(), 0, 0)

    def page_layout_input(self):
        frame = QtWidgets.QFrame()
        layout = QtWidgets.QGridLayout(frame)

        size_label = QtWidgets.QLabel("Select Page Size")
        layout.addWidget(size_label, 0, 0, 1, 3)
        layout.addWidget(self.create_page_size_menu(), 1, 0, 1, 3)

        margin_label = QtWidgets.QLabel("Margin Size:")
        margin_input = QtWidgets.QLineEdit("51")
        margin_unit = QtWidgets.QLabel("Pixels")

        layout.addWidget(margin_label, 2, 0)
        layout.addWidget(margin_input, 2, 1)
        layout.addWidget(margin_unit, 2, 2)

        font_label = QtWidgets.QLabel("Font Size:")
        font_input = QtWidgets.QLineEdit("8")
        font_unit = QtWidgets.QLabel("pt")

        layout.addWidget(font_label, 3, 0)
        layout.addWidget(font_input, 3, 1)
        layout.addWidget(font_unit, 3, 2)

        return frame

    def create_page_size_menu(self):
        page_sizes = {}
        for key in dir(QtGui.QPageSize):
            value = getattr(QtGui.QPageSize, key)
            if isinstance(value, int):
                page_sizes[key] = value

        page_size_menu = QtWidgets.QComboBox()

        page_size_menu.addItems(page_sizes.keys())
        page_size_menu.setCurrentText("Letter")
        return page_size_menu

