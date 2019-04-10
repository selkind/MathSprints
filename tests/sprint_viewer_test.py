from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from src.GUI.views.worksheet_display import WorksheetDisplay
from src.problem_set_page_settings import ProblemSetPageSettings
from src.GUI.controllers.printer import Printer
from src.GUI.views.user_control_display import UserControlDisplay
from src.worksheet import Worksheet
from src.GUI.controllers.user_control_manager import UserControlManager
from src.GUI.controllers.problem_set_layout_manager import ProblemSetLayoutManager
from src.GUI.controllers.worksheet_set_manager import WorksheetSetManager
from src.GUI.controllers.problem_settings_manager import ProblemSettingsManager
from src.problem_set import ProblemSet
from src.problem_settings import ProblemSettings
import sys


class MainWindow:
    def __init__(self):
        self.window = None
        self.main_layout = None
        self.worksheet_display = None
        self.ctrl_panel = None
        self.sheet_set_manager = None
        self.set_layout_manager = None
        self.problem_settings_manager = None
        self.user_control_manager = None

    def run(self):
        app = QApplication([])

        self.window = QWidget()
        self.main_layout = QGridLayout()
        self.window.setLayout(self.main_layout)

        self.worksheet_display = WorksheetDisplay()

        set_page_settings = ProblemSetPageSettings()
        set_page_settings2 = ProblemSetPageSettings()
        set_page_settings2.max_problems_per_page = 5
        settings = ProblemSettings()
        settings2 = ProblemSettings()
        settings2.operator_sets = [["-"]]
        test_set = ProblemSet(settings, "set1")
        test_set2 = ProblemSet(settings2, "set2")
        test_set.problem_count = 10
        test_set2.problem_count = 5
        test_set.build_set()
        test_set2.build_set()

        sheet = Worksheet()
        sheet.problem_sets.append({"name": test_set.name,
                                   "set": test_set,
                                   "settings": set_page_settings})

        sheet.problem_sets.append({"name": test_set2.name,
                                   "set": test_set2,
                                   "settings": set_page_settings2})

        self.worksheet_display.worksheet = sheet

        self.worksheet_display.load_pages_to_viewer()

        self.main_layout.addWidget(self.worksheet_display, 0, 1)

        self.ctrl_panel = UserControlDisplay()
        self.main_layout.addWidget(self.ctrl_panel, 0, 0)
        self.user_control_manager = UserControlManager(self.ctrl_panel, self.worksheet_display)
        self.user_control_manager.configure_for_startup()

        self.configure_test_buttons()

        self.user_control_manager.problem_set_manager.set_current_model(sheet.problem_sets[-1]["set"])
        self.user_control_manager.problem_settings_manager.set_current_model(sheet.problem_sets[-1]["set"].settings)
        self.user_control_manager.set_layout_manager.set_current_model(sheet.problem_sets[-1]["settings"])

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

    def clear_problem_set(self):
        self.worksheet_display.clear_layout(self.worksheet_display.layout)

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
