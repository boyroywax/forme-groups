from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any

from .decorators import check_frozen
from .frozen import Frozen, FrozenInterface


_NONE = [None, "None", "NONE", "none", "null", "Null", "NULL", "nil", "Nil", "NIL", "NoneType", "nonetype", "NONETYPE"]
_EMPTY = ["", " ", "''", '""', str(""), str(" "), str("''"), str('""'), str(' ')]

@dataclass(
    slots=True,
)
class ValueInterface(FrozenInterface):
    """
    The interface for the Value class.
    """

    @property
    @abstractmethod
    def value(self) -> Any:
        pass

    @abstractmethod
    def check_empty(self) -> bool:
        pass

    @abstractmethod
    def check_none(self) -> bool:
        pass


@dataclass(
    slots=True,
)
class Value(ValueInterface, Frozen):
    """
    The Value class.
    """

    _value: Any = field(
        default=Any,
        init=False,
        repr=False,
        compare=False,
        hash=False,
        metadata=None
    )

    # _frozen: bool = field(default_factory=bool)

    def __init__(
        self,
        value: Any,
        freeze: bool = False
    ) -> None:
        """
        Initializes the Value class.
        """
        self._value = value
        self._frozen = freeze

    @property
    def value(self) -> Any:
        """
        The value of the Value.
        """
        return self._value

    @value.setter
    @check_frozen
    def value(self, value: Any) -> None:
        """
        Sets the value of the Value.
        """
        self._value = value

    @value.deleter
    @check_frozen
    def value(self) -> None:
        """
        Deletes the value of the Value.
        """
        del self._value

    @value.getter
    def value(self) -> Any:
        """
        Gets the value of the Value.
        """
        return self._value

    def check_empty(self) -> bool:
        """
        Checks if the value is None.
        """
        return self.value in _EMPTY

    def check_none(self) -> bool:
        """
        Checks if the value is None.
        """
        return self.value is None or self.value in _NONE

    def __hash__(self) -> int:
        """
        Hashes the Value.
        """
        return hash(self.value)