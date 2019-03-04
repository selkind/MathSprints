from PyQt5.QtWidgets import QApplication
from src.GUI.sprint_viewer import SprintViewer
from src.GUI.ProblemSetPageSettings import ProblemSetPageSettings
from tests.basic_problem_set import TestSet
from src.GUI.pdf_print_test import Window
import sys


def run():
    app = QApplication([])
    sprint = SprintViewer()
    set_page_settings = ProblemSetPageSettings()
    test_set = TestSet(50)

    sprint.problem_sets.append(test_set.prob_set)
    sprint.problem_set_settings.append(set_page_settings)

    sprint.layout_problem_set(sprint.problem_sets[0], sprint.problem_set_settings[0])

    for i in sprint.pages:
        sprint.layout.addWidget(i)

    sprint.setLayout(sprint.layout)

    sprint.show()

    printer = Window()
    printer.print_screen(sprint)

    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
