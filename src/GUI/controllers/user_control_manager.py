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
        #print("Problem_set: {}".format(self.problem_set_manager.current_model))
        # ensure that the changes made to problem elements are saved before switching to new problem set.
        if self.problem_settings_manager.problem_element_ctrl.current_model is not None:
            self.problem_settings_manager.problem_element_ctrl.update_model()
            # sorry, this is hideous, maybe I'll refactor it to work and be a little more elegant in the future.
            self.problem_settings_manager.current_model.problem_elements[
                self.problem_settings_manager.problem_element_ctrl.model_row] = \
                self.problem_settings_manager.problem_element_ctrl.current_model
            # this is needed so that the problem_element_manager does not overwrite the model of the newly selected
            # problem set
            self.problem_settings_manager.problem_element_ctrl.current_model = None

        row = self.sheet_set_manager.view.set_list.currentRow()
        problem_set = self.sheet_display.worksheet.problem_sets[row]
        self.problem_set_manager.set_current_model(problem_set["set"])
        self.problem_settings_manager.set_current_model(problem_set["set"].settings)
        self.set_layout_manager.set_current_model(problem_set["settings"])
        #for i in self.sheet_display.worksheet.problem_sets:
            #print(i["set"].settings)
        #print("Problem_set: {}".format(self.problem_set_manager.current_model))

    def update_models(self):
        self.problem_set_manager.update_model()
        self.problem_settings_manager.update_model()
        self.set_layout_manager.update_model()
        row = self.sheet_set_manager.view.set_list.currentRow()
        problem_set = self.sheet_display.worksheet.problem_sets[row]
        problem_set["set"].build_set()
        self.sheet_display.load_pages_to_viewer()

