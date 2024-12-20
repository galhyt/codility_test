import importlib
import re
from abc import ABCMeta

from statemachine import ZDStateMachine
from statemachine import ZDStateMachineMetaClass


class ActionMetaClass(ZDStateMachineMetaClass):

    def __call__(cls, *args, **kwargs):
        if cls.__name__ != "Action":
            return super().__call__(*args, **kwargs)

        clstype = args[0]
        module_name = f"actions.{clstype}"
        module = importlib.import_module(module_name)
        cls_name = re.sub(r'(^|_)(\w)', lambda m: m.group(2).upper(), clstype)
        impl_cls = getattr(module, cls_name)
        return super(ActionMetaClass, impl_cls).__call__(*args[1:], **kwargs)


class Action(ZDStateMachine, metaclass=ActionMetaClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type = None

    @property
    def type(self):
        if self._type is None:
            self._type = re.sub(r'(\w+?)([A-Z])', r'\1_\2', self.__class__.__name__).lower()
        return self._type

    def move_next(self):
        for tran in self.cur_state.transitions:
            if tran.__get__(self, self.__class__)():
                self.move_next()
