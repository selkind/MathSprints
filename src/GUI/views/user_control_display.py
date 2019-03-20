from PyQt5 import QtWidgets
from src.GUI.views.problem_set_layout import ProblemSetLayout
from src.problem_set_page_settings import ProblemSetPageSettings
from src.GUI.views.problem_setting_management import ProblemSettingManagement
from src.problem_settings import ProblemSettings
from src.GUI.views.worksheet_layout_management import WorksheetLayoutManagement
from src.worksheet_layout_settings import WorksheetLayoutSettings
from src.GUI.views.problem_set_management import ProblemSetManagement
from src.worksheet import Worksheet
from tests.basic_problem_set import BasicProblemSet


class UserControlDisplay(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QVBoxLayout(self)

        sheet_settings = WorksheetLayoutSettings()
        self.sheet_controls = WorksheetLayoutManagement(sheet_settings)
        self.layout.addWidget(self.sheet_controls)

        self.worksheet = Worksheet()
        self.worksheet.name = "testsheet"
        self.worksheet.problem_sets.append(BasicProblemSet(20, "test20").prob_set)
        self.worksheet.problem_sets.append(BasicProblemSet(40, "test40").prob_set)

        self.set_management = ProblemSetManagement(self.worksheet)
        self.layout.addWidget(self.set_management)

        set_settings = ProblemSettings()
        self.problem_setting_controls = ProblemSettingManagement(set_settings)
        self.layout.addWidget(self.problem_setting_controls)

        set_page_settings = ProblemSetPageSettings()
        self.problem_set_layout_controls = ProblemSetLayout(set_page_settings)
        self.layout.addWidget(self.problem_set_layout_controls)
