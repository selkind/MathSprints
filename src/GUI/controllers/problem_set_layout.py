class ProblemSetLayoutManager:
    def __init__(self):
        pass

    def load_to_view(self, view, model):
        view.v_space.setValue(model.v_answer_space)
        view.h_space.setValue(model.h_answer_space)

        if model.auto_columns:
            view.col_number.setCurrentText("Auto")
        else:
            view.col_number.setCurrentText(str(model.columns))

        view.point_val.setValue(model.max_problems_per_page)
        view.point_val.setValue(model.problem_value)

