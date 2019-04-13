class ProblemSetLayoutManager:
    def __init__(self, view, sheet_display):
        self.view = view
        self.sheet_display = sheet_display
        self.current_model = None

    def set_current_model(self, model):
        self.clear_connections()
        self.current_model = model
        self.load_to_view()
        self.configure_buttons()

    def configure_buttons(self):
        self.view.v_space.valueChanged.connect(self.update_v_space)
        self.view.h_space.valueChanged.connect(self.update_h_space)
        self.view.col_number.currentTextChanged.connect(self.update_col_num)
        self.view.page_prob_count.valueChanged.connect(self.update_max_problems)
        self.view.point_val.valueChanged.connect(self.update_problem_val)

    def clear_connections(self):
        if self.current_model is None:
            return
        self.view.v_space.disconnect()
        self.view.h_space.disconnect()
        self.view.col_number.disconnect()
        self.view.page_prob_count.disconnect()
        self.view.point_val.disconnect()

    def load_to_view(self):
        if self.current_model is None:
            return

        self.view.v_space.setValue(self.current_model.v_answer_space)
        self.view.h_space.setValue(self.current_model.h_answer_space)

        if self.current_model.auto_columns:
            self.view.col_number.setCurrentText("Auto")
        else:
            self.view.col_number.setCurrentText(str(self.current_model.columns))

        self.view.page_prob_count.setValue(self.current_model.max_problems_per_page)
        self.view.point_val.setValue(self.current_model.problem_value)

    def update_model(self):
        self.update_v_space()
        self.update_h_space()
        self.update_col_num()
        self.update_max_problems()
        self.update_problem_val()

    def update_v_space(self):
        self.current_model.v_answer_space = self.view.v_space.value()
        self.sheet_display.load_pages_to_viewer()

    def update_h_space(self):
        self.current_model.h_answer_space = self.view.h_space.value()
        self.sheet_display.load_pages_to_viewer()

    def update_col_num(self):
        if self.view.col_number.currentText() == "Auto":
            self.current_model.auto_columns = True
        else:
            self.current_model.auto_columns = False
            self.current_model.columns = int(self.view.col_number.currentText())
        self.sheet_display.load_pages_to_viewer()

    def update_max_problems(self):
        self.current_model.max_problems_per_page = self.view.page_prob_count.value()
        self.sheet_display.load_pages_to_viewer()

    def update_problem_val(self):
        self.current_model.problem_value = self.view.point_val.value()
        self.sheet_display.load_pages_to_viewer()
