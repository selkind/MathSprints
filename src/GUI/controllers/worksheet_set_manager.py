from tests.basic_problem_set import BasicProblemSet
from src.problem_settings import ProblemSettings
from src.problem_set_page_settings import ProblemSetPageSettings


class WorksheetSetManager:
    def __init__(self, view, sheet_display):
        self.view = view
        self.sheet_display = sheet_display

    def configure_buttons(self):
        self.view.add_button.clicked.connect(lambda: self.add_item())
        self.view.del_button.clicked.connect(lambda: self.remove_item())

    def add_item(self):
        page_settings = ProblemSetPageSettings()
        prob_set = BasicProblemSet(10, "default")
        self.sheet_display.worksheet.problem_sets.append({"name": prob_set.prob_set.name,
                                                          "set": prob_set.prob_set,
                                                          "settings": page_settings})
        self.view.add_item_to_set_list(prob_set.prob_set.name)
        self.view.set_list.setCurrentRow(self.view.set_list.count() - 1)
        self.sheet_display.load_pages_to_viewer()

    def remove_item(self):
        item = self.view.set_list.selectedItems()[0]
        for i in self.sheet_display.worksheet.problem_sets:
            if i["name"] == item.text():
                self.sheet_display.worksheet.problem_sets.remove(i)
        self.view.set_list.removeItemWidget(self.view.set_list.selectedItems()[0])
        self.sheet_display.load_pages_to_viewer()

