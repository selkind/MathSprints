import unittest
from tests.empty_page_repro import MainWindow

'''
The testing structure used here is pretty sloppy and not really unittesting. It's more about being able to reliably
reproduce a state of the application and assert that certain properties of the app in that state are consistent with
expectations. It works for now. It'll be interesting to see if this testing setup is extendable and maintainable.
'''


class WorksheetDisplayTest(unittest.TestCase):
    def setUp(self):
        self.test_ob = MainWindow()

    def test_last_page_removed_when_empty(self):
        res = self.test_ob.repro_blank_page()
        for i in res.pages:
            print(i.available_height)
            print(i.available_width)
            print(i.children())
        res = len(res.pages)
        self.assertEqual(1, res)