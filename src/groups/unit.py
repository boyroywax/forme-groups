from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .value import ValueInterface, Value
from .type import TypeInterface, Type

class UnitInterface(ValueInterface, TypeInterface):
    """
    The interface for the Unit class.
    """
    @abstractmethod
    def force_type(self) -> None:
        pass


@dataclass(
    init=False,
    repr=False,
    eq=False,
    order=False,
    unsafe_hash=True,
    frozen=True,
    match_args=True,
    kw_only=False,
    slots=True,
    weakref_slot=False
)
class Unit(UnitInterface, Value, Type):
    """
    This class manages a unit.
    """
    _type: str = field(
        default=None,
        init=False,
        repr=False,
        compare=False,
        hash=False,
        metadata=None
    )

    _value: Any = field(
        default=None,
        init=False,
        repr=False,
        compare=False,
        hash=False,
        metadata=None
    )

    def __init__(
        self,
        type: Optional[str] = None,
        value: Optional[Any] = None
    ) -> None:
        """
        Initializes the Unit class.
        """
        self._type = type
        self._value = value

    @property
    def type(self) -> str:
        """
        Returns the type.
        """
        return self._type

    @property
    def value(self) -> Any:
        """
        Returns the value.
        """
        return self._value

    def force_type(self) -> None:
        """
        Forces the type.
        """
        pass

    def check_none(self) -> bool:
        """
        Checks if the value is None.
        """
        pass