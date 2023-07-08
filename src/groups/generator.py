from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

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
    def type_groups(self) -> Tuple[ValueTypeGroupInterface]:
        """
        The type groups of the generator.
        """
        pass

    @property
    @abstractmethod
    def types(self) -> Tuple[ValueTypeInterface]:
        """
        The types of the generator.
        """
        pass

    @property
    @abstractmethod
    def units(self) -> Tuple[UnitInterface]:
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

    _type_groups: Tuple[ValueTypeGroup] = field(default_factory=tuple)
    _units: Tuple[Unit] = field(default_factory=tuple)

    def __init__(self, type_groups: Tuple[ValueTypeGroup]) -> None:
        """
        Initialize the class.
        """
        self._type_groups = type_groups
        self._units = ()

    @property
    def type_groups(self) -> Tuple[ValueTypeGroup]:
        """
        The type groups of the generator.
        """
        return self._type_groups

    @property
    def types(self) -> Tuple[ValueType]:
        """
        The types of the generator.
        """
        types = []

        for type_group in self._type_groups:
            types.append(type_group.group)

        return tuple(types)

    @property
    def units(self) -> Tuple[UnitInterface]:
        """
        The units of the generator.
        """
        return self._units

    @check_frozen
    def add_type_group(self, type_group: ValueTypeGroup) -> None:
        """
        Add a type group to the generator.
        """
        if type_group in self._type_groups:
            raise ValueError(f"Type group '{type_group}' already exists.")

        for existing_type_group in self._type_groups:
            if existing_type_group.name == type_group.name:
                raise ValueError(f"Type group with name '{type_group.name}' already exists.")

            if existing_type_group.level == type_group.level:
                raise ValueError(f"Type group with level '{type_group.level}' already exists.")

        self._type_groups = self._type_groups + (type_group,)

    @check_frozen
    def remove_type_group(self, name: str) -> None:
        """
        Remove a type group from the generator.
        """
        if name not in self._type_groups:
            raise ValueError(f"Type group '{name}' does not exist.")

        del self._type_groups[name]


    
