class IntegerSelectionManager:
    STREAK_MIN = 10

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

    def reset(self):
        self.clear_connections()
        self.current_model = None
        self.display_state = None
        self.view.clear_list()

    def clear_connections(self):
        """
        Don't use a null check on current model here. If a default display state is loaded and then hidden without a
        model being created, a null check would prevent the connections from being cleared leading to a recursive stack
        overflow with capture_range_changes and load_to_view.
        """
        try:
            self.view.display_state_test.disconnect()
            self.view.min_val.disconnect()
            self.view.max_val.disconnect()
            self.view.save_button.disconnect()
            self.view.reset_button.disconnect()
        except TypeError:
            pass

    def configure_buttons(self):
        self.view.display_state_test.clicked.connect(self.test_print)
        self.view.max_val.valueChanged.connect(self.set_min_max)
        self.view.min_val.valueChanged.connect(self.set_max_min)
        self.view.save_button.clicked.connect(self.save_selection_changes)
        self.view.reset_button.clicked.connect(self.reset_selection_changes)
        self.view.max_val.valueChanged.connect(self.capture_range_changes)
        self.view.min_val.valueChanged.connect(self.capture_range_changes)

    def test_print(self):
        self.capture_display_state()
        print(self.display_state)

    def set_min_max(self):
        self.view.min_val.setMaximum(self.view.max_val.value())

    def capture_range_changes(self):
        self.capture_display_state()
        self.load_to_view()

    def set_max_min(self):
        self.view.max_val.setMinimum(self.view.min_val.value())

    def save_selection_changes(self):
        self.capture_display_state()
        # a valid model cannot be generated if no values are selected by the user.
        if len(self.display_state["checked"]) != 0:
            self.update_model()
            self.display_state = None
        self.load_to_view()

    def reset_selection_changes(self):
        self.display_state = None
        if self.current_model is None:
            self.load_default_view()
        else:
            self.load_to_view()

    """
    This loads the view for a special case where no model for the integer selection exists. This happens when
     a user has turned on a new element type for an element group.
     """
    def load_default_view(self):
        self.display_state = {"low": 0, "high": 10, "checked": []}
        self.load_to_view()

    def load_to_view(self):
        if self.current_model is None and self.display_state is None:
            return
        self.clear_connections()
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
        self.view.min_val.setValue(low)
        self.view.max_val.setValue(high)
        self.configure_buttons()

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
        if self.display_state is None:
            return

        discontinuous = {"range": False, "vals": []}

        val_count = len(self.display_state["checked"])

        # prevents a model with no vals being captured just in case a parent calls this method directly and not through
        # self.save_selection_changes()
        if val_count == 0:
            return

        # model format "optimization" algorithm is unnecessary for small user selection of values
        if val_count <= self.STREAK_MIN:
            discontinuous["vals"] = self.display_state["checked"]
            self.current_model = [discontinuous]
            return

        continuous = []

        last_val = self.display_state["checked"][0]
        batch = [last_val]
        streak = 1
        i = 1
        while i < val_count:
            if self.display_state["checked"][i] - last_val == 1:
                streak += 1
                if streak < self.STREAK_MIN:
                    batch.append(self.display_state["checked"][i])
            else:
                if streak == 1:
                    discontinuous["vals"].append(last_val)

                elif streak < self.STREAK_MIN:
                    discontinuous["vals"] += batch

                else:
                    continuous.append({"range": True, "vals": [batch[0], batch[0] + streak - 1]})

                # reset tracking vars to default states
                streak = 1

                '''
                if another streak set cannot be formed before the loop terminates, 
                exit loop where all remaining vals are appended
                '''
                if i >= val_count - self.STREAK_MIN:
                    break

                batch = [self.display_state["checked"][i]]

            last_val = self.display_state["checked"][i]
            i += 1

        """
        Handle remaining checked vals or streak information when loop terminates
        """
        if streak <= self.STREAK_MIN:
            discontinuous["vals"] += self.display_state["checked"][i:]
        else:
            continuous.append({"range": True, "vals": [batch[0], batch[0] + streak - 1]})

        # handle continuous selections larger than STREAK_MIN with no discontinuous vals
        if len(discontinuous["vals"]) != 0:
            continuous.append(discontinuous)
        self.current_model = continuous
        self.display_state = None
