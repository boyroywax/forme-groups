from abc import ABC, abstractmethod
from dataclasses import dataclass, field
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
        for obj in cls.__dict__.values():
            print(obj)

    cls.__init__ = new_init

    return cls


@dataclass(slots=True)
class UnitTypeRef:
    type_ref: Any = field(default=None, repr=True, hash=True)


@dataclass(slots=True)
class UnitValue:
    value: Any = field(default=None, repr=True)


@dataclass(slots=True)
class UnitType:
    aliases: Optional[Tuple[UnitTypeRef]] = field(default_factory=tuple)
    super_type: Optional[UnitTypeRef] = field(default_factory=UnitTypeRef)
    prefix: Optional[str] = field(default_factory=str)
    suffix: Optional[str] = field(default_factory=str)
    separator: Optional[str] = field(default_factory=str)
    function_call: Optional[object] = field(default_factory=object)

@dataclass(slots=True)
class UnitTypePool:
    pool: Dict[str, UnitType] = field(default_factory=dict)

    def __SYSTEM_RESERVED__(self):
        self.pool.update(**{
            "integer": UnitType(
                aliases=(UnitTypeRef("int"),),
                super_type="__RESERVED_INT__",
                prefix=None,
                suffix=None,
                separator=None,
                function_call=int
            ),
            "float": UnitType(
                aliases=(UnitTypeRef("float"), UnitTypeRef("double"), UnitTypeRef("FLOAT"), UnitTypeRef("DOUBLE")),
                super_type="__RESERVED_FLOAT__",
                prefix=None,
                suffix=None,
                separator=None,
                function_call=float
            ),
            "string": UnitType(
                aliases=(UnitTypeRef("str"), UnitTypeRef("STRING")),
                super_type="__RESERVED_STRING__",
                prefix=None,
                suffix=None,
                separator=None,
                function_call=str
            ),
            "boolean": UnitType(
                aliases=(UnitTypeRef("bool"), UnitTypeRef("BOOLEAN")),
                super_type="__RESERVED_BOOLEAN__",
                prefix=None,
                suffix=None,
                separator=None,
                function_call=bool
            ),
            "list": UnitType(
                aliases=(UnitTypeRef("list"), UnitTypeRef("LIST")),
                super_type="__RESERVED_LIST__",
                prefix="[",
                suffix="]",
                separator=",",
                function_call=list
            ),
            "tuple": UnitType(
                aliases=(UnitTypeRef("tuple"), UnitTypeRef("TUPLE")),
                super_type="__RESERVED_TUPLE__",
                prefix="(",
                suffix=")",
                separator=",",
                function_call=tuple
            ),
            "dict": UnitType(
                aliases=(UnitTypeRef("dict"), UnitTypeRef("DICT")),
                super_type="__RESERVED_DICT__",
                prefix="{",
                suffix="}",
                separator=",",
                function_call=dict
            ),
            "bytes": UnitType(
                aliases=(UnitTypeRef("bytes"), UnitTypeRef("BYTES")),
                super_type="__RESERVED_BYTES__",
                prefix="b'",
                suffix="'",
                separator=None,
                function_call=bytes
            ),
        })

    def add_type(self, unit_type: UnitType, name: Optional[str] = None):
        if name is None:
            name = unit_type.aliases[0].type_ref
        self.pool[name] = unit_type
    
    def get_type(self, name: Optional[str] = None, alias: Optional[UnitTypeRef] = None) -> UnitType:
        if name is None and alias is None:
            raise ValueError("Must provide either a name or an alias.")
        if name is not None and alias is not None:
            raise ValueError("Must provide either a name or an alias, not both.")
        if name is not None:
            if name not in self.pool:
                raise ValueError(f"Unit type {name} not found.")
            else:
                return self.pool[name]
        if alias is not None:
            for key, unit_type in self.pool.items():
                if alias in list(unit_type.aliases):
                    return self.pool[key]
            raise ValueError(f"Unit type {alias} not found.")
            
        return self.pool[name]
    
    def remove_type(self, name: Optional[str] = None, alias: Optional[UnitTypeRef] = None) -> UnitType:
        if name is None and alias is None:
            raise ValueError("Must provide either a name or an alias.")
        if name is not None and alias is not None:
            raise ValueError("Must provide either a name or an alias, not both.")
        if name is not None:
            if name not in self.pool.keys():
                raise ValueError(f"Unit type {name} not found.")
            else:
                del self.pool[name]
        if alias is not None:
            for key, unit_type in self.pool.items():
                if alias in list(unit_type.aliases):
                    del self.pool[key]
                    return
            raise ValueError(f"Unit type {alias} not found.")
    

@dataclass(slots=True)
class Unit:
    value: UnitValue = None
    type_: UnitTypeRef = None


# def convert_list_to_tuple(arg):
#     """
#     Converts a list to a tuple if the argument is a list.
#     """
#     if isinstance(arg, list):
#         return tuple(arg)
#     else:
#         return arg
    
# def convert_dict_to_tuple(arg):
#     """
#     Converts a dict to a tuple if the argument is a dict.
#     """
#     if isinstance(arg, dict):
#         return tuple(arg.items())
#     else:
#         return arg
    
# def convert_iterable_to_tuple(arg):
#     """
#     Converts an iterable to a tuple if the argument is an iterable.
#     """
#     if isinstance(arg, Iterable):
#         return tuple(arg)
#     else:
#         return arg


# def convert_lists_to_tuples(func):
#     """
#     Wrapper function that converts incoming lists to tuples.
#     """
#     def wrapper(*args, **kwargs):
#         args = tuple(convert_list_to_tuple(arg) for arg in args)
#         kwargs = {k: convert_list_to_tuple(v) for k, v in kwargs.items()}
#         return func(*args, **kwargs)
#     return wrapper

