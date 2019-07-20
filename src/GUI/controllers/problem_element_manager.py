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

        if self.model_row[0] % 2 == 0:
            self.load_terms()
            self.show_term_selection()

        else:
            for i in self.view.get_op_checks():
                if i.text() in self.current_model:
                    i.setChecked(True)
            self.view.op_check.show()

    def configure_buttons(self):
        self.view.integer_option.stateChanged.connect(lambda: self.toggle_visibility(
                                                        self.view.integer_option,
                                                        self.integer_ctrl))

        self.view.fraction_option.stateChanged.connect(lambda: self.toggle_visibility(
                                                        self.view.fraction_option,
                                                        self.numerator_ctrl))

        self.view.fraction_option.stateChanged.connect(lambda: self.toggle_visibility(
                                                        self.view.fraction_option,
                                                        self.denominator_ctrl))

        self.view.decimal_option.stateChanged.connect(lambda: self.toggle_visibility(
                                                        self.view.decimal_option,
                                                        self.decimal_ctrl))

        self.view.element_save.clicked.connect(self.update_model)

    def clear_connections(self):
        try:
            self.view.element_save.disconnect()
            self.view.integer_option.disconnect()
            self.view.fraction_option.disconnect()
            self.view.decimal_option.disconnect()
        except TypeError:
            pass

    """
    This method only changes the visibility state of the integer selection displays to match the check state
    of the element option checkbox. It does not need to handle any updates to the integer selection model.
    When updating the entire element selection model, the check state determines whether or not to include
    the integer selection model.
    """

    def toggle_visibility(self, check_widget, integer_selection_widget):
        if check_widget.checkState() == 2:
            if integer_selection_widget.current_model is None:
                integer_selection_widget.load_default_view()
            integer_selection_widget.view.show()

        else:
            integer_selection_widget.view.hide()

    def clear_view(self):
        self.view.clear_op_checks()
        self.view.op_check.hide()

        self.view.integer_option.setChecked(False)
        self.view.fraction_option.setChecked(False)
        self.view.decimal_option.setChecked(False)

        self.integer_ctrl.reset()
        self.numerator_ctrl.reset()
        self.denominator_ctrl.reset()
        self.decimal_ctrl.reset()
        self.hide_term_selection()

    def hide_term_selection(self):
        self.view.integer_option.hide()
        self.integer_ctrl.view.hide()
        self.view.fraction_option.hide()
        self.numerator_ctrl.view.hide()
        self.denominator_ctrl.view.hide()
        self.view.decimal_option.hide()
        self.decimal_ctrl.view.hide()

    def show_term_selection(self):
        self.view.integer_option.show()
        self.view.fraction_option.show()
        self.view.decimal_option.show()

        self.toggle_visibility(self.view.integer_option, self.integer_ctrl)
        self.toggle_visibility(self.view.decimal_option, self.decimal_ctrl)
        self.toggle_visibility(self.view.fraction_option, self.numerator_ctrl)
        self.toggle_visibility(self.view.fraction_option, self.denominator_ctrl)

    def load_terms(self):
        term_types = self.current_model.keys()
        if "Integer" in term_types:
            self.view.integer_option.setChecked(True)
            self.integer_ctrl.set_current_model(self.current_model["Integer"])
            self.integer_ctrl.load_to_view()
            self.integer_ctrl.view.show()
        else:
            self.view.integer_option.setChecked(False)
            self.integer_ctrl.view.hide()

        if "Fraction" in term_types:
            self.view.fraction_option.setChecked(True)
            self.numerator_ctrl.set_current_model(self.current_model["Fraction"]["Numerator"]["Integer"])
            self.numerator_ctrl.load_to_view()
            self.denominator_ctrl.set_current_model(self.current_model["Fraction"]["Denominator"]["Integer"])
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
            self.decimal_ctrl.set_current_model(self.current_model["Decimal"])
            self.decimal_ctrl.load_to_view()
            self.decimal_ctrl.view.show()
        else:
            self.view.decimal_option.setChecked(False)
            self.decimal_ctrl.view.hide()

    def update_model(self):
        if self.model_row[0] % 2 != 0:
            new_model = []
            for i in self.view.get_op_checks():
                if i.checkState() == 2:
                    new_model.append(i.text())

        # The null checks are necessary in the case that a user checks an option box but does not select any values.
        else:
            new_model = {}
            if self.view.integer_option.checkState() == 2 and (self.integer_ctrl.current_model is not None
                                                               or self.integer_ctrl.display_state is not None):
                self.integer_ctrl.save_selection_changes()
                # If save_selection_changes detects that no values are selected, display_state is not set to None.
                # this honestly isn't a great solution from a best practice perspective.
                if self.integer_ctrl.display_state is None:
                    new_model["Integer"] = self.integer_ctrl.current_model
                self.integer_ctrl.load_to_view()

            if (self.view.fraction_option.checkState() == 2 and (self.numerator_ctrl.current_model is not None
                                                                 or self.numerator_ctrl.display_state is not None)
                    and (self.denominator_ctrl.current_model is not None or self.denominator_ctrl.display_state is not None)):
                self.numerator_ctrl.save_selection_changes()
                self.denominator_ctrl.save_selection_changes()
                if self.numerator_ctrl.display_state is None and self.denominator_ctrl.display_state is None:
                    new_model["Fraction"] = {"Numerator": {"Integer": self.numerator_ctrl.current_model},
                                             "Denominator": {"Integer": self.denominator_ctrl.current_model}}
                self.numerator_ctrl.load_to_view()
                self.denominator_ctrl.load_to_view()

            if self.view.decimal_option.checkState() == 2 and (self.decimal_ctrl.current_model is not None
                                                               or self.decimal_ctrl.display_state is not None):
                self.decimal_ctrl.save_selection_changes()
                if self.decimal_ctrl.display_state is None:
                    new_model["Decimal"] = self.decimal_ctrl.current_model
                    for i in new_model["Decimal"]:
                        i["precision"] = 3
                self.decimal_ctrl.load_to_view()

        if new_model == {} or new_model == []:
            self.current_model = None

        self.current_model = new_model

