from abc import ABC
from attrs import define, field, validators
from typing import Any, Optional, Tuple, List

from .base import BaseInterface
from ..merkle_tree import MerkleTree


__DEFAULT_UNIT_TYPE_REF__ = "str"
__DEFAULT_VALUE_TYPES__ = str | int | float | bool | bytes | type(None)


@define(frozen=True, slots=True, weakref_slot=False)
class ValueInterface(BaseInterface):
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
