class ProblemSetManager:
    def __init__(self, view, sheet_display):
        self.view = view
        self.sheet_display = sheet_display
        self.current_model = None

    def set_current_model(self, model):
        self.current_model = model
        self.load_to_view()

    def load_to_view(self):
        if self.current_model is None:
            return
        self.view.set_name.setText(self.current_model.name)
        self.view.problem_count.setValue(self.current_model.problem_count)

    def update_model(self):
        self.current_model.name = self.view.set_name.text()
        self.current_model.problem_count = self.view.problem_count.value()
