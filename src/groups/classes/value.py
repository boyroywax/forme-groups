from abc import ABC, abstractmethod
from dataclasses import dataclass, field, InitVar
from typing import Any, Dict, List, Optional


_NONE = [None, "None", "NONE", "none", "null", "Null", "NULL", "nil", "Nil", "NIL", "NoneType", "nonetype", "NONETYPE"]
_EMPTY = ["", " ", "''", '""', str(""), str(" "), str("''"), str('""'), str(' ')]


class ValueInterface(ABC):
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
    init=False,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=True,
    frozen=True,
    match_args=True,
    kw_only=False,
    slots=True,
    weakref_slot=False
)
class Value(ValueInterface):
    """
    The Value class.
    """

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
        value: Any,
    ) -> None:
        """
        Initializes the Value class.
        """
        self._value = value

    @property
    def value(self) -> Any:
        """
        The value of the Value.
        """
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        """
        Sets the value of the Value.
        """
        self._value = value

    @value.deleter
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
