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
        self.view.multiple_type_option.stateChanged.connect(self.switch_term_list)
        self.view.multiple_op_option.stateChanged.connect(self.switch_op_list)

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

        multi_term_types = len(self.current_model.term_sets[0]) > 1 or len(self.current_model.term_sets) > 1
        self.view.multiple_type_option.setChecked(multi_term_types)

        if multi_term_types:
            self.view.term_radio.hide()
            for i in self.view.get_term_checks():
                for j in self.current_model.term_sets:
                    if i.text() in j:
                        i.setChecked(True)
        else:
            self.view.term_check.hide()
            for i in self.view.get_term_radios():
                if i.text() in self.current_model.term_sets[0]:
                    i.setChecked(True)

        multi_op_types = len(self.current_model.operator_sets[0]) > 1 or len(self.current_model.operator_sets) > 1
        self.view.multiple_op_option.setChecked(multi_op_types)

        if multi_op_types:
            self.view.op_radio.hide()
            for i in self.view.get_op_checks():
                for j in self.current_model.operator_sets:
                    if i.text() in j:
                        i.setChecked(True)
        else:
            self.view.op_check.hide()
            for i in self.view.get_op_radios():
                if i.text() in self.current_model.operator_sets[0]:
                    i.setChecked(True)

    def update_model(self):
        pass

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

            self.view.term_count_max.disconnect()
            self.view.term_count_min.disconnect()

    def min_changed(self):
        self.view.term_count_max.setMinimum(self.view.term_count_min.value())

    def max_changed(self):
        self.view.term_count_min.setMaximum(self.view.term_count_max.value())

    def switch_term_list(self):
        if self.view.multiple_type_option.isChecked():
            self.view.term_check.show()
            self.view.term_radio.hide()
        else:
            self.view.term_radio.show()
            self.view.term_check.hide()

    def switch_op_list(self):
        if self.view.multiple_op_option.isChecked():
            self.view.op_check.show()
            self.view.op_radio.hide()
        else:
            self.view.op_radio.show()
            self.view.op_check.hide()
