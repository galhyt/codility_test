from abc import ABC, ABCMeta
from dataclasses import dataclass, field
from functools import partial
from typing import List, Callable


@dataclass
class ZDState:
    name: str
    initial: bool = False
    transitions: List = field(default_factory=list)

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
        return succeeded

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


class ZDStateMachine(ABC, metaclass=ZDStateMachineMetaClass):

    states: List[ZDState] = []
    transitions: List[Transition] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_transitions_callbacks_()
        self.cur_state = None
        self._set_cur_state_()

    def _set_transitions_callbacks_(self):
        for transition in self.transitions:
            fn_name = f"on_{transition.name}"
            fn = getattr(self, fn_name, None)
            transition.execute_callback = partial(self._on_transition_, fn, transition)
            transition.execute_callback_succeeded = partial(self._after_transition_, transition.trg)

    def _set_cur_state_(self):
        init_state = [state for state in self.states if state.initial]
        if init_state:
            self.cur_state = init_state[0]

    def _on_transition_(self, fn, transition):
        print(f"{transition}")
        if self.cur_state != transition.src:
            raise TypeError(f"Transition {transition.name} can't be executed from state {self.cur_state.name}")
        return fn() if fn else True

    def _after_transition_(self, trg_state):
        self.cur_state = trg_state


class Action(ZDStateMachine):

    def move_next(self):
        for tran in self.cur_state.transitions:
            if tran():
                self.move_next()


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


class RemoveAction(Action):
    pending = ZDState("pending", initial=True)
    machine_remove = ZDState("machine_remove")
    cloud_remove = ZDState("cloud_remove")
    final = ZDState("final")

    start = pending.to(machine_remove)
    start_cloud = machine_remove.to(cloud_remove)
    finish = cloud_remove.to(final)

    def on_start_cloud(self):
        print("on_start_cloud")
        return False


if __name__ == '__main__':
    add = AddAction()
    print(f"initial state = {add.cur_state}")
    add.start()
    print(f"initial state = {add.cur_state}")
    add.start_machine()
    print(f"initial state = {add.cur_state}")
