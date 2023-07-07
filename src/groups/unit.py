from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .value import ValueInterface, Value
from .value_type import ValueType

class UnitInterface(ABC):
    """
    The interface for the Unit class.
    """
    @abstractmethod
    def force_type(self) -> None:
        pass


@dataclass(
    slots=True
)
class Unit(UnitInterface):
    """
    This class manages a unit.
    """
    _type: ValueType = field(
        default=ValueType,
        init=False,
        repr=False,
        compare=False,
        hash=False,
        metadata=None
    )

    _value: Value = field(
        default=Value,
        init=False,
        repr=False,
        compare=False,
        hash=False,
        metadata=None
    )

    def __init__(
        self,
        type: ValueType
        value: Optional[Value] = None
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