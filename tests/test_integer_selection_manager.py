import unittest
import sys
from src.GUI.controllers.integer_selection_manager import IntegerSelectionManager
"""This is almost certainly a bad way to do unit testing, but it's the only way I've been bothered
   to try and it seems to work"""


class IntegerSelectionManagerTest(unittest.TestCase):

    def setUp(self):
        self.ism = IntegerSelectionManager("test")

    def test_update_model(self):
        test_cases = []
        test_cases.append(self.create_single_val_case())
        test_cases.append(self.create_two_con_val_case())
        test_cases.append(self.create_two_discon_val_case())
        test_cases.append(self.create_streak_min_con_val_case())
        test_cases.append(self.create_one_greater_than_streak_min_discon_val_case())
        test_cases.append(self.create_one_greater_than_streak_min_con_val_case())
        test_cases.append(self.create_single_discon_then_streak())
        test_cases.append(self.create_multi_discon_then_streak())
        test_cases.append(self.create_streak_discon_streak())
        test_cases.append(self.create_discon_streak_discon())
        test_cases.append(self.create_double_batch_discon())

        print("\nThe final printed is the case that failed\n")
        for i in test_cases:
            print("\n" + i["name"])
            self.ism.current_model = None
            self.ism.display_state = i["display_state"]
            self.ism.update_model()
            size = 0
            for j in self.ism.current_model:
                size += sys.getsizeof(j["vals"])
            print(self.ism.current_model)
            print(size)
            self.assertEqual(i["expected_model"], self.ism.current_model)

    def create_test_case(self, name, state, model):
        case = {}
        case["name"] = name
        case["display_state"] = state
        case["expected_model"] = model
        return case

    def create_single_val_case(self):
        name = "single val"
        state = {"checked": [1]}
        model = [{"range": False, "vals": [1]}]
        return self.create_test_case(name, state, model)

    def create_two_con_val_case(self):
        name = "two continuous values"
        state = {"checked": [1, 2]}
        model = [{"range": False, "vals": [1, 2]}]
        return self.create_test_case(name, state, model)

    def create_two_discon_val_case(self):
        name = "two discontinuous values"
        state = {"checked": [1, 3]}
        model = [{"range": False, "vals": [1, 3]}]
        return self.create_test_case(name, state, model)

    def create_streak_min_con_val_case(self):
        name = "streak min continuous"
        start = 1
        vals = list(range(start, self.ism.STREAK_MIN + 1))
        state = {"checked": vals}
        model = [{"range": False, "vals": vals}]
        return self.create_test_case(name, state, model)

    def create_one_greater_than_streak_min_discon_val_case(self):
        name = "One val more than streak min discontinuous"
        start = 1
        vals = list(range(start, self.ism.STREAK_MIN))
        vals.append(13)
        vals.append(14)
        state = {"checked": vals}
        model = [{"range": False, "vals": vals}]
        return self.create_test_case(name, state, model)

    def create_one_greater_than_streak_min_con_val_case(self):
        name = "One val more than streak min continuous"
        start = 1
        vals = list(range(start, self.ism.STREAK_MIN + start + 1))
        state = {"checked": vals}
        model = [{"range": True, "vals": [1, 11]}]
        return self.create_test_case(name, state, model)

    def create_single_discon_then_streak(self):
        name = "single discon then streak"
        vals = [-1]
        start = 1
        vals += list(range(start, self.ism.STREAK_MIN + start + 1))
        state = {"checked": vals}
        model = [{"range": True, "vals": [1, 11]}, {"range": False, "vals": [-1]}]
        return self.create_test_case(name, state, model)

    def create_multi_discon_then_streak(self):
        name = "multi discon then streak"
        vals = [-5, -2, -1]
        start = 1
        vals += list(range(start, self.ism.STREAK_MIN + start + 1))
        state = {"checked": vals}
        model = [{"range": True, "vals": [1, 11]}, {"range": False, "vals": [-5, -2, -1]}]
        return self.create_test_case(name, state, model)

    def create_streak_discon_streak(self):
        name = "streak, multi discon, streak"
        start = -20
        vals = list(range(start, self.ism.STREAK_MIN + start + 1))
        vals += [-5, -2, -1]
        start1 = 1
        vals += list(range(start1, self.ism.STREAK_MIN + start1 + 1))
        state = {"checked": vals}
        model = [{"range": True, "vals": [-20, -10]}, {"range": True, "vals": [1, 11]}, {"range": False, "vals": [-5, -2, -1]}]
        return self.create_test_case(name, state, model)

    def create_discon_streak_discon(self):
        name = "discon, streak, discon"
        vals = [1, 2, 3, 4, 7]
        start = 9
        vals += list(range(start, self.ism.STREAK_MIN + start + 5))
        vals += [25, 26, 28, 31, 32, 33, 34, 35]
        state = {"checked": vals}
        model = [{"range": True, "vals": [9, 23]}, {"range": False, "vals": [1, 2, 3, 4, 7, 25, 26, 28, 31, 32, 33, 34, 35]}]
        return self.create_test_case(name, state, model)

    def create_double_batch_discon(self):
        name = "double_batch_discon"
        start = 1
        vals = list(range(start, 2 * (self.ism.STREAK_MIN + start + 6), 2))
        state = {"checked": vals}
        model = [{"range": False, "vals": vals}]
        return self.create_test_case(name, state, model)