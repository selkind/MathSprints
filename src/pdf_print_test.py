from PyQt5 import QtGui, QtWidgets, QtCore, QtQuick
import sys
from tests.basic_problem_set import TestSet


'''Probably going to have to have two painters. One to render the worksheet dynamically
    then another to pass the printer to when creating a pdf.'''


class Window(QtWidgets.QDesktopWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setWindowTitle(self.tr("test rendering"))
        self.layout.addWidget(self.page_layout())
        self.setLayout(self.layout)

    def page_layout(self):
        page_widget = QtWidgets.QWidget()
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(10, 100, 10))
        page_widget.setAutoFillBackground(True)
        page_widget.setPalette(pal)
        layout = QtWidgets.QGridLayout(page_widget)
        label = self.problem_label(self.config_test_problem())
        layout.addWidget(label, 0, 1)
        page_widget.setFixedSize(850, 1100)
        return page_widget

    def problem_label(self, problem):
        font = QtGui.QFont()
        font.setPointSize(12)
        problem = QtWidgets.QLabel(problem.__str__())
        problem.setFont(font)
        return problem

    def config_test_problem(self):
        test_set = TestSet(1)
        return test_set.prob_set.problems[0]

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
    #geom = window.availableGeometry()
    #print(geom)
    window.show()
    #window.print_screen(window)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
