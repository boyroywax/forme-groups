from abc import ABC, abstractmethod
from dataclasses import dataclass, field, InitVar
from typing import Any, Dict, List, Optional


_STRING_TYPES = str
_STRING_ALIASES = ["str", "string", "String", "STRING", "STR"]

_BYTE_TYPES = bytes
_BYTE_ALIASES = ["bytes", "Bytes", "BYTES"]

_NUMBER_TYPES = (int, float, complex)
_NUMBER_ALIASES = ["int", "integer", "Int", "Integer", "INT", "INTEGER", "float", "Float", "FLOAT", "complex", "Complex", "COMPLEX"]

_BOOLEAN_TYPES = bool
_BOOLEAN_ALIASES = ["bool", "boolean", "Bool", "Boolean", "BOOL", "BOOLEAN"]

_LIST_TYPES = list
_LIST_ALIASES = ["list", "List", "LIST"]

_TUPLE_TYPES = tuple
_TUPLE_ALIASES = ["tuple", "Tuple", "TUPLE"]

_DICT_TYPES = dict
_DICT_ALIASES = ["dict", "Dict", "DICT"]

_SET_TYPES = set
_SET_ALIASES = ["set", "Set", "SET"]

_NONE_TYPES = type(None)
_NONE_ALIASES = ["none", "None", "NONE", "null", "Null", "NULL", "nil", "Nil", "NIL", "NoneType", "nonetype", "NONETYPE"]

_ANY_TYPES = Any
_ANY_ALIASES = ["any", "Any", "ANY"]



class TypesGroupInterface(ABC):
    """
    The Interface for the Types class.
    """
    @property
    @abstractmethod
    def id(self) -> str:
        """
        Returns the id.
        """
        pass

    @property
    @abstractmethod
    def types(self) -> Dict[str, Any]:
        """
        Returns the types and aliases.
        """
        pass

    @abstractmethod
    def has_alias(self, alias: str) -> Any:
        """
        Returns the type provided the alias.
        """
        pass

    @abstractmethod
    def get_aliases(self, type_: Optional[Any] = None) -> List[str]:
        """
        Returns the aliases.
        """
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
class TypesGroup(TypesGroupInterface):
    """
    This class manages a group of types.
    """

    _id: str = field(
        default=None,
        init=False,
        repr=False,
        compare=False,
        hash=False,
        metadata=None
    )

    _types: Dict[str, Any] = field(
        default=None,
        init=False,
        repr=False,
        compare=False,
        hash=False,
        metadata=None
    )

    def __init__(
        self,
        types: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Initializes the TypesGroup class.
        """
        self._types = types if types is not None else self.get_types()

    @property
    def id(self) -> str:
        """
        Returns the id.
        """
        return self._id

    @property
    def types(self) -> Dict[str, Any]:
        """
        Returns the types.
        """
        return self._types

    @types.setter
    def types(self, types: Dict[str, Any]) -> None:
        """
        Sets the types.
        """
        self._types = types

    def has_alias(self, alias: str) -> Any:
        """
        Returns the alias.
        """
        for type_ in self.types:
            if alias in self.get_aliases(type_):
                return alias
        return None

    def get_aliases(self, type_: Optional[Any] = None) -> List[str]:
        """
        Returns the aliases.
        """
        if type_ is None:
            return []
        aliases = []
        for alias, type__ in self.types.items():
            if type_ == type__:
                aliases.append(alias)
        return aliases

