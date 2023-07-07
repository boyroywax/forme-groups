from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
from uuid import uuid4

from .decorators import check_frozen
from .frozen import Frozen, FrozenInterface
from .value_type import ValueTypeInterface, ValueType


@dataclass(slots=True)
class ValueTypeGroupInterface(FrozenInterface):
    _name: str
    _group: Dict[str, ValueTypeInterface]

    @property
    @abstractmethod
    def group(self) -> Dict[str, ValueTypeInterface]:
        """
        The group of the value types.
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """
        The name of the group.
        """
        pass

    @property
    @abstractmethod
    def aliases(self) -> List[str]:
        """
        The aliases of the group.
        """
        pass

    @property
    @abstractmethod
    def types(self) -> List[ValueTypeInterface]:
        """
        The types of the group.
        """
        pass

    @abstractmethod
    def add(self, alias: str, type_: ValueTypeInterface) -> None:
        """
        Add a value type to the group.
        """
        pass

    @abstractmethod
    def remove(self, alias: str) -> None:
        """
        Remove a value type from the group.
        """
        pass

    @abstractmethod
    def check_alias(self, alias: str) -> bool:
        """
        Check if the alias is in the group.
        """
        pass


@dataclass(slots=True, unsafe_hash=True)
class ValueTypeGroup:

    _name: str
    _group: Dict[str, ValueType] = field(default_factory=dict)
    _frozen: bool = field(default_factory=bool)

    def __init__(self, name: Optional[str] = None, group: Dict[str, ValueType] = Dict[str, ValueType], freeze: Optional[bool] = None) -> None:
        self._name = name
        self._group = group
        self._frozen = freeze

    @property
    def frozen(self) -> bool:
        """
        Whether the group is frozen.
        """
        return self._frozen

    def freeze(self) -> None:
        """
        Freeze the group.
        """
        for value in self._group.values():
            if value.frozen is False:
                value.freeze()
        self._frozen = True

    @property
    def group(self) -> Dict[str, ValueType]:
        """
        The group of the value types.
        """
        return self._group
    
    @group.setter
    @check_frozen
    def group(self, value: Dict[str, ValueType]) -> None:
        """
        Set the group of the value types.
        """
        self._group = value

    @group.getter
    def group(self) -> Dict[str, ValueType]:
        """
        Get the group of the value types.
        """
        return self._group
    
    @group.deleter
    @check_frozen
    def group(self) -> None:
        """
        Delete the group of the value types.
        """
        for value in self._group.values():
            del value

    @property
    def name(self) -> str:
        """
        The name of the group.
        """
        return self._name

    @name.setter
    @check_frozen
    def name(self, value: str) -> None:
        """
        Set the name of the group.
        """
        if self.check_name(value):
            raise ValueError("The group name is already in use.")
        self._name = value

    @name.getter
    def name(self) -> str:
        """
        Get the name of the group.
        """
        return self._name

    @name.deleter
    @check_frozen
    def name(self) -> None:
        """
        Delete the name of the group.
        """
        del self._name

    def check_alias(self, aliases: Tuple[str]) -> bool:
        for value in self._group.values():
            for alias in aliases:
                if value.check_alias(alias):
                    return True
        else:
            return False

    def check_name(self, name: str) -> bool:
        if self.name == name:
            return True
        else:
            return False

    def check_value_type_key(self, key: str) -> bool:
        for k in self._group.keys():
            if k == key:
                return True
        else:
            return False

    def check_type(self, type_: ValueType) -> bool:
        for value_type in self._group.values():
            if value_type.type == type_.type:
                return True
        else:
            return False

    @check_frozen
    def add(self, type_: ValueType, name: Optional[str] = None) -> None:
        """
        Add a value type to the group.
        """
        _name = name
        if _name is None:
            if type_.type is None:
                raise Exception("The type is None.")
            else:
                try:
                    _name = type(type_.type).__name__()
                except Exception:
                    _name = str(uuid4())

        if self.check_alias(type_.aliases):
            raise ValueError(f"The alias '{type_.aliases}' is already in use.")

        if self.check_name(_name):
            raise ValueError(f"The group name '{_name}' is already in use.")

        if self.check_type(type_):
            raise ValueError(f"The type '{type_}' is already in use.")

        if self.check_value_type_key(_name):
            raise ValueError(f"The key '{_name}' is already in use.")

        self._group[_name] = type_

    @check_frozen
    def remove(self, aliases: Optional[Tuple[str]] = None, name: Optional[str] = None) -> None:
        """
        Remove a value type from the group.
        """
        if aliases is None and name is None:
            raise ValueError("You must specify at least one of the two parameters.")

        if aliases is not None and name is not None:
            raise ValueError("You must specify only one of the two parameters.")

        entries = []

        if aliases is not None:
            if not self.check_alias(aliases):
                raise ValueError(f"The alias '{aliases}' is not in use.")
            else:
                for key, entry in self._group.items():
                    for alias in aliases:
                        if entry.check_alias(alias):
                            entries.append(key)

        if name is not None:
            if not self.check_name(name):
                raise ValueError(f"The name '{name}' is not in use.")
            else:
                entries.append(self._group[name])

        for entry in entries:
            del self._group[entry]

    def has_alias(self, alias: str) -> Any:
        """
        Returns the alias.
        """
        for key, value_type in self._group.items():
            if value_type.check_alias(alias):
                return key

    def get_aliases(self) -> Tuple[str]:
        """
        Returns the aliases.
        """
        aliases = []
        for type_ in self._group.values():
            for alias in type_.aliases:
                aliases.append(alias)
        return tuple(aliases)

    def get_value_type(self, alias: Optional[str] = None, value_type_id: Optional[str] = None) -> ValueType:
        """
        Returns the value type.
        """
        for id_, value_type in self._group.items():
            if value_type.check_alias(alias):
                return value_type
            if id_ == value_type_id:
                return value_type

    @property
    def aliases(self) -> Tuple[str]:
        """
        Returns the aliases.
        """
        return self.get_aliases()

    @property
    def types(self) -> Tuple[ValueType]:
        """
        Returns the value types.
        """
        return tuple(value.type for value in self._group.values())

    @types.getter
    def types(self) -> Tuple[ValueType]:
        """
        Returns the value types.
        """
        return tuple(value.type for value in self._group.values())

    @types.setter
    @check_frozen
    def types(self, value: Tuple[ValueType]) -> None:
        """
        Set the value types.
        """
        raise AttributeError("You can't set the value 'types'. Value 'types' are added and removed with the 'add' and 'remove' methods.")
