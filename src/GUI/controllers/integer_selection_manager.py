class IntegerSelectionManager:
    def __init__(self, view):
        self.view = view
        self.current_model = None
        self.display_state = None

    def capture_display_state(self):
        if self.display_state is None:
            self.display_state = {}

        self.display_state["low"] = self.view.min_val.value()
        self.display_state["high"] = self.view.max_val.value()

        self.display_state["checked"] = []
        for i in range(self.view.int_list.count()):
            item = self.view.int_list.item(i)
            val = int(item.text())
            if item.checkState() and (self.display_state["high"] >= val >= self.display_state["low"]):
                self.display_state["checked"].append(val)

    def set_current_model(self, model):
        self.clear_connections()
        self.current_model = model
        self.configure_buttons()
        self.load_to_view()

    def clear_connections(self):
        if self.current_model is None:
            return
        self.view.display_state_test.disconnect()
        self.view.min_val.disconnect()
        self.view.max_val.disconnect()

    def configure_buttons(self):
        self.view.display_state_test.clicked.connect(self.test_print)
        self.view.max_val.valueChanged.connect(self.set_min_max)
        self.view.min_val.valueChanged.connect(self.set_max_min)

    def test_print(self):
        self.capture_display_state()
        print(self.display_state)

    def set_min_max(self):
        self.view.min_val.setMaximum(self.view.max_val.value())

    def set_max_min(self):
        self.view.max_val.setMinimum(self.view.min_val.value())

    def load_to_view(self):
        if self.current_model is None:
            return
        self.view.clear_list()

        if self.display_state is None:
            checked = self.generate_model_checks()
            low = checked[0]
            high = checked[-1]
        else:
            checked = self.display_state["checked"]
            low = self.display_state["low"]
            high = self.display_state["high"]

        self.view.populate_list(low, high, checked)

        self.view.min_val.setValue(checked[0])
        self.view.max_val.setValue(checked[-1])

    def generate_model_checks(self):
        checked = []
        for i in self.current_model:
            if i["range"]:
                checked += list(range(i["vals"][0], i["vals"][1] + 1))
            else:
                checked += i["vals"]
        checked.sort()
        return checked

    def update_model(self):
        pass

