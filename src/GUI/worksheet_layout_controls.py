from PyQt5 import QtWidgets, QtGui


class WorksheetLayoutControls(QtWidgets.QFrame):
    def __init__(self, worksheet_layout_settings):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        self.settings = worksheet_layout_settings

        self.page_size()
        self.margins()
        self.font()

    def page_size(self):
        size_label = QtWidgets.QLabel("Select Page Size")
        self.layout.addWidget(size_label, 0, 0, 1, 3)
        self.layout.addWidget(self.create_page_size_menu(), 1, 0, 1, 3)

    def margins(self):
        margin_label = QtWidgets.QLabel("Margin Size:")
        margin_input = QtWidgets.QLineEdit(str(self.settings.margin_size))
        margin_unit = QtWidgets.QLabel(self.settings.margin_unit)

        self.layout.addWidget(margin_label, 2, 0)
        self.layout.addWidget(margin_input, 2, 1)
        self.layout.addWidget(margin_unit, 2, 2)

    def font(self):
        font_label = QtWidgets.QLabel("Font Size:")
        font_input = QtWidgets.QLineEdit(str(self.settings.font_size))
        font_unit = QtWidgets.QLabel("pt")

        self.layout.addWidget(font_label, 3, 0)
        self.layout.addWidget(font_input, 3, 1)
        self.layout.addWidget(font_unit, 3, 2)

    def create_page_size_menu(self):
        page_sizes = {}
        for key in dir(QtGui.QPageSize):
            value = getattr(QtGui.QPageSize, key)
            if isinstance(value, int):
                page_sizes[key] = value

        page_size_menu = QtWidgets.QComboBox()
        page_size_menu.addItems(page_sizes.keys())
        page_size_menu.setCurrentText(self.settings.page_size)

        return page_size_menu
