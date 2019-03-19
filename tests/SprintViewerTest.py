from PyQt5.QtWidgets import QApplication, QScrollArea, QFrame, QHBoxLayout, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QPageSize
from PyQt5.QtPrintSupport import QPrinter
from src.GUI.sprint_viewer import SprintViewer
from src.GUI.ProblemSetPageSettings import ProblemSetPageSettings
from tests.basic_problem_set import TestSet
from src.GUI.pdf_print_test import Window
from src.GUI.user_control import UserControl
from src.Worksheet import Worksheet
import sys


class MainWindow:
    def __init__(self):
        self.window = None
        self.main_layout = None
        self.sprint = None

    def run(self):
        app = QApplication([])

        self.window = QWidget()
        self.main_layout = QGridLayout()
        self.window.setLayout(self.main_layout)

        self.sprint = SprintViewer()

        set_page_settings = ProblemSetPageSettings()
        test_set = TestSet(100, "test100")
        test_set2 = TestSet(10, "test10")

        sheet = Worksheet()
        sheet.problem_sets.append(test_set.prob_set)
        sheet.problem_sets.append(test_set2.prob_set)

        self.sprint.worksheet = sheet
        self.sprint.problem_set_settings.append(set_page_settings)
        self.sprint.problem_set_settings.append(set_page_settings)

        self.sprint.load_pages_to_viewer()

        self.main_layout.addWidget(self.sprint, 0, 1)

        ctrl_panel = UserControl()
        self.main_layout.addWidget(ctrl_panel, 0, 0)

        viewer_toggle = QPushButton("toggle page viewer")
        viewer_toggle.clicked.connect(lambda: self.toggle_visiblity(self.sprint))

        self.main_layout.addWidget(viewer_toggle, 1, 0)

        print_but = QPushButton("print sprint")
        print_but.clicked.connect(lambda: self.print_sprint(self.sprint))

        self.main_layout.addWidget(print_but, 2, 0)

        change_but = QPushButton("change problem_set")
        change_but.clicked.connect(lambda: self.change_problem_set())

        self.main_layout.addWidget(change_but, 3, 0)

        self.window.show()

        sys.exit(app.exec_())

    def clear_problem_set(self):
        self.sprint.clear_layout(self.sprint.layout)

    def change_problem_set(self):
        self.sprint.clear_layout(self.sprint.layout)

        new_set_settings = ProblemSetPageSettings()
        new_set = TestSet(20, "test20")

        self.sprint.problem_sets = []
        self.sprint.problem_set_settings = []

        self.sprint.problem_sets.append(new_set.prob_set)
        self.sprint.problem_set_settings.append(new_set_settings)
        self.sprint.load_pages_to_viewer()

    def toggle_visiblity(self, widget):
        if widget.isHidden():
            widget.show()
        else:
            widget.hide()

    def print_sprint(self, widget):
        printer = Window()
        printer.print_screen(widget)


if __name__ == "__main__":
    program = MainWindow()
    program.run()
