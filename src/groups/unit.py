from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .decorators import check_frozen
from .value import Value
from .value_type import ValueType


class UnitInterface(ABC):
    """
    The interface for the Unit class.
    """
    _type: ValueType
    _value: Value

    @property
    @abstractmethod
    def type(self) -> str:
        """
        The type of the value.
        """
        pass

    @property
    @abstractmethod
    def value(self) -> Any:
        """
        The value of the value.
        """
        pass

    @abstractmethod
    def force_type(self) -> None:
        pass

    @property
    @abstractmethod
    def frozen(self) -> bool:
        """
        Check if the class is frozen.
        """
        pass

    @abstractmethod
    def freeze(self) -> None:
        """
        Freeze the class.
        """
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

    _frozen: bool = field(default_factory=bool)

    def __init__(
        self,
        type_: ValueType,
        value_: Optional[Value] = None,
        frozen: bool = False
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
    def type(self, type_: ValueType) -> None:
        """
        Sets the type.
        """
        self._type = type_

    @type.getter
    def type(self) -> ValueType:
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

    def force_type(self) -> None:
        """
        Forces the type.
        """
        pass

    @property
    def frozen(self) -> bool:
        """
        Checks if the class is frozen.
        """
        return self._frozen

    @check_frozen
    def freeze(self) -> None:
        """
        Freezes the class.
        """
        self._frozen = True
        for attr in self.__dict__:
            if isinstance(self.__dict__[attr], UnitInterface):
                if self.__dict__[attr].frozen is False:
                    self.__dict__[attr].freeze()
