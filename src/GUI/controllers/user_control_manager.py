from src.GUI.controllers.worksheet_set_manager import WorksheetSetManager
from src.GUI.controllers.problem_set_manager import ProblemSetManager
from src.GUI.controllers.problem_settings_manager import ProblemSettingsManager
from src.GUI.controllers.problem_set_layout_manager import ProblemSetLayoutManager


class UserControlManager:
    def __init__(self, view, sheet_display):
        self.view = view
        self.sheet_display = sheet_display

        self.sheet_set_manager = None
        self.problem_set_manager = None
        self.problem_settings_manager = None
        self.set_layout_manager = None

    def configure_for_startup(self):
        self.sheet_set_manager = WorksheetSetManager(self.view.set_management, self.sheet_display)
        self.problem_set_manager = ProblemSetManager(self.view.problem_set_display, self.sheet_display)
        self.problem_settings_manager = ProblemSettingsManager(self.view.problem_setting_controls,
                                                               self.sheet_display)
        self.set_layout_manager = ProblemSetLayoutManager(self.view.problem_set_layout_controls,
                                                          self.sheet_display)

    def load_set_to_view(self):
        pass