from src.models.problem_set_page_settings import ProblemSetPageSettings
from src.models.problem_settings import ProblemSettings
from src.models.problem_set import ProblemSet


class WorksheetSetManager:
    def __init__(self, view, sheet_display):
        self.view = view
        self.sheet_display = sheet_display # In this case, the sheet_display is the "current_model" and never changes.
        self.configure_list()
        self.configure_buttons()

    def configure_buttons(self):
        self.view.add_button.clicked.connect(lambda: self.add_item())
        self.view.del_button.clicked.connect(lambda: self.remove_item())
        self.view.up_button.clicked.connect(lambda: self.shift_up())
        self.view.down_button.clicked.connect(lambda: self.shift_down())

    def configure_list(self):
        for i in self.sheet_display.worksheet.problem_sets:
            self.view.add_item_to_set_list(i["set"].name)
        self.view.set_list.setCurrentRow(self.view.set_list.count() - 1)

    def add_item(self):
        page_settings = ProblemSetPageSettings()
        page_settings.max_problems_per_page = 5
        settings = ProblemSettings()
        settings.problem_elements = [{"terms": {"Integer": [{"range": False, "vals": [0, 1, 2, 3, 4, 5]}]},
                                      "operators": ["+"]}]

        new_set = ProblemSet(settings, "New Set")
        new_set.problem_count = 5
        new_set.build_set()
        self.sheet_display.worksheet.problem_sets.append({"set": new_set,
                                                          "settings": page_settings})
        self.view.add_item_to_set_list(new_set.name)
        self.view.set_list.setCurrentRow(self.view.set_list.count() - 1)
        self.sheet_display.load_pages_to_viewer()

    def remove_item(self):
        row = self.view.set_list.currentRow()
        self.view.set_list.takeItem(row)
        self.sheet_display.worksheet.problem_sets.pop(row)
        # refactor the deleteLater line into worksheet_set_display
        self.sheet_display.load_pages_to_viewer()

    def shift_up(self):
        row = self.view.set_list.currentRow()
        if row == 0:
            return
        selected = self.view.set_list.takeItem(row)
        new_row = row - 1
        self.view.set_list.insertItem(new_row, selected)
        self.view.set_list.setCurrentRow(new_row)

        shifted_set = self.sheet_display.worksheet.problem_sets.pop(row)
        self.sheet_display.worksheet.problem_sets.insert(new_row, shifted_set)
        self.sheet_display.load_pages_to_viewer()

    def shift_down(self):
        row = self.view.set_list.currentRow()
        if row == self.view.set_list.count() - 1:
            return
        selected = self.view.set_list.takeItem(row)
        new_row = row + 1
        self.view.set_list.insertItem(new_row, selected)
        self.view.set_list.setCurrentRow(new_row)

        shifted_set = self.sheet_display.worksheet.problem_sets.pop(row)
        self.sheet_display.worksheet.problem_sets.insert(new_row, shifted_set)
        self.sheet_display.load_pages_to_viewer()

