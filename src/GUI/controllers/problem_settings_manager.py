from PyQt5 import QtWidgets, QtCore
from src.GUI.controllers.problem_element_manager import ProblemElementManager


class ProblemSettingsManager:
    MIN_TERMS = 2
    MAX_TERMS = 10

    def __init__(self, view, sheet_display):
        self.view = view
        self.sheet_display = sheet_display
        self.problem_element_ctrl = ProblemElementManager(self.view.problem_element_selection)
        self.current_model = None

    def set_current_model(self, model):
        self.clear_connections()
        self.clear_view()
        self.current_model = model
        self.load_term_display_state()
        self.configure_element_list()
        self.load_to_view()
        self.configure_buttons()

    def configure_buttons(self):
        self.view.variable_term_count.stateChanged.connect(self.switch_term_count_state)
        self.view.problem_elements.itemSelectionChanged.connect(self.load_term_display_state)
        self.view.add_button.clicked.connect(self.add_element)
        self.view.del_button.clicked.connect(self.del_element)

    def clear_connections(self):
        try:
            self.view.variable_term_count.disconnect()
            self.view.problem_elements.disconnect()
            self.view.add_button.disconnect()
            self.view.del_button.disconnect()
        except TypeError:
            pass

    def clear_view(self):
        self.problem_element_ctrl.clear_view()
        self.view.problem_elements.clear()

    def add_element(self):
        self.view.add_problem_element_item("Element Group {}".format(self.view.problem_elements.count() + 1))
        self.current_model.problem_elements.append({"terms": {}, "operators": []})

    def del_element(self):
        self.clear_connections()
        self.problem_element_ctrl.clear_view()

        selected = self.view.problem_elements.currentRow()
        self.view.remove_selected_element_item(selected)
        self.current_model.problem_elements.pop(selected)

        new_row = self.view.problem_elements.currentRow()
        self.problem_element_ctrl.set_current_model(self.current_model.problem_elements[new_row], new_row)
        self.configure_buttons()

    def configure_element_list(self):
        self.view.problem_elements.clear()

        term_count = len(self.current_model.ordered_terms)

        for i in range(term_count):
            term_widget = QtWidgets.QTreeWidgetItem(self.view.problem_elements)
            term_widget.setText(0, "Term {}".format(i + 1))
            for j in range(len(self.current_model.ordered_terms[i])):
                term_setting = QtWidgets.QTreeWidgetItem(term_widget)
                term_setting.setText(0, "Term Group {}".format(j + 1))
            if i < term_count - 1:
                operator_widget = QtWidgets.QTreeWidgetItem(self.view.problem_elements)
                operator_widget.setText(0, "Operator {}".format(i + 1))
                for k in range(len(self.current_model.ordered_operators[i])):
                    operator_setting = QtWidgets.QTreeWidgetItem(operator_widget)
                    operator_setting.setText(0, "Operator Group {}".format(k + 1))

        self.view.problem_elements.setCurrentItem(term_widget)

    def load_term_display_state(self):
        if self.problem_element_ctrl.current_model is not None:
            self.problem_element_ctrl.update_model()
            self.current_model.problem_elements[self.problem_element_ctrl.model_row] = self.problem_element_ctrl.current_model

        try:
            parent = self.view.problem_elements.currentItem().parent()
            parent_row = self.view.problem_elements.indexOfTopLevelItem(parent)
            selected_item_row = self.view.problem_elements.selectionModel().selectedIndexes()[0].row()
            print(selected_item_row, parent_row)
        except IndexError as e:
            row = self.view.problem_elements.indexOfTopLevelItem(self.view.problem_elements.currentItem())
            print(e)
        except AttributeError as e:
            row = self.view.problem_elements.indexOfTopLevelItem(self.view.problem_elements.currentItem())
            print(e)

        selected_element = self.current_model.problem_elements[row]
        self.problem_element_ctrl.set_current_model(selected_element, row)

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
        self.problem_element_ctrl.update_model()
        self.current_model.problem_elements[self.problem_element_ctrl.model_row] = self.problem_element_ctrl.current_model

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
