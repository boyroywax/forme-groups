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
    _value: Value = field(validator=validators.instance_of(Value | str | int | float | bool | dict | list | tuple | bytes | None), converter=_value_converter)
    _type_ref: UnitTypeRef = field(validator=validators.instance_of(UnitTypeRef | str), converter=_type_ref_converter)

    @property
    def value(self) -> str | int | float | bool | dict | list | tuple | bytes | None:
        return self._value._value
    
    @property
    def type_ref(self) -> str:
        return self._type_ref.__str__()

    def __str__(self) -> str:
        return f"{self.value.__str__()}"

    def __repr__(self) -> str:
        return f"Unit(value={self.value}, type_ref={self.type_ref})"

    def hash_256(self) -> str:
        return hashlib.sha256(self.__repr__().encode()).hexdigest()