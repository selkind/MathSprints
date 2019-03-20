from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from src.GUI.views.user_control_display import UserControlDisplay
import sys


class MainWindow:
    def __init__(self):
        self.window = None
        self.main_layout = None
        self.control = None

    def run(self):
        app = QApplication([])

        self.window = QWidget()
        self.main_layout = QGridLayout()
        self.window.setLayout(self.main_layout)

        self.control = UserControlDisplay()
        self.main_layout.addWidget(self.control)

        self.window.show()

        sys.exit(app.exec_())


if __name__ == "__main__":
    program = MainWindow()
    program.run()
