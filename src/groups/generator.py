from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .decorators import check_frozen
from .frozen import FrozenInterface, Frozen
from .unit import UnitInterface, Unit
from .value_type import ValueTypeInterface, ValueType
from .value_type_group import ValueTypeGroupInterface, ValueTypeGroup


class GeneratorInterface(FrozenInterface):
    """
    The interface for the Generator class.
    """

    @property
    @abstractmethod
    def type_groups(self) -> Dict[str, ValueTypeGroupInterface]:
        """
        The type groups of the generator.
        """
        pass

    @property
    @abstractmethod
    def types(self) -> Dict[str, ValueTypeInterface]:
        """
        The types of the generator.
        """
        pass

    @property
    @abstractmethod
    def units(self) -> Dict[str, UnitInterface]:
        """
        The units of the generator.
        """
        pass


@dataclass(
    slots=True
)
class Generator(GeneratorInterface, Frozen):
    """
    This class manages the generator.
    """

    _type_groups: Dict[str, ValueTypeGroup] = field(default_factory=dict)
    _units: Dict[str, UnitInterface] = field(default_factory=dict)

    def __init__(self) -> None:
        """
        Initialize the class.
        """
        self._type_groups = {}
        self._units = {}

    @property
    def type_groups(self) -> Dict[str, ValueTypeGroup]:
        """
        The type groups of the generator.
        """
        return self._type_groups

    @property
    def types(self) -> Dict[str, ValueType]:
        """
        The types of the generator.
        """
        types = {}

        for type_group in self._type_groups.values():
            types.update(type_group.group)

        return types

    @property
    def units(self) -> Dict[str, UnitInterface]:
        """
        The units of the generator.
        """
        return self._units

    @check_frozen
    def add_type_group(self, name: str) -> None:
        """
        Add a type group to the generator.
        """
        if name in self._type_groups:
            raise ValueError(f"Type group '{name}' already exists.")

        self._type_groups[name] = ValueTypeGroup(name)

    @check_frozen
    def remove_type_group(self, name: str) -> None:
        """
        Remove a type group from the generator.
        """
        if name not in self._type_groups:
            raise ValueError(f"Type group '{name}' does not exist.")

        del self._type_groups[name]

    
