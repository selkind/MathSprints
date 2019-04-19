from PyQt5 import QtWidgets
from src.GUI.views.problem_set_layout import ProblemSetLayout
from src.GUI.views.problem_setting_display import ProblemSettingDisplay
from src.GUI.views.problem_set_display import ProblemSetDisplay
from src.GUI.views.worksheet_layout_management import WorksheetLayoutManagement
from src.worksheet_layout_settings import WorksheetLayoutSettings
from src.GUI.views.worksheet_set_display import WorksheetSetDisplay


'''basically a container to hold all of the user input controls'''


class UserControlDisplay(QtWidgets.QScrollArea):
    def __init__(self):
        QtWidgets.QScrollArea.__init__(self)
        self.setWidgetResizable(True)
        self.layout = QtWidgets.QVBoxLayout(self)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        self.layout.addWidget(widget)
        self.setWidget(widget)

        sheet_layout_settings = WorksheetLayoutSettings()
        self.sheet_controls = WorksheetLayoutManagement(sheet_layout_settings)
        layout.addWidget(self.sheet_controls)

        self.set_management = WorksheetSetDisplay()
        layout.addWidget(self.set_management)

        self.problem_set_display = ProblemSetDisplay()
        layout.addWidget(self.problem_set_display)

        self.problem_setting_controls = ProblemSettingDisplay()
        layout.addWidget(self.problem_setting_controls)

        self.problem_set_layout_controls = ProblemSetLayout()
        layout.addWidget(self.problem_set_layout_controls)
