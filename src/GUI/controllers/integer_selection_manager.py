class IntegerSelectionManager:
    def __init__(self, view):
        self.view = view
        self.current_model = None
        self.display_state = None

    def initialize_display_state(self):
        self.display_state = {}
        self.display_state["low"] = self.view.min_val.value()
        self.display_state["high"] = self.view.max_val.value()
        self.display_state["checked"] = []
        for i in range(self.view.int_list.count()):
            if self.view.int_list.item(i).checkState():
                self.display_state["checked"].append(self.view.int_list.item(i).text())

    def set_current_model(self, model):
        self.clear_connections()
        self.current_model = model
        self.configure_buttons()
        self.load_to_view()

    def clear_connections(self):
        if self.current_model is None:
            return
        self.display_state_test.disconnect()
        self.view.min_val.disconnect()
        self.view.max_val.disconnect()

    def configure_buttons(self):
        self.view.display_state_test.clicked.connect(self.test_print)
        self.view.max_val.valueChanged.connect(self.set_min_max)
        self.view.min_val.valueChanged.connect(self.set_max_min)

    def test_print(self):
        self.initialize_display_state()
        print(self.display_state)

    def set_min_max(self):
        self.view.min_val.setMaximum(self.view.max_val.value())

    def set_max_min(self):
        self.view.max_val.setMinimum(self.view.min_val.value())

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

    def update_model(self):
        pass

