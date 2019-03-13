from PyQt5 import QtWidgets, QtGui, QtCore
from src.GUI.Page import Page
from src.GUI.ProblemSetPageSettings import ProblemSetPageSettings

"""
This class manages the distribution of problem sets on pages and displays those pages as a 
    comprehensive sprint
"""


class SprintViewer(QtWidgets.QScrollArea):
    def __init__(self):
        QtWidgets.QScrollArea.__init__(self)
        self.page_background = QtGui.QColor(10, 100, 10, 50)
        self.problem_background = QtGui.QColor(10, 10, 100, 50)
        self.header_background = QtGui.QColor(100, 10, 10, 50)
        self.aspect_ratio = 17/22

        self.layout = QtWidgets.QVBoxLayout()
        self.setWidgetResizable(True)
        self.current_frame = None
        self.pages = None
        self.problem_sets = []
        self.problem_set_settings = []

    def load_pages_to_viewer(self):
        self.pages = []
        self.add_header()
        self.current_frame = QtWidgets.QWidget()
        page_layout = QtWidgets.QVBoxLayout()
        self.current_frame.setLayout(page_layout)

        for i in range(len(self.problem_sets)):
            self.layout_problem_set(self.problem_sets[i], self.problem_set_settings[i])
        for i in self.pages:
            i.setLayout(i.layout)
            page_layout.addWidget(i)
        self.layout.addWidget(self.current_frame)
        self.setWidget(self.current_frame) # critical to make scroll area work

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def add_header(self):
        first_page = self.new_page()

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

    def layout_problem_set(self, problem_set, set_page_settings):
        """
        get space requirements of the largest problem in the set and use that rect as the widget size for each problem
        This ensures no widget overflow/overlap on page.
        """
        largest_problem = problem_set.get_largest_problem()
        max_label = self.generate_problem_label(largest_problem, set_page_settings.font_size)
        max_prob_size = max_label.fontMetrics().boundingRect(max_label.text())

        max_width = max_prob_size.width() + set_page_settings.h_answer_space
        problem_height = max_prob_size.height() + set_page_settings.v_answer_space

        """
        configure problem set header and add it to considerations used to choose whether set begins on a new page
        """
        prob_count = len(problem_set.problems)

        set_label = self.generate_set_header(problem_set.name, set_page_settings.problem_value * prob_count)

        has_room = self.pages[-1].available_height - problem_height - set_label.height() > 0

        if has_room:
            current_page = self.pages.pop()
        else:
            current_page = self.new_page()

        # not sure if this is necessary. Should revisit once more page sizes are supported

        current_page.available_height -= set_label.height()
        current_page.layout.addWidget(set_label)

        current_page.available_width = current_page.size().width()

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(0,0,0,0)

        col_count = current_page.available_width // max_width
        if col_count < 1:
            raise ValueError("largest problem in set is too large to fit on a single line with selected font size")

        row_count = min(set_page_settings.max_problems_per_page // col_count,
                        current_page.available_height // problem_height)

        col = 0
        row = 0

        for i in problem_set.problems:
            problem = self.generate_problem_label(i, set_page_settings.font_size)
            problem.setFixedSize(max_width, problem_height)
            layout.addWidget(problem, row, col)

            col += 1

            if col == col_count:
                row += 1
                col = 0
                current_page.available_height -= problem_height

            if row == row_count or current_page.available_height - problem_height < 0:
                # ensures current page will not have any problems added to it from another problem set
                current_page.available_height = 0
                widget.setLayout(layout)
                current_page.layout.addWidget(widget)
                self.pages.append(current_page)

                current_page = self.new_page()
                current_page.available_width = current_page.size().width()
                row_count = min(set_page_settings.max_problems_per_page // col_count,
                                current_page.available_height // problem_height)

                widget = QtWidgets.QWidget()
                layout = QtWidgets.QGridLayout()
                row = 0
                col = 0

        widget.setLayout(layout)
        current_page.layout.addWidget(widget)
        self.pages.append(current_page)

        """
        creates a header for a problem set with Set name and grading space
        """

    def generate_set_header(self, name, max_score):
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

        score = QtWidgets.QLabel("/{} points".format(max_score))
        score.setFont(font)

        layout.addWidget(score)

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
