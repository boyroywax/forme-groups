from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, List, Optional, Tuple, Iterable

from .decorators import check_frozen
from .frozen import Frozen, FrozenInterface
from .value_type_ref import ValueTypeRef, ValueTypeRefInterface


@dataclass(slots=True)
class ValueTypeInterface(FrozenInterface):
    """
    The interface for the Type class.
    """
    _aliases: Tuple[ValueTypeRefInterface, ...] = field(default_factory=tuple)
    _type: Tuple[Any] = field(default_factory=tuple)
    _frozen: bool = field(default_factory=bool, init=False)
    _super_type: Optional[ValueTypeRefInterface] = field(default_factory=ValueTypeRefInterface)
    _prefix: Optional[str] = None
    _suffix: Optional[str] = None
    _separator: Optional[str] = None

    @property
    @abstractmethod
    def type_(self) -> Any:
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

    @property
    @abstractmethod
    def super_type(self) -> Optional[ValueTypeRef]:
        """
        The super type of the value.
        """
        pass

    @property
    @abstractmethod
    def prefix(self) -> Optional[str]:
        """
        The prefix of the value.
        """
        pass

    @property
    @abstractmethod
    def suffix(self) -> Optional[str]:
        """
        The suffix of the value.
        """
        pass

    @property
    @abstractmethod
    def separator(self) -> Optional[str]:
        """
        The seperator of the value.
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

    def __init__(
        self,
        aliases: Tuple[ValueTypeRef, ...],
        type_: Tuple[Any, ...],
        freeze: Optional[bool] = False,
        super_type: Optional[ValueTypeRef] = None,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        separator: Optional[str] = None
    ) -> None:
        """
        Initialize the class.
        """
        for attr in ('aliases', 'type_', 'super_type', 'prefix', 'suffix', 'separator'):
            if isinstance(attr, list):
                attr = tuple(attr)

        self._aliases = aliases
        self._type = type_
        self._frozen = freeze
        self._super_type = super_type
        self._prefix = prefix
        self._suffix = suffix
        self._separator = separator


    def __post_init__(self) -> None:
        """
        Post initialization.
        """
        # self.freeze()
        pass

    @property
    def type_(self) -> Tuple[Any, ...]:
        """
        The type of the value.
        """

        return self._type

    @type_.setter
    @check_frozen
    def type_(self, value: Tuple[str, ...]) -> None:
        """
        Set the type of the value.
        """
        for type_ in value:
            if isinstance(type_, list):
                type_ = tuple(type_)
        self._type = value

    @type_.getter
    def type_(self) -> Tuple[str, ...]:
        """
        Get the type of the value.
        """
        return self._type

    @type_.deleter
    @check_frozen
    def type_(self) -> None:
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
    def add_alias(self, alias: str ) -> None:
        """
        Add an alias to the aliases list.
        """
        if not self.check_alias(alias):
            self.aliases += ValueTypeRef(alias)

    @check_frozen
    def remove_alias(self, alias: str) -> None:
        """
        Remove an alias from the aliases list.
        """
        if self.check_alias(alias):
            aliases = list(self.aliases)
            aliases.remove(alias)
            self.aliases = tuple(aliases)

    @property
    def super_type(self) -> Optional[ValueTypeRef]:
        """
        The super type of the value.
        """
        return self._super_type
    
    @super_type.setter
    @check_frozen
    def super_type(self, value: ValueTypeRef) -> None:
        """
        Set the super type of the value.
        """
        self._super_type = value

    @super_type.getter
    def super_type(self) -> Optional[ValueTypeRef]:
        """
        Get the super type of the value.
        """
        return self._super_type
    
    @super_type.deleter
    @check_frozen
    def super_type(self) -> None:
        """
        Delete the super type of the value.
        """
        del self._super_type

    @property
    def prefix(self) -> Optional[str]:
        """
        The prefix of the value.
        """
        return self._prefix
    
    @prefix.setter
    @check_frozen
    def prefix(self, value: Optional[str] = None) -> None:
        """
        Set the prefix of the value.
        """
        self._prefix = value

    @prefix.getter
    def prefix(self) -> Optional[str]:
        """
        Get the prefix of the value.
        """
        return self._prefix
    
    @prefix.deleter
    @check_frozen
    def prefix(self) -> None:
        """
        Delete the prefix of the value.
        """
        raise AttributeError("Cannot delete prefix.")

    @property
    def suffix(self) -> Optional[str]:
        """
        The suffix of the value.
        """
        return self._suffix
    
    @suffix.setter
    @check_frozen
    def suffix(self, value: Optional[str] = None) -> None:
        """
        Set the suffix of the value.
        """
        self._suffix = value

    @suffix.getter
    def suffix(self) -> Optional[str]:
        """
        Get the suffix of the value.
        """
        return self._suffix
    
    @suffix.deleter
    @check_frozen
    def suffix(self) -> None:
        """
        Delete the suffix of the value.
        """
        raise AttributeError("Cannot delete suffix.")
    
    @property
    def separator(self) -> Optional[str]:
        """
        The seperator of the value.
        """
        return self._separator
    
    @separator.setter
    @check_frozen
    def separator(self, value: str) -> None:
        """
        Set the seperator of the value.
        """
        self._separator = value


    def __hash__(self) -> int:
        """
        Hash the class.
        """
        return hash(tuple(self.type_))
    
    def __iter__(self) -> Iterable[Any]:
        """
        Iterate over the class.
        """
        return iter(tuple(self.type_))
    
    # def __repr__(self) -> str:
    #     return f"{self.__class__.__name__}(aliases={self.aliases}, type={self.type}, frozen={self.frozen}, _aliases={self._aliases}, _type={self._type}, _frozen={self._frozen})"
