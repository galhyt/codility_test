from unittest import TestCase

from actions import AddAction, RemoveAction


class TestAddAction(TestCase):

    def test_add_action(self):
        add = AddAction()
        self.assertEqual(add.cur_state, add.pending)
        add.start()
        self.assertEqual(add.cur_state, add.pending)

        with self.assertRaises(TypeError):
            add.start_machine()
        self.assertEqual(add.cur_state, add.pending)

        add = AddAction()
        add.start_signal = True
        add.start()
        self.assertEqual(add.cur_state, add.cloud_running)

    def test_move_next(self):
        add = AddAction()
        self.assertEqual(add.cur_state, add.pending)
        add.move_next()
        self.assertEqual(add.cur_state, add.pending)

        add = AddAction()
        add.start_signal = True
        add.move_next()
        self.assertEqual(add.cur_state, add.final)

    def test_action_type(self):
        remove = RemoveAction()
        self.assertEqual(remove.type, "remove_action")

    def test_actions_not_overlapp(self):
        add1, add2 = AddAction(), AddAction()
        add1.start_signal = True
        add1.start()
        self.assertEqual(add1.cur_state, add1.cloud_running)
        self.assertEqual(add2.cur_state, add2.pending)
