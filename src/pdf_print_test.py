from PyQt5 import QtGui, QtWidgets, QtCore
import sys


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)
        self.setWindowTitle(self.tr("test rendering"))
        self.texttest = QtWidgets.QTextEdit()
        self.texttest.setText("FISHY FISHY FISHY")
        self.layout.addWidget(self.texttest)


def print_screen(widget):
    filename = "test.pdf"
    printer = QtGui.QPdfWriter(filename)
    printer.setPageSize(QtGui.QPdfWriter.Letter)
    painter = QtGui.QPainter(printer)
    widget.render(painter)
    painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    print_screen(window)
    sys.exit(app.exec_())
