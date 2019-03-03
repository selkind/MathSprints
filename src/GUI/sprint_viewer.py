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
        self.layout = QtWidgets.QVBoxLayout(self)
        self.pages = []
        self.pages.append(self.new_page())
        self.problem_sets = []
        self.problem_set_settings = []

        self.page_background = QtGui.QColor(10, 100, 10, 50)
        self.problem_background = QtGui.QColor(10, 10, 100, 50)
        self.aspect_ratio = 17/22

    def layout_problem_set(self, problem_set, set_settings):
        largest_problem = problem_set.get_largest_problem()
        max_prob_size = largest_problem.fontMetrics().boundingRect(largest_problem.__str__())

        max_width = max_prob_size.width()
        problem_height = max_prob_size.height()

        has_room = self.pages[-1].available_height - problem_height > 0

        if has_room:
            current_page = self.pages.pop()
        else:
            current_page = self.new_page()

        current_page.available_width = current_page.size().width()
        layout = QtWidgets.QGridLayout(current_page)

        col_count = current_page.size().width() // (max_width + ProblemSetPageSettings.ANSWER_SPACE)
        if col_count < 1:
            raise ValueError("largest problem in set is too large to fit on a single line with selected font size")

        row_count = set_settings.max_problems_per_page // problem_height

        col = 0
        row = 0

        for i in problem_set.problems:
            layout.addWidget(self.generate_problem_label(i), row, col)
            col += 1
            if col == col_count:
                row += 1
                col = 0
                current_page.available_height -= problem_height

            if row == row_count or current_page.available_height - problem_height < 0:
                current_page.available_height = 0
                self.pages.append(current_page)
                current_page = self.new_page()
                current_page.available_width = current_page.size().width()
                layout = QtWidgets.QGridLayout(current_page)
                row = 0
                col = 0

        self.pages.append(current_page)

    """
    Creates a label containing the text of a problem
    """
    
    def generate_problem_label(self, problem, display_answer=False):
        font = QtGui.QFont()
        font.setPointSize(12)

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
