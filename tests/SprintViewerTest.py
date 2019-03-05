from PyQt5.QtWidgets import QApplication, QScrollArea, QFrame, QHBoxLayout, QWidget, QGridLayout, QPushButton
from src.GUI.sprint_viewer import SprintViewer
from src.GUI.ProblemSetPageSettings import ProblemSetPageSettings
from tests.basic_problem_set import TestSet
from src.GUI.pdf_print_test import Window
import sys

def run():
    app = QApplication([])
    main = QWidget()
    main_layout = QGridLayout()
    main.setLayout(main_layout)


    sprint = SprintViewer()

    set_page_settings = ProblemSetPageSettings()
    test_set = TestSet(100)

    sprint.problem_sets.append(test_set.prob_set)
    sprint.problem_set_settings.append(set_page_settings)

    sprint.layout_problem_set(sprint.problem_sets[0], sprint.problem_set_settings[0])

    for i in sprint.pages:
        i.setLayout(i.layout)
        sprint.layout.addWidget(i)

    sprint.setLayout(sprint.layout)

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setWidget(sprint)

    main_layout.addWidget(scroll, 0, 1)

    viewer_toggle = QPushButton("toggle page viewer")
    viewer_toggle.clicked.connect(lambda: toggle_visiblity(scroll))

    main_layout.addWidget(viewer_toggle, 0, 0)

    print_but = QPushButton("print sprint")
    print_but.clicked.connect(lambda: print_sprint(sprint))

    main_layout.addWidget(print_but, 1, 0)

    main.show()

    print(main.children())

    sys.exit(app.exec_())


def toggle_visiblity(widget):
    if widget.isHidden():
        widget.show()
    else:
        widget.hide()

def print_sprint(widget):
    printer = Window()
    printer.print_screen(widget)


if __name__ == "__main__":
    run()
