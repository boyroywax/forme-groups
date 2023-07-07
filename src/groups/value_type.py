from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, List, Optional

from .decorators import check_frozen
from .frozen import Frozen, FrozenInterface


@dataclass(slots=True)
class ValueTypeInterface(FrozenInterface):
    """
    The interface for the Type class.
    """
    _aliases: List[str]
    _type: List[Any]

    @property
    @abstractmethod
    def type(self) -> Any:
        """
        The type of the value.
        """
        pass

    @property
    @abstractmethod
    def aliases(self) -> List[str]:
        """
        The aliases of the value.
        """
        pass

    @abstractmethod
    def check_alias(self, alias: str) -> bool:
        """
        Check if the alias is in the aliases list.
        """
        pass

    @abstractmethod
    def add_alias(self, alias: str) -> None:
        """
        Add an alias to the aliases list.
        """
        pass


@dataclass(frozen=False, slots=True)
class ValueType(ValueTypeInterface, Frozen):
    """
    The Value Type class.
    """
    _aliases: List[str]
    _type: List[Any]
    _frozen: bool = field(init=False, default=False)

    def __init__(self, aliases: List[str], type_: List[Any], freeze: Optional[bool] = False) -> None:
        """
        Initialize the class.
        """
        self._aliases = aliases
        self._type = type_
        self._frozen = freeze

    @property
    def type(self) -> List[Any]:
        """
        The type of the value.
        """
        return self._type

    @type.setter
    @check_frozen
    def type(self, value: List[str]) -> None:
        """
        Set the type of the value.
        """
        # if self.frozen:
        #     raise Exception("Cannot set type of frozen class.")
        self._type = value

    @type.getter
    def type(self) -> List[str]:
        """
        Get the type of the value.
        """
        return self._type

    @type.deleter
    @check_frozen
    def type(self) -> None:
        """
        Delete the type of the value.
        """
        del self._type

    @property
    def aliases(self) -> List[str]:
        """
        The aliases of the value.
        """
        return self._aliases

    @aliases.setter
    @check_frozen
    def aliases(self, value: List[str]) -> None:
        """
        Set the aliases of the value.
        """
        self._aliases = value

    @aliases.getter
    def aliases(self) -> List[str]:
        """
        Get the aliases of the value.
        """
        return self._aliases

    @aliases.deleter
    @check_frozen
    def aliases(self) -> None:
        """
        Delete the aliases of the value.
        """
        del self._aliases

    def check_alias(self, alias: str) -> bool:
        """
        Check if the alias is in the aliases list.
        """
        return alias in self.aliases

    @check_frozen
    def add_alias(self, alias: str) -> None:
        """
        Add an alias to the aliases list.
        """
        if not self.check_alias(alias):
            self.aliases.append(alias)
