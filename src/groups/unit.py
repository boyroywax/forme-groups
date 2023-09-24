import hashlib
from attrs import define, field, validators
import json
from typing import Any, Optional, Tuple

from .unit_type import UnitType, UnitTypeRef, UnitTypeFunction


@define(frozen=True, slots=True)
class Value:
    _value: Any

    def __str__(self) -> str:
        return f"{self._value}"

    def __repr__(self) -> str:
        return f"{self._value}"

    def hash_256(self) -> str:
        return hashlib.sha256(self.__repr__().encode()).hexdigest()


@define(frozen=True, slots=True)
class Unit:
    value: Value
    type_ref: UnitTypeRef

    def __attrs_init__(self, value: Value | Any = None, type_ref: UnitTypeRef | str = None):
        if isinstance(value, Value):
            self.value = value
        else:
            self.value = Value(value)

        if isinstance(type_ref, UnitTypeRef):
            self.type_ref = type_ref
        else:
            self.type_ref = UnitTypeRef(type_ref)

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"Unit(value={self.value.__repr__()}, type_ref={self.type_ref.__repr__()})"

    def hash_256(self) -> str:
        return hashlib.sha256(self.__repr__().encode()).hexdigest()