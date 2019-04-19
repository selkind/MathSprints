class ProblemSettingsManager:
    MIN_TERMS = 2
    MAX_TERMS = 10

    def __init__(self, view, sheet_display):
        self.view = view
        self.sheet_display = sheet_display
        self.current_model = None

    def set_current_model(self, model):
        self.current_model = model
        self.configure_buttons()
        self.load_to_view()

    def configure_buttons(self):
        self.view.variable_term_count.stateChanged.connect(self.switch_term_count_state)

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

        for i in self.view.get_term_checks():
            for j in self.current_model.term_sets:
                if i.text() in j:
                    i.setChecked(True)
                else:
                    i.setChecked(False)

        for i in self.view.get_op_checks():
            for j in self.current_model.operator_sets:
                if i.text() in j:
                    i.setChecked(True)
                else:
                    i.setChecked(False)

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
