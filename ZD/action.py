from abc import ABC, ABCMeta
from dataclasses import dataclass
from functools import partial
from typing import List, Callable


@dataclass
class ZDState:
    name: str
    initial: bool = False
    transitions = []

    def to(self, target):
        return Transition(self, target)


@dataclass
class Transition:
    src: ZDState
    trg: ZDState
    name: str = None
    execute_callback: Callable = None
    execute_callback_succeeded: Callable = None

    def __call__(self, *args, **kwargs):
        succeeded = self.execute_callback(*args, **kwargs) if self.execute_callback else True
        if succeeded:
            self.execute_callback_succeeded()

    def __str__(self):
        return f"Transition {self.name}: {self.src.name} -> {self.trg.name}"


class ZDStateMachineMetaClass(ABCMeta):

    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)

        if all((parent is not ABC for parent in args[1])):
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

            for transition in cls.transitions:
                transition.src.transitions.append(transition)

        return cls

    def __call__(cls, *args, **kwargs):
        self = super().__call__(*args, **kwargs)

        for transition in self.transitions:
            fn_name = f"on_{transition.name}"
            fn = getattr(cls, fn_name, None)
            transition.execute_callback = partial(cls._on_transition_, fn, self, transition)
            transition.execute_callback_succeeded = partial(cls._after_transition_, self, transition.trg)

        init_state = [state for state in self.states if state.initial]
        if init_state:
            self.cur_state = init_state[0]

        return self

    @staticmethod
    def _after_transition_(state_machine, trg_state):
        state_machine.cur_state = trg_state

    @staticmethod
    def _on_transition_(fn, state_machine, transition):
        print(f"{transition}")
        if state_machine.cur_state != transition.src:
            raise TypeError(f"Transition {transition.name} can't be executed from state {state_machine.cur_state.name}")
        return fn(state_machine) if fn else True


class ZDStateMachine(ABC, metaclass=ZDStateMachineMetaClass):

    states: List[ZDState] = []
    transitions: List[Transition] = []

    def __init__(self):
        self.cur_state = None


class Action(ZDStateMachine):

    def move_next(self):
        for tran in self.cur_state.transitions:
            if tran():
                return True
        return False


class AddAction(Action):
    pending = ZDState("pending", initial=True)
    cloud_running = ZDState("cloud_running")
    machine_running = ZDState("machine_running")
    final = ZDState("final")

    start = pending.to(cloud_running)
    start_machine = cloud_running.to(machine_running)
    finish = machine_running.to(final)

    def on_start(self):
        print("on_start")
        return False


if __name__ == '__main__':
    add = AddAction()
    print(f"initial state = {add.cur_state}")
    add.start()
    print(f"initial state = {add.cur_state}")
    add.start_machine()
    print(f"initial state = {add.cur_state}")
