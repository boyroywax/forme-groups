from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Iterable

from .decorators import check_frozen
from .frozen import Frozen, FrozenInterface


class ValueTypeRefInterface(FrozenInterface):
    """
    The interface for the ValueTypeRef class.
    """
    _alias: str

    @property
    @abstractmethod
    def alias(self) -> str:
        """
        The alias of the value type.
        """
        pass


@dataclass(slots=True)
class ValueTypeRef(ValueTypeRefInterface, Frozen):
    """
    The Value Type Ref class.
    """
    _alias: str = field(default_factory=str, repr=True)

    def __init__(self, alias: str, freeze: Optional[bool] = False) -> None:
        """
        Initializes the ValueTypeRef class.
        """
        self._alias = alias
        self._frozen = freeze

    @property
    def alias(self) -> str:
        """
        The alias of the value type.
        """
        return self._alias

    @alias.setter
    @check_frozen
    def alias(self, alias: str) -> None:
        """
        Sets the alias of the value type.
        """
        self._alias = alias

    @alias.getter
    def alias(self) -> str:
        """
        Gets the alias of the value type.
        """
        return self._alias
    
    def __iter__(self) -> Iterable:
        """
        Returns the iterator for the ValueTypeRef class.
        """
        return iter(self._alias)