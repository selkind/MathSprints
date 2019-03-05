from PyQt5 import QtWidgets, QtGui, QtCore
from src.GUI.Page import Page
from src.GUI.ProblemSetPageSettings import ProblemSetPageSettings

"""
This class manages the distribution of problem sets on pages and displays those pages as a 
    comprehensive sprint
"""


class SprintViewer(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.page_background = QtGui.QColor(10, 100, 10, 50)
        self.problem_background = QtGui.QColor(10, 10, 100, 50)
        self.header_background = QtGui.QColor(100, 10, 10, 50)
        self.aspect_ratio = 17/22

        self.layout = QtWidgets.QVBoxLayout()
        self.pages = []
        self.problem_sets = []
        self.problem_set_settings = []
        self.add_header()

    def add_header(self):
        first_page = self.new_page()
        first_page.logicalDpiY()

        header = self.build_sprint_header()
        first_page.layout.addWidget(header)
        first_page.available_height -= header.size().height()
        self.pages.append(first_page)

    def build_sprint_header(self):
        header = QtWidgets.QWidget()
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, self.header_background)
        header.setAutoFillBackground(True)
        header.setPalette(pal)

        font = QtGui.QFont()
        font.setPointSizeF(4)
        layout = QtWidgets.QHBoxLayout()

        name = QtWidgets.QLabel("Name:")
        name.setFont(font)
        height = name.fontMetrics().boundingRect(name.text()).height()

        date = QtWidgets.QLabel("Date:")
        date.setFont(font)

        layout.addWidget(name)
        layout.addWidget(date)
        layout.setAlignment(QtCore.Qt.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        header.setFixedHeight(height)

        header.setLayout(layout)
        return header

    def layout_problem_set(self, problem_set, set_settings):
        largest_problem = problem_set.get_largest_problem()
        max_label = self.generate_problem_label(largest_problem, set_settings.font_size)
        max_prob_size = max_label.fontMetrics().boundingRect(max_label.text())

        max_width = max_prob_size.width() + set_settings.h_answer_space
        problem_height = max_prob_size.height() + set_settings.v_answer_space

        set_label = self.generate_set_header(problem_set.name)

        has_room = self.pages[-1].available_height - problem_height - set_label.height() > 0

        if has_room:
            current_page = self.pages.pop()
        else:
            current_page = self.new_page()

        current_page.available_width = current_page.size().width()

        current_page.available_height -= set_label.height()
        current_page.layout.addWidget(set_label)

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()

        col_count = current_page.available_width // max_width
        if col_count < 1:
            raise ValueError("largest problem in set is too large to fit on a single line with selected font size")

        row_count = min(set_settings.max_problems_per_page // col_count,
                        current_page.available_height // problem_height)
        print("row_count: {}".format(row_count))

        col = 0
        row = 0

        for i in problem_set.problems:
            problem = self.generate_problem_label(i, set_settings.font_size)
            problem.setFixedSize(max_width, problem_height)
            layout.addWidget(problem, row, col)
            col += 1
            if col == col_count:
                row += 1
                col = 0
                current_page.available_height -= problem_height

            if row == row_count or current_page.available_height - problem_height < 0:
                current_page.available_height = 0
                widget.setLayout(layout)
                current_page.layout.addWidget(widget)
                self.pages.append(current_page)

                current_page = self.new_page()
                current_page.available_width = current_page.size().width()
                row_count = min(set_settings.max_problems_per_page // col_count,
                                current_page.available_height // problem_height)
                widget = QtWidgets.QWidget()
                layout = QtWidgets.QGridLayout()
                row = 0
                col = 0

        widget.setLayout(layout)
        current_page.layout.addWidget(widget)
        self.pages.append(current_page)

    def generate_set_header(self, name):
        header = QtWidgets.QWidget()

        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, self.header_background)
        header.setAutoFillBackground(True)
        header.setPalette(pal)

        font = QtGui.QFont()
        font.setPointSizeF(4)
        layout = QtWidgets.QHBoxLayout()

        name = QtWidgets.QLabel(name)
        name.setFont(font)
        height = name.fontMetrics().boundingRect(name.text()).height()


        layout.addWidget(name)
        layout.setAlignment(QtCore.Qt.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        header.setFixedHeight(height)

        header.setLayout(layout)
        return header

    """
    Creates a label containing the text of a problem
    """
    
    def generate_problem_label(self, problem, font_size, display_answer=False):
        font = QtGui.QFont()
        font.setPointSize(font_size)

        problem = QtWidgets.QLabel(problem.__str__())

        problem.setAlignment(QtCore.Qt.AlignLeft)

        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, self.problem_background)
        problem.setAutoFillBackground(True)
        problem.setPalette(pal)
        problem.setFont(font)

        return problem

    """
    Generates QWidget and configures a blank page with a fixed aspect ratio
    actual dimensions are dependent upon the SprintViewer widget size
    """

    def new_page(self):
        height = self.size().height()
        width = height * self.aspect_ratio

        page = Page(width, height)

        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, self.page_background)
        page.setAutoFillBackground(True)
        page.setPalette(pal)

        page.setFixedSize(width, height)

        return page
