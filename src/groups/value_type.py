from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, List, Optional, Tuple

from .decorators import check_frozen
from .frozen import Frozen, FrozenInterface


@dataclass(slots=True)
class ValueTypeInterface(FrozenInterface):
    """
    The interface for the Type class.
    """
    _aliases: Tuple[str, ...] = field(default_factory=tuple)
    _type: Tuple[Any, ...] = field(default_factory=tuple)

    @property
    @abstractmethod
    def type(self) -> Any:
        """
        The type of the value.
        """
        pass

    @property
    @abstractmethod
    def aliases(self) -> Tuple[str, ...]:
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
    _aliases: Tuple[str, ...] = field(default_factory=tuple)
    _type: Tuple[Any, ...] = field(default_factory=tuple)
    _frozen: bool = field(init=False, default=False)

    def __init__(self, aliases: Tuple[str, ...], type_: Tuple[Any, ...], freeze: Optional[bool] = False) -> None:
        """
        Initialize the class.
        """
        self._aliases = aliases
        self._type = type_
        self._frozen = freeze

    @property
    def type(self) -> Tuple[Any, ...]:
        """
        The type of the value.
        """

        return self._type

    @type.setter
    @check_frozen
    def type(self, value: Tuple[str, ...]) -> None:
        """
        Set the type of the value.
        """
        for type_ in value:
            if isinstance(type_, list):
                type_ = tuple(type_)
        self._type = value

    @type.getter
    def type(self) -> Tuple[str, ...]:
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
    def aliases(self) -> Tuple[str, ...]:
        """
        The aliases of the value.
        """
        return self._aliases

    @aliases.setter
    @check_frozen
    def aliases(self, value: Tuple[str, ...]) -> None:
        """
        Set the aliases of the value.
        """
        self._aliases = value

    @aliases.getter
    def aliases(self) -> Tuple[str, ...]:
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
            self.aliases += (alias,)

    def __hash__(self) -> int:
        """
        Hash the class.
        """
        return hash(tuple(self.type))
