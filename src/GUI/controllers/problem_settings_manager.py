from src.GUI.controllers.integer_selection_manager import IntegerSelectionManager


class ProblemSettingsManager:
    MIN_TERMS = 2
    MAX_TERMS = 10

    def __init__(self, view, sheet_display):
        self.view = view
        self.integer_ctrl = IntegerSelectionManager(self.view.integer_selection)
        self.decimal_ctrl = IntegerSelectionManager(self.view.decimal_selection)
        self.numerator_ctrl = IntegerSelectionManager(self.view.numerator_selection)
        self.denominator_ctrl = IntegerSelectionManager(self.view.denominator_selection)
        self.sheet_display = sheet_display
        self.current_model = None

    def set_current_model(self, model):
        self.current_model = model
        self.configure_buttons()
        self.configure_element_list()
        self.load_to_view()

    def configure_buttons(self):
        self.view.variable_term_count.stateChanged.connect(self.switch_term_count_state)
        self.view.problem_elements.itemSelectionChanged.connect(self.load_term_display_state)

    def configure_element_list(self):
        self.view.problem_elements.clear()
        for i in range(len(self.current_model.problem_elements)):
            self.view.add_problem_element_item("Element Group {}".format(i + 1))
        self.view.problem_elements.setCurrentRow(self.view.problem_elements.count() - 1)

    def load_term_display_state(self):
        row = self.view.problem_elements.currentRow()
        selected_element = self.current_model.problem_elements[row]
        self.load_operators(selected_element["operators"])
        self.load_terms(selected_element["terms"])

    def load_operators(self, model_operators):
        for i in self.view.get_op_checks():
            if i.text() in model_operators:
                i.setChecked(True)
            else:
                i.setChecked(False)

    def load_terms(self, model_terms):
        term_types = model_terms.keys()
        if "Integer" in term_types:
            self.view.integer_option.setChecked(True)
            self.integer_ctrl.set_current_model(model_terms["Integer"])
            self.integer_ctrl.load_to_view()
        if "Fraction" in term_types:
            self.view.fraction_option.setChecked(True)
            self.numerator_ctrl.set_current_model(model_terms["Fraction"]["Numerator"]["Integer"])
            self.denominator_ctrl.set_current_model(model_terms["Fraction"]["Numerator"]["Integer"])
            self.numerator_ctrl.load_to_view()
            self.denominator_ctrl.load_to_view()
        if "Decimal" in term_types:
            self.view.decimal_option.setChecked(True)
            self.decimal_ctrl.set_current_model(model_terms["Decimal"])
            self.decimal_ctrl.load_to_view()

    def load_to_view(self):
        if self.current_model is None:
            return
        self.view.variable_term_count.setChecked(self.current_model.variable_term_count)
        self.view.term_count_min.setValue(self.current_model.term_count_min)
        self.view.term_count_min.setMinimum(self.MIN_TERMS)
        self.view.term_count_min.setMaximum(self.current_model.term_count_max)

        self.view.term_count_max.setMinimum(self.current_model.term_count_min)
        self.view.term_count_max.setMaximum(self.MAX_TERMS)

        self.switch_term_count_state()
        self.view.term_count_max.setValue(self.current_model.term_count_max)


    def update_model(self):
        self.current_model.variable_term_count = self.view.variable_term_count.isChecked()
        if self.current_model.variable_term_count:
            self.current_model.term_count_min = self.view.term_count_min.value()
            self.current_model.term_count_max = self.view.term_count_max.value()
        else:
            self.current_model.term_count_min = self.view.term_count_min.value()
            self.current_model.term_count_max = self.current_model.term_count_min

        self.current_model.term_sets = []
        for i in self.view.get_term_checks():
            if i.isChecked():
                self.current_model.term_sets.append([i.text()])

        self.current_model.operator_sets = []
        for i in self.view.get_op_checks():
            if i.isChecked():
                self.current_model.operator_sets.append([i.text()])

    def switch_term_count_state(self):
        if self.view.variable_term_count.isChecked():
            self.view.term_count_label_min.show()
            self.view.term_count_label_max.show()

            self.view.term_count_max.show()
            self.view.term_count_max.setValue(self.view.term_count_min.value())
            self.view.term_count_max.setMinimum(self.view.term_count_min.value())

            self.view.term_count_max.valueChanged.connect(self.max_changed)
            self.view.term_count_min.valueChanged.connect(self.min_changed)
        else:
            self.view.term_count_label_min.hide()
            self.view.term_count_label_max.hide()
            self.view.term_count_max.hide()

            self.view.term_count_min.setMaximum(self.MAX_TERMS)

            if self.view.term_count_max.receivers(self.view.term_count_max.valueChanged) > 0:
                self.view.term_count_max.disconnect()
            if self.view.term_count_min.receivers(self.view.term_count_min.valueChanged) > 0:
                self.view.term_count_min.disconnect()

    def min_changed(self):
        self.view.term_count_max.setMinimum(self.view.term_count_min.value())

    def max_changed(self):
        self.view.term_count_min.setMaximum(self.view.term_count_max.value())
