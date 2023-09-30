import hashlib
from abc import ABC, abstractmethod, ABCMeta
from attrs import define, field, validators, converters
import json
from typing import Any, Optional, Tuple

from .interfaces.base import BaseInterface
from .interfaces.value import ValueInterface
from .interfaces.container import ContainerInterface
from .unit_type import UnitType, UnitTypeRef, UnitTypeFunction
from .utils.merkle_tree import MerkleTree

# def _type_ref_converter(type_ref: UnitTypeRef | str) -> UnitTypeRef:
#     if isinstance(type_ref, UnitTypeRef):
#         return type_ref
#     elif isinstance(type_ref, str):
#         return UnitTypeRef(alias=type_ref)
#     else:
#         raise ValueError(f"Invalid type_ref {type_ref}.")


@define(frozen=True, slots=True, weakref_slot=False)
class Unit(BaseInterface):
    _unit: ValueInterface | ContainerInterface = field(validator=validators.instance_of(ValueInterface | ContainerInterface))

    @property
    def unit(self) -> ValueInterface | ContainerInterface:
        """Get the _unit of the Unit object.

        Returns:
            ValueInterface | ContainerInterface: The _unit of the Unit object.
        """
        return self.__getattribute__("_unit")

    @property
    def value(self) -> ValueInterface | ContainerInterface:
        """Get the value of the Unit object.

        Returns:
            ValueInterface | ContainerInterface: The value of the Unit object.
        """
        return self.unit.value
    
    @property
    def type_ref(self) -> UnitTypeRef:
        """Get the type_ref of the Unit object.

        Returns:
            UnitTypeRef: The type_ref of the Unit object.
        """
        return self.unit.type_ref
    

