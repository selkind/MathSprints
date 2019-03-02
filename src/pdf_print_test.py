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
        self.page = self.page_layout(self.make_test_set(50))
        self.layout.addWidget(self.page)
        self.setLayout(self.layout)

    def page_layout(self, problem_set):
        page_widget = QtWidgets.QWidget()
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(10, 100, 10, 50))
        page_widget.setAutoFillBackground(True)
        page_widget.setPalette(pal)

        page_size = self.size()
        page_width = page_size.height() * (17/22)
        page_widget.setFixedSize(page_width, page_size.height())

        layout = QtWidgets.QGridLayout(page_widget)

        available_page_width = page_width
        col_count = 3
        col = 0
        row = 0

        for i in problem_set.problems:
            problem_label = self.problem_label(i)
            test_font = QtGui.QFont()
            test_font.setPointSizeF(4)
            problem_label.setFont(test_font)

            problem_size = problem_label.fontMetrics().boundingRect(problem_label.text())
            #problem_label.setFixedWidth(problem_size.width())

            available_page_width -= problem_size.width()
            if available_page_width < 0:
                row += 1
                col = 0
                available_page_width = page_width

            print("problem_label size: {}".format(problem_label.fontMetrics().boundingRect(problem_label.text())))
            layout.addWidget(problem_label, row, col)
            col += 1
            if col == col_count:
                row += 1
                col = 0
                available_page_width = page_width

        return page_widget

    def problem_label(self, problem):
        font = QtGui.QFont()
        font.setPointSize(12)

        problem = QtWidgets.QLabel(problem.__str__())

        problem.setAlignment(QtCore.Qt.AlignLeft)

        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(10, 10, 100, 50))
        problem.setAutoFillBackground(True)
        problem.setPalette(pal)
        problem.setFont(font)

        return problem

    def answer_label(self):
        answer = QtWidgets.QLabel()
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(100, 10, 10, 50))
        answer.setAutoFillBackground(True)
        answer.setPalette(pal)
        return answer

    def make_test_set(self, problem_count):
        return TestSet(problem_count).prob_set

    def print_screen(self, widget):
        filename = "test.pdf"

        '''
        Potential to take string argument of page sizes and use a dictionary to map
        to Qpage sizes. then use that size as parameter during page size instantiation
        '''
        page_size = QtGui.QPageSize(QtGui.QPageSize.Letter)

        printer = QtGui.QPdfWriter(filename)
        printer.setPageSize(QtGui.QPdfWriter.Letter)
        printer.setPageMargins(QtCore.QMarginsF())
        page_resolution = printer.logicalDpiY()
        y_pixels_page = QtGui.QPageSize.sizePixels(page_size.id(), page_resolution).height()
        y_pixels_widget = widget.size().height()

        scaling = y_pixels_page / y_pixels_widget

        print("pixels: {}".format(y_pixels_page))

        print("widgetsize: {}".format(widget.size()))
        print("scaling: {}".format(scaling))

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
    #window.print_screen(window.page)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
