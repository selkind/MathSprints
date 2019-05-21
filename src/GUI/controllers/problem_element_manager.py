from src.GUI.controllers.integer_selection_manager import IntegerSelectionManager


class ProblemElementManager:
    def __init__(self, view):
        self.view = view

        self.integer_ctrl = IntegerSelectionManager(self.view.integer_selection)
        self.decimal_ctrl = IntegerSelectionManager(self.view.decimal_selection)
        self.numerator_ctrl = IntegerSelectionManager(self.view.numerator_selection)
        self.denominator_ctrl = IntegerSelectionManager(self.view.denominator_selection)

        self.current_model = None
        self.model_row = None

    def set_current_model(self, model, row):
        self.current_model = model
        self.model_row = row
        self.load_to_view()

    def load_to_view(self):
        self.clear_view()
        self.load_operators()
        self.load_terms()

    def clear_view(self):
        self.view.integer_selection.clear_list()
        self.view.numerator_selection.clear_list()
        self.view.denominator_selection.clear_list()
        self.view.decimal_selection.clear_list()

    def load_operators(self):
        for i in self.view.get_op_checks():
            i.setChecked((i.text() in self.current_model["operators"]))

    def load_terms(self):
        term_types = self.current_model["terms"].keys()
        if "Integer" in term_types:
            self.view.integer_option.setChecked(True)
            self.integer_ctrl.set_current_model(self.current_model["terms"]["Integer"])
            self.integer_ctrl.load_to_view()
        else:
            self.view.integer_option.setChecked(False)

        if "Fraction" in term_types:
            self.view.fraction_option.setChecked(True)
            self.numerator_ctrl.set_current_model(self.current_model["terms"]["Fraction"]["Numerator"]["Integer"])
            self.denominator_ctrl.set_current_model(self.current_model["terms"]["Fraction"]["Denominator"]["Integer"])
        else:
            self.view.fraction_option.setChecked(False)

        if "Decimal" in term_types:
            self.view.decimal_option.setChecked(True)
            self.decimal_ctrl.set_current_model(self.current_model["terms"]["Decimal"])
        else:
            self.view.decimal_option.setChecked(False)

    def update_model(self):
        new_model = {"terms": {}, "operators": []}
        for i in self.view.get_op_checks():
            if i.checkState():
                new_model["operators"].append(i.text())

        if self.view.integer_option.checkState():
            new_model["terms"]["Integer"] = self.integer_ctrl.current_model

        if self.view.fraction_option.checkState():
            new_model["terms"]["Fraction"] = {"Numerator": {"Integer": self.numerator_ctrl.current_model}}
            new_model["terms"]["Fraction"]["Denominator"] = {"Integer": self.denominator_ctrl.current_model}

        if self.view.decimal_option.checkState():
            new_model["terms"]["Decimal"] = self.decimal_ctrl.current_model
            for i in new_model["terms"]["Decimal"]:
                i["precision"] = 3
        self.current_model = new_model
