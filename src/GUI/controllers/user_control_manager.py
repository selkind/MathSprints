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
        self.configure_buttons()

    def configure_buttons(self):
        self.sheet_set_manager.view.set_list.itemSelectionChanged.connect(self.load_set_to_view)
        self.problem_set_manager.view.update_but.clicked.connect(self.update_models)

    def load_set_to_view(self):
        print("Problem_set: {}\nProblem_settings: {}\nset_layout: {}".format(self.problem_set_manager.current_model,
                                                                             self.problem_settings_manager.current_model,
                                                                             self.set_layout_manager.current_model))
        row = self.sheet_set_manager.view.set_list.currentRow()
        problem_set = self.sheet_display.worksheet.problem_sets[row]
        self.problem_set_manager.set_current_model(problem_set["set"])
        self.problem_settings_manager.set_current_model(problem_set["set"].settings)
        self.set_layout_manager.set_current_model(problem_set["settings"])

    def update_models(self):
        self.problem_set_manager.update_model()
        self.problem_settings_manager.update_model()
        self.set_layout_manager.update_model()
        row = self.sheet_set_manager.view.set_list.currentRow()
        problem_set = self.sheet_display.worksheet.problem_sets[row]
        problem_set["set"].build_set()
        self.sheet_display.load_pages_to_viewer()
