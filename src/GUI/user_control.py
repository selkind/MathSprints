from PyQt5 import QtGui, QtWidgets
from src.GUI.problem_set_layout_controls import ProblemSetLayoutControls
from src.GUI.ProblemSetPageSettings import ProblemSetPageSettings
from src.GUI.problem_setting_controls import ProblemSettingControls
from src.ProblemSettings import ProblemSettings
from src.GUI.worksheet_layout_controls import WorksheetLayoutControls
from src.GUI.worksheet_layout_settings import WorksheetLayoutSettings


class UserControl(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)

        sheet_settings = WorksheetLayoutSettings()
        self.sheet_controls = WorksheetLayoutControls(sheet_settings)
        self.layout.addWidget(self.sheet_controls, 0, 0)

        set_settings = ProblemSettings()
        self.problem_setting_controls = ProblemSettingControls(set_settings)
        self.layout.addWidget(self.problem_setting_controls, 1, 0)

        set_page_settings = ProblemSetPageSettings()
        self.problem_set_layout_controls = ProblemSetLayoutControls(set_page_settings)
        self.layout.addWidget(self.problem_set_layout_controls, 2, 0)
