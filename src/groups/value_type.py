from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, List, Optional, Tuple

from .decorators import check_frozen
from .frozen import Frozen, FrozenInterface
from .value_type_ref import ValueTypeRef, ValueTypeRefInterface


@dataclass(slots=True)
class ValueTypeInterface(FrozenInterface):
    """
    The interface for the Type class.
    """
    _aliases: Tuple[ValueTypeRefInterface, ...] = field(default_factory=tuple)
    _type: Tuple[Any, ...] = field(default_factory=tuple)
    _frozen: bool = field(init=False, default=False, repr=True)

    @property
    @abstractmethod
    def type(self) -> Any:
        """
        The type of the value.
        """
        pass

    @property
    @abstractmethod
    def aliases(self) -> Tuple[ValueTypeRef, ...]:
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
    def add_alias(self, alias: ValueTypeRef) -> None:
        """
        Add an alias to the aliases list.
        """
        pass

    @abstractmethod
    def remove_alias(self, alias: ValueTypeRef) -> None:
        """
        Remove an alias from the aliases list.
        """
        pass


@dataclass(slots=True)
class ValueType(ValueTypeInterface, Frozen):
    """
    The Value Type class.
    """
    # _aliases: Tuple[ValueTypeRef, ...] = field(default_factory=tuple, repr=True)
    # _type: Tuple[Any, ...] = field(default_factory=tuple, repr=True)
    # _frozen: bool = field(init=False, default=False, repr=True)

    def __init__(self, aliases: Tuple[ValueTypeRef, ...], type_: Tuple[Any, ...], freeze: Optional[bool] = False) -> None:
        """
        Initialize the class.
        """
        self._aliases = aliases
        self._type = type_
        self._frozen = freeze

    def __post_init__(self) -> None:
        """
        Post initialization.
        """
        # self.freeze()
        pass

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
    def aliases(self) -> Tuple[ValueTypeRef, ...]:
        """
        The aliases of the value.
        """
        return self._aliases

    @aliases.setter
    @check_frozen
    def aliases(self, value: Tuple[ValueTypeRef, ...]) -> None:
        """
        Set the aliases of the value.
        """
        self._aliases = value

    @aliases.getter
    def aliases(self) -> Tuple[ValueTypeRef, ...]:
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

    @check_frozen
    def remove_alias(self, alias: str) -> None:
        """
        Remove an alias from the aliases list.
        """
        if self.check_alias(alias):
            aliases = list(self.aliases)
            aliases.remove(alias)
            self.aliases = tuple(aliases)

    def __hash__(self) -> int:
        """
        Hash the class.
        """
        return hash(tuple(self.type))
    
    # def __repr__(self) -> str:
    #     return f"{self.__class__.__name__}(aliases={self.aliases}, type={self.type}, frozen={self.frozen}, _aliases={self._aliases}, _type={self._type}, _frozen={self._frozen})"
