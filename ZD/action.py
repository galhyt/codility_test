from abc import ABC, ABCMeta
from dataclasses import dataclass
from functools import partial
from typing import List, Callable


@dataclass
class ZDState:
    name: str
    initial: bool = False

    def to(self, target):
        return Transition(self, target)


@dataclass
class Transition:
    src: ZDState
    trg: ZDState
    name: str = None
    execute_callback: Callable = None
    execute_callback_succeeded: Callable = None

    def execute(self):
        succeeded = self.execute_callback()
        if succeeded:
            self.execute_callback_succeeded()


class ZDStateMachineMetaClass(ABCMeta):

    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)
        parent, = args[1]

        if parent is not ABC:
            states = []
            transitions = []

            for attrname in dir(cls):
                attr = getattr(cls, attrname)
                if isinstance(attr, Transition):
                    transitions.append(attr)
                    setattr(attr, "name", attrname)
                elif isinstance(attr, ZDState):
                    states.append(attr)

            setattr(cls, "states", states)
            setattr(cls, "transitions", transitions)

        return cls

    def __call__(cls, *args, **kwargs):
        self = super().__call__(*args, **kwargs)

        for transition in self.transitions:
            fn_name = f"on_{transition.name}"
            fn = getattr(cls, fn_name, None)
            if fn:
                transition.execute_callback = partial(fn, self)
                transition.execute_callback = partial(cls._after_transition_, self, transition.trg)

        init_state = [state for state in self.states if state.initial]
        if init_state:
            self.cur_state = init_state

        return self

    @staticmethod
    def _after_transition_(state_machine, trg_state):
        state_machine.cur_state = trg_state


class ZDStateMachine(ABC, metaclass=ZDStateMachineMetaClass):

    states: List[ZDState] = []
    transitions: List[Transition] = []

    def __init__(self):
        self.cur_state = None


class Action(ZDStateMachine):

    def move_next(self):
        pass


class AddAction(Action):
    pending = ZDState("pending", initial=True)
    cloud_running = ZDState("cloud_running")
    machine_running = ZDState("machine_running")
    final = ZDState("final")

    start = pending.to(cloud_running)
    start_machine = cloud_running.to(machine_running)
    finish = machine_running.to(final)

    def on_start(self):
        print("om_start")
        return True


if __name__ == '__main__':
    add = AddAction()
    print(f"initial state = {add.cur_state}")
    add.start.execute()
    print(f"initial state = {add.cur_state}")