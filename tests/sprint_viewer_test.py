from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from src.GUI.views.worksheet_display import WorksheetDisplay
from src.problem_set_page_settings import ProblemSetPageSettings
from tests.basic_problem_set import BasicProblemSet
from src.GUI.controllers.printer import Printer
from src.GUI.views.user_control_display import UserControlDisplay
from src.worksheet import Worksheet
from src.GUI.controllers.problem_set_layout import ProblemSetLayoutManager
import sys


class MainWindow:
    def __init__(self):
        self.window = None
        self.main_layout = None
        self.worksheet_display = None
        self.ctrl_panel = None
        self.set_layout_manager = None

    def run(self):
        app = QApplication([])

        self.window = QWidget()
        self.main_layout = QGridLayout()
        self.window.setLayout(self.main_layout)

        self.worksheet_display = WorksheetDisplay()

        set_page_settings = ProblemSetPageSettings()
        test_set = BasicProblemSet(100, "test100")
        test_set2 = BasicProblemSet(10, "test10")

        sheet = Worksheet()
        sheet.problem_sets.append([test_set.prob_set, set_page_settings])
        sheet.problem_sets.append([test_set2.prob_set, set_page_settings])

        self.worksheet_display.worksheet = sheet
        self.worksheet_display.problem_set_settings.append(set_page_settings)
        self.worksheet_display.problem_set_settings.append(set_page_settings)

        self.worksheet_display.load_pages_to_viewer()

        self.main_layout.addWidget(self.worksheet_display, 0, 1)

        self.ctrl_panel = UserControlDisplay()
        self.main_layout.addWidget(self.ctrl_panel, 0, 0)

        self.configure_test_buttons()

        self.set_layout_manager = ProblemSetLayoutManager(self.ctrl_panel.problem_set_layout_controls,
                                                          self.worksheet_display)

        self.set_layout_manager.set_current_model(sheet.problem_sets[0][1])

        self.set_layout_manager.load_to_view()

        self.window.show()

        sys.exit(app.exec_())

    def configure_panel_buttons(self):
        self.set_layout_manager = ProblemSetLayoutManager(self.ctrl_panel.problem_set_layout_controls)

    def configure_test_buttons(self):
        viewer_toggle = QPushButton("toggle page viewer")
        viewer_toggle.clicked.connect(lambda: self.toggle_visiblity(self.worksheet_display))

        self.main_layout.addWidget(viewer_toggle, 1, 0)

        print_but = QPushButton("print sprint")
        print_but.clicked.connect(lambda: self.print_sprint(self.worksheet_display))

        self.main_layout.addWidget(print_but, 2, 0)

        change_but = QPushButton("change problem_set")
        change_but.clicked.connect(lambda: self.change_problem_set())

        self.main_layout.addWidget(change_but, 3, 0)

    def clear_problem_set(self):
        self.worksheet_display.clear_layout(self.worksheet_display.layout)

    def change_problem_set(self):
        self.worksheet_display.clear_layout(self.worksheet_display.layout)

        new_set_settings = ProblemSetPageSettings()
        new_set = BasicProblemSet(20, "test20")

        self.worksheet_display.problem_sets = []
        self.worksheet_display.problem_set_settings = []

        self.worksheet_display.problem_sets.append(new_set.prob_set)
        self.worksheet_display.problem_set_settings.append(new_set_settings)
        self.worksheet_display.load_pages_to_viewer()

    def toggle_visiblity(self, widget):
        if widget.isHidden():
            widget.show()
        else:
            widget.hide()

    def print_sprint(self, widget):
        printer = Printer()
        printer.worksheet_to_pdf(widget)


if __name__ == "__main__":
    program = MainWindow()
    program.run()
