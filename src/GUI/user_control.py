from PyQt5 import QtWidgets
from src.GUI.problem_set_layout_controls import ProblemSetLayoutControls
from src.GUI.ProblemSetPageSettings import ProblemSetPageSettings
from src.GUI.problem_setting_controls import ProblemSettingControls
from src.ProblemSettings import ProblemSettings
from src.GUI.worksheet_layout_controls import WorksheetLayoutControls
from src.GUI.worksheet_layout_settings import WorksheetLayoutSettings
from src.GUI.problem_set_management_controls import ProblemSetManagementControls
from src.Worksheet import Worksheet
from tests.basic_problem_set import TestSet


class UserControl(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QVBoxLayout(self)

        sheet_settings = WorksheetLayoutSettings()
        self.sheet_controls = WorksheetLayoutControls(sheet_settings)
        self.layout.addWidget(self.sheet_controls)

        self.worksheet = Worksheet()
        self.worksheet.name = "testsheet"
        self.worksheet.problem_sets.append(TestSet(20, "test20").prob_set)
        self.worksheet.problem_sets.append(TestSet(40, "test40").prob_set)

        self.set_management = ProblemSetManagementControls(self.worksheet)
        self.layout.addWidget(self.set_management)

        set_settings = ProblemSettings()
        self.problem_setting_controls = ProblemSettingControls(set_settings)
        self.layout.addWidget(self.problem_setting_controls)

        set_page_settings = ProblemSetPageSettings()
        self.problem_set_layout_controls = ProblemSetLayoutControls(set_page_settings)
        self.layout.addWidget(self.problem_set_layout_controls)
