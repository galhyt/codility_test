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

    def __call__(self, instance, *args, **kwargs):
        succeeded = self.execute_callback(instance, *args, **kwargs) if self.execute_callback else True
        if succeeded:
            self.execute_callback_succeeded(instance)
        return succeeded

    def __str__(self):
        return f"Transition {self.name}: {self.src.name} -> {self.trg.name}"


class BoundTransition:
    def __init__(self, transition: Transition):
        self.transition = transition

    def __get__(self, instance, owner):
        # Return a callable bound to the instance of A
        def transition_bounded(*args, **kwargs):
            return self.transition(instance, *args, **kwargs)
        return transition_bounded


class ZDStateMachineMetaClass(ABCMeta):

    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)

        if all((parent is not ABC for parent in args[1])):
            states = []
            transitions = []

            for attrname in dir(cls):
                attr = getattr(cls, attrname)
                if isinstance(attr, Transition):
                    transitions.append((attr, BoundTransition(attr)))
                    setattr(attr, "name", attrname)
                elif isinstance(attr, ZDState):
                    states.append(attr)

            setattr(cls, "states", states)
            setattr(cls, "transitions", transitions)

            for transition, bound_transition in cls.transitions:
                transition.src.transitions.append(bound_transition)

            if cls.states:
                cls.init_state = cls._get_initial_state_()
            if cls.transitions:
                cls._set_transitions_callbacks_()

            for transition, bound_transition in cls.transitions:
                setattr(cls, transition.name, bound_transition)

        return cls

    def _set_transitions_callbacks_(cls):
        for transition, bound_transition in cls.transitions:
            fn_name = f"on_{transition.name}"
            fn = getattr(cls, fn_name, None)
            transition.execute_callback = partial(cls._on_transition_, fn, transition)
            transition.execute_callback_succeeded = partial(cls._after_transition_, transition.trg)

    def _get_initial_state_(cls):
        init_state = [state for state in cls.states if state.initial]
        if len(init_state) != 1:
            raise Exception(f"There should be only one state. initial states are {[state.name for state in init_state]}")
        return init_state[0]

    def _on_transition_(cls, fn, transition, instance):
        print(f"{transition}")
        if instance.cur_state != transition.src:
            raise TypeError(f"Transition {transition.name} can't be executed from state {instance.cur_state.name}")
        return fn(instance) if fn else True

    def _after_transition_(cls, trg_state, instance):
        instance.cur_state = trg_state


class ZDStateMachine(ABC, metaclass=ZDStateMachineMetaClass):

    states: List[ZDState] = []
    transitions: List[Transition] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cur_state = self.init_state
