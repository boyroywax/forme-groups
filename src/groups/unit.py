from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .decorators import check_frozen
from .frozen import Frozen, FrozenInterface
from .value import Value
from .value_type_ref import ValueTypeRef
from .value_type import ValueType

@dataclass(slots=True)
class UnitInterface(FrozenInterface):
    """
    The interface for the Unit class.
    """
    _type: ValueTypeRef
    _value: Value

    @property
    @abstractmethod
    def type(self) -> ValueTypeRef:
        """
        The type of the value.
        """
        pass

    @property
    @abstractmethod
    def value(self) -> Value:
        """
        The value of the value.
        """
        pass


@dataclass(
    # unsafe_hash=True,
    slots=True
)
class Unit(UnitInterface, Frozen):
    """
    This class manages a unit.
    """
    _type: ValueTypeRef = field(default_factory=ValueTypeRef)

    _value: Value = field(default_factory=Value)

    # _frozen: bool = field(default_factory=bool)

    def __init__(
        self,
        type_: ValueTypeRef,
        value_: Optional[Value] = None,
        frozen: Optional[bool] = False
    ) -> None:
        """
        Initializes the Unit class.
        """
        self._type = type_
        self._value = value_
        self._frozen = frozen

    @property
    def type(self) -> str:
        """
        Returns the type.
        """
        return self._type

    @type.setter
    @check_frozen
    def type(self, type_: ValueTypeRef) -> None:
        """
        Sets the type.
        """
        self._type = type_

    @type.getter
    def type(self) -> ValueTypeRef:
        """
        Gets the type.
        """
        return self._type

    @type.deleter
    @check_frozen
    def type(self) -> None:
        """
        Deletes the type.
        """
        del self._type

    @property
    def value(self) -> Any:
        """
        Returns the value.
        """
        return self._value

    @value.setter
    @check_frozen
    def value(self, value_: Value) -> None:
        """
        Sets the value.
        """
        self._value = value_

    @value.getter
    def value(self) -> Value:
        """
        Gets the value.
        """
        return self._value

    @value.deleter
    @check_frozen
    def value(self) -> None:
        """
        Deletes the value.
        """
        del self._value

    def __hash__(self) -> int:
        return hash((self._type, self._value))
