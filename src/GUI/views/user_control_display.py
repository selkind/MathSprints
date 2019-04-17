from PyQt5 import QtWidgets
from src.GUI.views.problem_set_layout import ProblemSetLayout
from src.GUI.views.problem_setting_display import ProblemSettingDisplay
from src.GUI.views.problem_set_display import ProblemSetDisplay
from src.GUI.views.worksheet_layout_management import WorksheetLayoutManagement
from src.worksheet_layout_settings import WorksheetLayoutSettings
from src.GUI.views.worksheet_set_display import WorksheetSetDisplay


'''basically a container to hold all of the user input controls'''


class UserControlDisplay(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QVBoxLayout(self)

        sheet_layout_settings = WorksheetLayoutSettings()
        self.sheet_controls = WorksheetLayoutManagement(sheet_layout_settings)
        self.layout.addWidget(self.sheet_controls)

        self.set_management = WorksheetSetDisplay()
        self.layout.addWidget(self.set_management)

        self.problem_set_display = ProblemSetDisplay()
        self.layout.addWidget(self.problem_set_display)

        self.problem_setting_controls = ProblemSettingDisplay()
        self.layout.addWidget(self.problem_setting_controls)

        self.problem_set_layout_controls = ProblemSetLayout()
        self.layout.addWidget(self.problem_set_layout_controls)
