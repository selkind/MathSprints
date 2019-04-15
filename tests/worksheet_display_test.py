import unittest
from PyQt5.QtWidgets import QLabel, QWidget
from tests.empty_page_repro import MainWindow

'''
The testing structure used here is pretty sloppy and not really unittesting. It's more about being able to reliably
reproduce a state of the application and assert that certain properties of the app in that state are consistent with
expectations. It works for now. It'll be interesting to see if this testing setup is extendable and maintainable.
'''


class WorksheetDisplayTest(unittest.TestCase):
    def setUp(self):
        self.test_ob = MainWindow()

    def test_problem_widgets_dont_overlap(self):
        res = self.test_ob.repro_overlapping_widgets()
        for i in res.pages:
            print(i.available_height)
            print(i.height())
        widgets = [i for i in res.pages[1].children() if isinstance(i, QWidget)]
        labels = []
        for i in widgets:
            labels += [j for j in i.children() if isinstance(j, QLabel)]
        for i in labels:
            print(i.rect().height())

    def test_last_page_removed_when_empty(self):
        res = self.test_ob.repro_blank_page()
        page_count = len(res.pages)
        has_problems = False
        for i in res.pages[-1].children():
            if isinstance(i, QWidget):
                for j in i.children():
                    if isinstance(j, QLabel):
                        has_problems = True
        self.assertTrue(has_problems)
