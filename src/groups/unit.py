import hashlib
from attrs import define, field, validators, converters
import json
from typing import Any, Optional, Tuple

from .unit_type import UnitType, UnitTypeRef, UnitTypeFunction





def _type_ref_converter(type_ref: UnitTypeRef | str) -> UnitTypeRef:
    if isinstance(type_ref, UnitTypeRef):
        return type_ref
    elif isinstance(type_ref, str):
        return UnitTypeRef(alias=type_ref)
    else:
        raise ValueError(f"Invalid type_ref {type_ref}.")

@define(frozen=True, slots=True)
class Value:
    _value: Any

    def __str__(self) -> str:
        return f"{self._value}"

    def __repr__(self) -> str:
        return f"{self._value}"

    def hash_256(self) -> str:
        return hashlib.sha256(self.__repr__().encode()).hexdigest()


def _value_converter(value: Any) -> Value:
    print(value.__class__.__name__)
    if isinstance(value, Value):
        return value
    elif isinstance(value, str) or isinstance(value, int) or isinstance(value, float) or isinstance(value, bool) or isinstance(value, dict) or isinstance(value, list) or isinstance(value, tuple) or isinstance(value, bytes) or value is None:
        return Value(value)
    else:
        raise ValueError(f"Invalid value {value}.")


@define(frozen=True, slots=True)
class Unit:
    value: Value = field(validator=validators.instance_of(Value | str | int | float | bool | dict | list | tuple | bytes | None), converter=_value_converter)
    type_ref: UnitTypeRef = field(validator=validators.instance_of(UnitTypeRef | str), converter=_type_ref_converter)

    # def __attrs_init__(self, value: Value | Any = None, type_ref: UnitTypeRef | str = None):
    #     if isinstance(value, Value):
    #         self.value = value
    #     else:
    #         self.value = Value(_value=value)

    #     if isinstance(type_ref, UnitTypeRef):
    #         self.type_ref = type_ref
    #     else:
    #         self.type_ref = UnitTypeRef(type_ref)

    def __str__(self) -> str:
        return f"{self.value.__str__()}"

    def __repr__(self) -> str:
        return f"Unit(value={self.value._value.__str__()}, type_ref={self.type_ref.__str__()})"

    def hash_256(self) -> str:
        return hashlib.sha256(self.__repr__().encode()).hexdigest()