from PyQt5 import QtGui, QtWidgets, QtCore
import sys
from tests.basic_problem_set import TestSet
from src.GUI.ProblemSetPageSettings import ProblemSetPageSettings


'''Probably going to have to have two painters. One to render the worksheet dynamically
    then another to pass the printer to when creating a pdf.'''


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setWindowTitle(self.tr("test rendering"))
        self.set_settings = ProblemSetPageSettings()
        self.set_settings.columns = 10
        self.page = self.page_layout(self.make_test_set(50), self.set_settings)
        self.layout.addWidget(self.page)
        self.setLayout(self.layout)

    #refactor into PageViewer class that contains Pages containing widgets generated according to problem sets and page settings
    def page_layout(self, problem_set, set_settings):
        page_widget = QtWidgets.QWidget()
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(10, 100, 10, 50))
        page_widget.setAutoFillBackground(True)
        page_widget.setPalette(pal)


        layout = QtWidgets.QGridLayout(page_widget)

        page_size = self.size()
        page_width = page_size.height() * (17/22)
        page_widget.setFixedSize(page_width, page_size.height())

        available_page_width = page_width
        max_prob_size = page_widget.fontMetrics().boundingRect(problem_set.get_largest_problem().__str__())
        answer_space = 10
        max_width = max_prob_size.width()
        max_height = max_prob_size.height()
        col_count = page_width // (max_width + answer_space)
        print("page_width: {}\nproblem_width: {}\ncol_count: {}".format(page_width, max_width, col_count))
        row_count = set_settings.max_problems_per_page // max_height
        col = 0
        row = 0

        for i in problem_set.problems:
            problem_label = self.problem_label(i)
            test_font = QtGui.QFont()
            test_font.setPointSizeF(set_settings.font_size)
            problem_label.setFont(test_font)

            layout.addWidget(problem_label, row, col)
            col += 1
            if col == col_count:
                row += 1
                col = 0

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
