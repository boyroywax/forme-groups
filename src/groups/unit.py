import hashlib
from attrs import define, field, validators, converters
import json
from typing import Any, Optional, Tuple

from .interfaces.value import ValueInterface
from .interfaces.container import ContainerInterface
from .unit_type import UnitType, UnitTypeRef, UnitTypeFunction
from .utils.merkle_tree import MerkleTree
from .utils.converters import _value_converter, _type_ref_converter
from .utils.defaults import __DEFAULT_UNIT_TYPE_REF__, __DEFAULT_UNIT_TYPE__, __DEFAULT_COLLECTION_TYPES__


# def _type_ref_converter(type_ref: UnitTypeRef | str) -> UnitTypeRef:
#     if isinstance(type_ref, UnitTypeRef):
#         return type_ref
#     elif isinstance(type_ref, str):
#         return UnitTypeRef(alias=type_ref)
#     else:
#         raise ValueError(f"Invalid type_ref {type_ref}.")


@define(frozen=True, slots=True, weakref_slot=False)
class Unit:
    _value: ValueInterface | ContainerInterface = field(validator=validators.instance_of(ValueInterface | ContainerInterface))

    def __pre_init__(self, value: ValueInterface | ContainerInterface):
        """Initialize the Unit object.

        Args:
            value (ValueInterface | ContainerInterface): The value of the Unit object.
        """
        setattr(self, "_value", value)

    @property
    def value(self) -> ValueInterface | ContainerInterface:
        """Get the value of the Unit object.

        Returns:
            ValueInterface | ContainerInterface: The value of the Unit object.
        """
        return self._value
    
    def _verify_type_ref(self) -> bool:
        """Verify the type_ref of the Unit object.

        Args:
            type_ref (UnitTypeRef): The type_ref to verify.

        Returns:
            bool: Whether the type_ref is valid.
        """
        if isinstance(self._value, ValueInterface):
            
    
    @property
    def type_ref(self) -> UnitTypeRef:
        """Get the type_ref of the Unit object.

        Returns:
            UnitTypeRef: The type_ref of the Unit object.
        """
        return self._value.type_ref
    

