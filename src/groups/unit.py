import hashlib
from attrs import define, field, validators, converters
import json
from typing import Any, Optional, Tuple

from .interfaces.base import BaseInterface
from .unit_type import UnitType, UnitTypeRef, UnitTypeFunction
from .utils.merkle_tree import MerkleTree
from .utils.converters import _value_converter, _type_ref_converter


# def _type_ref_converter(type_ref: UnitTypeRef | str) -> UnitTypeRef:
#     if isinstance(type_ref, UnitTypeRef):
#         return type_ref
#     elif isinstance(type_ref, str):
#         return UnitTypeRef(alias=type_ref)
#     else:
#         raise ValueError(f"Invalid type_ref {type_ref}.")


@define(frozen=True, slots=True)
class Value(BaseInterface):
    _value: Optional[Any] = field(default=None, validator=validators.optional(validators.instance_of(str | int | float | bool | dict | list | tuple | bytes | None)))

    # def __str__(self) -> str:
    #     return f"{self._value}"

    # def __repr__(self) -> str:
    #     return f"{self._value}"

    # def hash_sha256(self) -> str:
    #     return hashlib.sha256(self.__repr__().encode()).hexdigest()



@define(frozen=True, slots=True, weakref_slot=False)
class Unit(BaseInterface):
    _value: Value = field(validator=validators.instance_of(Value | str | int | float | bool | dict | list | tuple | bytes | None), converter=_value_converter)
    _type_ref: UnitTypeRef = field(validator=validators.instance_of(UnitTypeRef | str), converter=_type_ref_converter)

    @property
    def value(self) -> Value | str | int | float | bool | dict | list | tuple | bytes | None:
        return self._value._value

    @property
    def type_ref(self) -> str:
        return self._type_ref.__str__()

    def to_dict(self) -> dict:
        return {
            "value": self.value,
            "type_ref": self.type_ref
        }

    # def __str__(self) -> str:
    #     return f"{self.value.__str__()}"

    # def __repr__(self) -> str:
    #     return f"Unit(value={self.value}, type_ref={self.type_ref})"

    # def hash_sha256(self) -> str:
    #     return hashlib.sha256(self.__repr__().encode()).hexdigest()

    # def hash_tree(self) -> MerkleTree:
    #     return MerkleTree([self._value.hash_sha256(), self._type_ref.hash_sha256()])