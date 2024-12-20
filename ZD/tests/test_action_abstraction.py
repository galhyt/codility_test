from unittest import TestCase
from unittest.mock import patch

from actions.action import Action


class TestActionAbstraction(TestCase):

    def test_add_action(self):
        add = Action("add_action")
        self.assertEqual(add.cur_state, add.pending)
        add.move_next()
        self.assertEqual(add.cur_state, add.pending)

        add = Action("add_action")
        add.start_signal = True
        add.move_next()
        self.assertEqual(add.cur_state, add.final)
