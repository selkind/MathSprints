from PyQt5.QtWidgets import QApplication, QScrollArea, QFrame, QHBoxLayout, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QPageSize
from PyQt5.QtPrintSupport import QPrinter
from src.GUI.sprint_viewer import SprintViewer
from src.GUI.ProblemSetPageSettings import ProblemSetPageSettings
from tests.basic_problem_set import TestSet
from src.GUI.pdf_print_test import Window
from src.GUI.user_control import UserControl
import sys


class MainWindow:
    def __init__(self):
        self.window = None
        self.main_layout = None
        self.control = None

    def run(self):
        app = QApplication([])

        self.window = QWidget()
        self.main_layout = QGridLayout()
        self.window.setLayout(self.main_layout)

        self.control = UserControl()
        self.main_layout.addWidget(self.control)

        self.window.show()

        sys.exit(app.exec_())


if __name__ == "__main__":
    program = MainWindow()
    program.run()
