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
        if self.pages[-1].hasSpace:
            current_page = self.pages.pop()
        else:
            current_page = self.new_page()

        current_page.available_width = current_page.size().width()
        layout = QtWidgets.QGridLayout(current_page)

        # find problem with max width and calculate largest number of columns with that info
        max_problems = set_settings.max_problems_per_page
        # find number of rows that the max problems will take up in the largest number of columns
        col = 0
        row = 0

        for i in problem_set.problems:
            problem_label = self.generate_problem_label(i)
            problem_size = problem_label.fontMetrics().boundingRect(problem_label.text())
            if problem_size > current_page.size().width():
                raise ValueError("problem is too large to fit on a single line with current font")

            if current_page.available_width < problem_size.width():
                row += 1
                col = 0



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
