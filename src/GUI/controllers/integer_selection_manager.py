class IntegerSelectionManager:
    def __init__(self, view):
        self.view = view
        self.current_model = None

    def set_current_model(self, model):
        self.current_model = model
        self.configure_buttons()
        self.load_to_view()

    def configure_buttons(self):
        pass

    def load_to_view(self):
        if self.current_model is None:
            return