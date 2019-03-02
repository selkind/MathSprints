from PyQt5 import QtGui, QtWidgets, QtCore, QtQuick
import sys
from tests.basic_problem_set import TestSet


'''Probably going to have to have two painters. One to render the worksheet dynamically
    then another to pass the printer to when creating a pdf.'''


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setWindowTitle(self.tr("test rendering"))
        self.page = self.page_layout()
        self.layout.addWidget(self.page)
        self.setLayout(self.layout)

    def page_layout(self):
        page_widget = QtWidgets.QWidget()
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(10, 100, 10, 50))
        page_widget.setAutoFillBackground(True)
        page_widget.setPalette(pal)
        layout = QtWidgets.QGridLayout(page_widget)
        label = self.problem_label(self.config_test_problem())
        label2 = self.problem_label(self.config_test_problem())
        layout.addWidget(label2, 1, 1)
        print("label2 size: {}".format(label2.fontMetrics().boundingRect(label2.text())))
        layout.addWidget(label, 0, 1)
        page_size = self.size()
        page_width = page_size.height() * (17/22)
        page_widget.setFixedSize(page_width, page_size.height())
        print(page_size)
        return page_widget

    def problem_label(self, problem):
        #font = QtGui.QFont()
        #font.setPointSize(12)

        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(10, 10, 100, 50))

        problem = QtWidgets.QLabel(problem.__str__())
        problem.setAutoFillBackground(True)
        problem.setPalette(pal)
        #problem.setFont(font)

        #dimensions = problem.fontMetrics().boundingRect(problem.text())
        #problem.setFixedSize(dimensions.width(), dimensions.height())
        return problem

    def config_test_problem(self):
        test_set = TestSet(1)
        return test_set.prob_set.problems[0]

    def print_screen(self, widget):
        filename = "test.pdf"
        printer = QtGui.QPdfWriter(filename)
        printer.setPageSize(QtGui.QPdfWriter.Letter)
        printer.setPageMargins(QtCore.QMarginsF())

        logicaldpix = printer.logicalDpiX()
        pointsperinch = 40
        printer.pageSize()
        scaling = logicaldpix / pointsperinch

        painter = QtGui.QPainter(printer)
        painter.scale(scaling, scaling)
        widget.render(painter)
        painter.end()


def run():
    app = QtWidgets.QApplication([])

    window = Window()
    #geom = window.availableGeometry()
    #print(geom)
    window.show()
    window.print_screen(window.page)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
