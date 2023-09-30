from abc import ABC, abstractmethod, ABCMeta
from attrs import define, field, validators
from typing import Any, Optional, Tuple, List

from .base import BaseInterface
from ..utils.merkle_tree import MerkleTree


__DEFAULT_UNIT_TYPE_REF__ = "str"
__DEFAULT_VALUE_TYPES__ = str | int | float | bool | bytes | type(None)


@define(frozen=True, slots=True, weakref_slot=False)
class ValueInterface(BaseInterface, metaclass=ABCMeta):
    """A Value object.
    """
    _value: Optional[__DEFAULT_VALUE_TYPES__] = field(default=None, validator=validators.optional(validators.instance_of(__DEFAULT_VALUE_TYPES__)))

    def __pre_init__(self, value: __DEFAULT_VALUE_TYPES__):
        """Initialize the Value object.

        Args:
            value (__DEFAULT_VALUE_TYPES__): The value of the Value object.
        """
        setattr(self, "_value", value)

    @property
    def value(self) -> __DEFAULT_VALUE_TYPES__:
        """Get the value of the Value object.

        Returns:
            __DEFAULT_VALUE_TYPES__: The value of the Value object.
        """
        return self._value

    @property
    def type_ref(self) -> str:
        """Get the type_ref of the Value object.

        Returns:
            str: The type_ref of the Value object.
        """
        return type(self._value).__name__

    def convert_to_type(self, type_ref: str) -> __DEFAULT_VALUE_TYPES__:
        """Convert the Value object to a type.

        Args:
            type_ref (str): The type to convert the Value object to.

        Returns:
            __DEFAULT_VALUE_TYPES__: The converted Value object.
        """
        match(type_ref):
            case("str"):
                return str(self._value)
            case("int"):
                return int(self._value)
            case("float"):
                return float(self._value)
            case("bool"):
                return bool(self._value)
            case("bytes"):
                return bytes(self._value)
            case("NoneType"):
                return None
            case _:
                raise ValueError(f"Cannot convert Value to type {type_ref}.")
