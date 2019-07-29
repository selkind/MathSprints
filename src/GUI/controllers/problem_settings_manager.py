from PyQt5 import QtWidgets, QtCore
import logging
from src.GUI.controllers.problem_element_manager import ProblemElementManager


class ProblemSettingsManager:
    MIN_TERMS = 2
    MAX_TERMS = 10

    def __init__(self, view, sheet_display):
        self.view = view
        self.sheet_display = sheet_display
        self.problem_element_ctrl = ProblemElementManager(self.view.problem_element_selection)
        self.current_model = None
        logging.basicConfig(filename="log.txt", level=logging.DEBUG)

    def set_current_model(self, model):
        self.clear_connections()
        self.clear_view()
        self.current_model = model
        self.load_term_display_state()
        self.configure_element_list()
        self.load_to_view()
        self.toggle_tree_mod_buttons()
        self.toggle_variable_term_count()
        self.configure_buttons()

    def configure_buttons(self):
        self.view.ordered_term_check.stateChanged.connect(self.toggle_variable_term_count)
        self.view.variable_term_count.stateChanged.connect(self.switch_term_count_state)
        self.view.problem_elements.itemSelectionChanged.connect(self.load_term_display_state)
        self.view.problem_elements.itemSelectionChanged.connect(self.toggle_tree_mod_buttons)
        self.view.add_button.clicked.connect(self.add_element)
        self.view.del_button.clicked.connect(self.del_element)
        self.problem_element_ctrl.view.element_save.clicked.connect(self.update_problem_elements_model)

    def clear_connections(self):
        try:
            self.view.ordered_term_check.disconnect()
            self.view.variable_term_count.disconnect()
            self.view.problem_elements.disconnect()
            self.view.add_button.disconnect()
            self.view.del_button.disconnect()
            self.problem_element_ctrl.view.element_save.disconnect()
        except TypeError as e:
            logging.log(logging.DEBUG, e)

    def clear_view(self):
        self.problem_element_ctrl.clear_view()
        self.view.problem_elements.clear()

    def add_element(self):
        # this line is necessary because adding elements changes the selection, so unsaved changes would be lost.
        self.update_problem_elements_model()
        # after updating the current model, set the problem_elements model to None to bypass the included model update
        # in self.load_term_display_state(). This should probably be pulled out into a separate method to conform to SRP
        self.problem_element_ctrl.current_model = None

        parent, selected_item_row = self.get_selection_coordinates()
        if parent == -1:
            parent = selected_item_row
            selected_item_row = -1

        if parent % 2 == 0:
            self.current_model.ordered_terms[(parent // 2)].append({})
        else:
            self.current_model.ordered_operators[(parent - 1) // 2].append([])

        # clearing connections here because configure element list changes the selection and we're manually changing
        # the selection below. This avoids triggering self.load_term_display_state
        self.clear_connections()
        self.configure_element_list()

        receiving_parent_item = self.view.problem_elements.topLevelItem(parent)
        try:
            added_child = receiving_parent_item.child(selected_item_row + 1)
            self.view.problem_elements.setCurrentItem(added_child)
        except AttributeError as e:
            logging.log(logging.DEBUG, str(e) + "problem selecting child at coordinates {}, {}".format(parent,
                                                                                            selected_item_row + 1))
        self.load_term_display_state()

        self.configure_buttons()

    def del_element(self):
        self.clear_connections()
        self.problem_element_ctrl.current_model = None

        parent, selected_item_row = self.get_selection_coordinates()

        if parent % 2 == 0:
            self.current_model.ordered_terms[parent // 2].pop(selected_item_row)
        else:
            self.current_model.ordered_operators[(parent - 1) // 2].pop(selected_item_row)

        self.configure_element_list()

        item_losing_parent = self.view.problem_elements.topLevelItem(parent)
        next_remaining_child = item_losing_parent.child(selected_item_row - 1)
        self.view.problem_elements.setCurrentItem(next_remaining_child)
        try:
            self.load_term_display_state()
        except IndexError as e:
            logging.log(logging.DEBUG, str(e) + " no element groups remained in the topLevelItem")

            empty_parent = self.view.problem_elements.topLevelItem(parent)
            self.view.problem_elements.setCurrentItem(empty_parent)
            self.load_term_display_state()

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
        try:
            self.view.problem_elements.setCurrentItem(term_setting)
        except NameError as e:
            logging.log(logging.DEBUG, str(e) + " while attempting to set current item of "
                                           "problem_setting_display.problem elements. The last term has no "
                                           "term setting groups in the model")

    def load_term_display_state(self):
        if self.problem_element_ctrl.current_model is not None:
            self.update_problem_elements_model()

        parent_row, selected_item_row = self.get_selection_coordinates()

        if parent_row == -1:
            self.problem_element_ctrl.clear_view()
            return
        elif parent_row % 2 == 0:
            selected_element = self.current_model.ordered_terms[parent_row // 2][selected_item_row]
        else:
            selected_element = self.current_model.ordered_operators[(parent_row - 1) // 2][selected_item_row]

        try:
            self.problem_element_ctrl.set_current_model(selected_element, (parent_row, selected_item_row))
        except AttributeError as e:
            logging.debug(str(e) + " problem_settings model: {}\n selection coordinates: {}, {}".format(
                                                                                                    self.current_model,
                                                                                                    parent_row,
                                                                                                    selected_item_row))

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

        self.update_problem_elements_model()

    def update_problem_elements_model(self):
        self.problem_element_ctrl.update_model()
        parent_row, setting_row = self.problem_element_ctrl.model_row
        try:
            if parent_row % 2 == 0:
                self.current_model.ordered_terms[parent_row // 2][setting_row] = self.problem_element_ctrl.current_model
            else:
                self.current_model.ordered_operators[(parent_row - 1) // 2][setting_row] = self.problem_element_ctrl.current_model
        except IndexError as e:
            logging.log(logging.DEBUG, str(e) + " Tried to update problem element model when topLevelItem was selected")

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

    def toggle_tree_mod_buttons(self):
        parent_selected = self.get_selection_coordinates()[0] == -1
        self.view.add_button.setEnabled(parent_selected)
        self.view.del_button.setEnabled(not parent_selected)

    def toggle_variable_term_count(self):
        self.view.variable_term_count.setChecked(False)
        self.view.variable_term_count.setEnabled(not self.view.ordered_term_check.isChecked())

    def min_changed(self):
        self.view.term_count_max.setMinimum(self.view.term_count_min.value())

    def max_changed(self):
        self.view.term_count_min.setMaximum(self.view.term_count_max.value())

    def get_selection_coordinates(self):
        parent_row = None
        selected_item_row = None

        try:
            parent = self.view.problem_elements.currentItem().parent()
            parent_row = self.view.problem_elements.indexOfTopLevelItem(parent)
            selected_item_row = self.view.problem_elements.selectionModel().selectedIndexes()[0].row()
        except IndexError as e:
            logging.log(logging.DEBUG, e)
        except AttributeError as e:
            logging.log(logging.DEBUG, e)

        # if nothing is selected, select the last setting from the last term to load into the view
        if parent_row is None:
            # I know this looks dumb, but having the parent row is important so that the correct indices
            # are used to update the model in the first iteration.
            parent_row = (len(self.current_model.ordered_terms) - 1) * 2
            selected_item_row = len(self.current_model.ordered_terms[parent_row // 2]) - 1
            logging.log(logging.DEBUG, "selection coordinates set to: {}, {}".format(parent_row, selected_item_row))

        return parent_row, selected_item_row
