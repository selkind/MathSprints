import unittest
from tests.empty_page_repro import MainWindow


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