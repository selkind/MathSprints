class IntegerSelectionManager:
    def __init__(self, view):
        self.view = view
        self.current_model = None

    def set_current_model(self, model):
        self.view.clear_list()
        self.clear_connections()
        self.current_model = model
        self.load_to_view()
        self.configure_buttons()

    def clear_connections(self):
        if self.current_model is None:
            return
        self.view.min_val.disconnect()
        self.view.max_val.disconnect()

    def configure_buttons(self):
        self.view.min_val.valueChanged.connect(self.set_min_max)
        self.view.max_val.valueChanged.connect(self.set_max_min)

    def set_min_max(self):
        self.view.min_val.setMaximum(self.view.max_val.Value() - 1)

    def set_max_min(self):
        self.view.max_val.setMinimum(self.view.min_val.Value() + 1)

    def load_to_view(self):
        if self.current_model is None:
            return
        self.view.clear_list()

        checked = []
        for i in self.current_model:
            if i["range"]:
                checked += list(range(i["vals"][0], i["vals"][1] + 1))
            else:
                checked += i["vals"]
        checked.sort()
        self.view.populate_list(checked)

        self.view.min_val.setValue(checked[0])
        self.view.max_val.setValue(checked[-1])
