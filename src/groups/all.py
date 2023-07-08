from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Callable, Tuple, Iterable


@dataclass(slots=True)
class Frozen(object):
    _frozen: bool = False

    def __init__(self, *args, **kwargs):
        object.__setattr__(self, "_frozen", False)

    def __setattr__(self, name, value):
        if getattr(self, "_frozen", False):
            raise AttributeError("Cannot modify frozen class.")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if getattr(self, "_frozen", False):
            raise AttributeError("Cannot modify frozen class.")
        object.__delattr__(self, name)


def frozen(cls):
    """
    Decorator that makes a class immutable (i.e. frozen).
    """
    def freeze(cls, *args, **kwargs):
        if getattr(cls, "_frozen", False):
            raise AttributeError("Cannot modify frozen class.")
        return cls

    cls.__setattr__ = freeze
    cls.__delattr__ = freeze

    original_init = cls.__init__

    print(original_init.__str__())

    def new_init(self, *args, **kwargs):
        original_init(cls, *args, **kwargs)
        cls._frozen = True

    cls.__init__ = new_init

    return cls


@dataclass(slots=True)
class UnitTypeRef:
    type_ref: Any = None


@dataclass(slots=True)
class UnitValue:
    value: Any = None


# @dataclass(slots=True)
# class UnitTypeInterface(ABC):
#     aliases: tuple = (UnitTypeRef)
#     super_type: Optional[UnitTypeRef] = None
#     prefix: Optional[str] = None
#     suffix: Optional[str] = None
#     separator: Optional[str] = None
#     function_call: Optional[Callable] = None


@dataclass(slots=True)
class UnitType:
    aliases: Optional[Tuple[UnitTypeRef]] = None
    super_type: Optional[UnitTypeRef] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    separator: Optional[str] = None
    function_call: Optional[Callable] = None
