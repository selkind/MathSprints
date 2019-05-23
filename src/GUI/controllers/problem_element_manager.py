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
        self.clear_connections()
        self.current_model = model
        self.model_row = row
        self.load_to_view()
        self.configure_buttons()

    def load_to_view(self):
        self.clear_view()

        for i in self.view.get_op_checks():
            if i.text() in self.current_model["operators"]:
                i.setChecked(True)

        self.load_terms()

    def configure_buttons(self):
        self.view.integer_option.stateChanged.connect(lambda: self.toggle_visibility(self.integer_ctrl.view))
        self.view.fraction_option.stateChanged.connect(lambda: self.toggle_visibility(self.numerator_ctrl.view))
        self.view.fraction_option.stateChanged.connect(lambda: self.toggle_visibility(self.denominator_ctrl.view))
        self.view.decimal_option.stateChanged.connect(lambda: self.toggle_visibility(self.decimal_ctrl.view))

    def clear_connections(self):
        if self.current_model is None:
            return
        self.view.integer_option.disconnect()
        self.view.fraction_option.disconnect()
        self.view.decimal_option.disconnect()

    def toggle_visibility(self, widget):
        if widget.isVisible():
            widget.hide()
        else:
            widget.show()

    def clear_view(self):
        self.view.clear_op_checks()
        self.view.integer_option.setChecked(False)
        self.view.fraction_option.setChecked(False)
        self.view.decimal_option.setChecked(False)
        self.integer_ctrl.clear_connections()
        self.numerator_ctrl.clear_connections()
        self.denominator_ctrl.clear_connections()
        self.decimal_ctrl.clear_connections()
        self.view.integer_selection.clear_list()
        self.view.numerator_selection.clear_list()
        self.view.denominator_selection.clear_list()
        self.view.decimal_selection.clear_list()

    def load_terms(self):
        term_types = self.current_model["terms"].keys()
        if "Integer" in term_types:
            self.view.integer_option.setChecked(True)
            self.integer_ctrl.set_current_model(self.current_model["terms"]["Integer"])
            self.integer_ctrl.load_to_view()
            self.integer_ctrl.view.show()
        else:
            self.view.integer_option.setChecked(False)
            self.integer_ctrl.view.hide()

        if "Fraction" in term_types:
            self.view.fraction_option.setChecked(True)
            self.numerator_ctrl.set_current_model(self.current_model["terms"]["Fraction"]["Numerator"]["Integer"])
            self.numerator_ctrl.load_to_view()
            self.denominator_ctrl.set_current_model(self.current_model["terms"]["Fraction"]["Denominator"]["Integer"])
            self.denominator_ctrl.load_to_view()
            self.numerator_ctrl.view.show()
            self.view.numerator_label.show()
            self.denominator_ctrl.view.show()
            self.view.denominator_label.show()
        else:
            self.view.fraction_option.setChecked(False)
            self.numerator_ctrl.view.hide()
            self.view.numerator_label.hide()
            self.denominator_ctrl.view.hide()
            self.view.denominator_label.hide()

        if "Decimal" in term_types:
            self.view.decimal_option.setChecked(True)
            self.decimal_ctrl.set_current_model(self.current_model["terms"]["Decimal"])
            self.decimal_ctrl.load_to_view()
            self.decimal_ctrl.view.show()
        else:
            self.view.decimal_option.setChecked(False)
            self.decimal_ctrl.view.hide()

    def update_model(self):
        new_model = {"terms": {}, "operators": []}
        for i in self.view.get_op_checks():
            if i.checkState() == 2:
                new_model["operators"].append(i.text())

        if self.view.integer_option.checkState() == 2:
            new_model["terms"]["Integer"] = self.integer_ctrl.current_model
            self.integer_ctrl.display_state = None

        if self.view.fraction_option.checkState() == 2:
            new_model["terms"]["Fraction"] = {"Numerator": {"Integer": self.numerator_ctrl.current_model}}
            new_model["terms"]["Fraction"]["Denominator"] = {"Integer": self.denominator_ctrl.current_model}
            self.numerator_ctrl.display_state = None
            self.denominator_ctrl.display_state = None

        if self.view.decimal_option.checkState() == 2:
            new_model["terms"]["Decimal"] = self.decimal_ctrl.current_model
            self.decimal_ctrl.display_state = None
            for i in new_model["terms"]["Decimal"]:
                i["precision"] = 3
        self.current_model = new_model
