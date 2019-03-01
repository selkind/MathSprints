from PyQt5 import QtGui, QtWidgets, QtCore, QtQuick
import sys


'''Probably going to have to have two painters. One to render the worksheet dynamically
    then another to pass the printer to when creating a pdf.'''


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setWindowTitle(self.tr("test rendering"))
        self.layout.addWidget(self.page_layout())
        self.setLayout(self.layout)

    def page_layout(self):
        top_widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(top_widget)
        label = self.config_problem_label()
        layout.addWidget(label, 0, 1)
        top_widget.setFixedSize(850, 1100)
        return top_widget

    def config_problem_label(self):
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(10, 100, 10))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        problem = QtWidgets.QLabel("Problem 1")
        problem.setAutoFillBackground(True)
        problem.setPalette(pal)
        problem.setFont(font)
        return problem

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
    #window.print_screen(window.texttest)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
