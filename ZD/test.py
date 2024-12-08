from unittest import TestCase
from unittest.mock import patch

from action import AddAction


class TestAddAction(TestCase):

    def test_add_action(self):
        add = AddAction()
        self.assertEqual(add.cur_state, add.pending)
        add.start()
        self.assertEqual(add.cur_state, add.pending)

        with self.assertRaises(TypeError):
            add.start_machine()
        self.assertEqual(add.cur_state, add.pending)

        with patch("action.AddAction.on_start", returned_value=True):
            add = AddAction()
            add.start()
            self.assertEqual(add.cur_state, add.cloud_running)

    def test_move_next(self):
        add = AddAction()
        self.assertEqual(add.cur_state, add.pending)
        add.move_next()
        self.assertEqual(add.cur_state, add.pending)
        with patch("action.AddAction.on_start", returned_value=True):
            add = AddAction()
            add.move_next()
            self.assertEqual(add.cur_state, add.final)
