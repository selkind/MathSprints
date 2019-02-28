from PyQt5 import QtGui, QtWidgets, QtCore
import sys


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)
        self.setWindowTitle(self.tr("test rendering"))
        self.texttest = QtWidgets.QLabel("FISHY")
        self.layout.addWidget(self.texttest)
        self.setMinimumSize(800,800)

    def print_screen(self, widget):
        filename = "test.pdf"
        printer = QtGui.QPdfWriter(filename)
        printer.setPageSize(QtGui.QPdfWriter.Letter)
        painter = QtGui.QPainter(printer)
        painter.scale(10, 10)
        widget.render(painter)
        painter.end()


def run():
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    window.print_screen(window.texttest)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
