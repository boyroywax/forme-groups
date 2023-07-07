from abc import ABC, abstractmethod
from dataclasses import dataclass, field, InitVar, is_dataclass
from typing import Any, Dict, List, Optional
from uuid import uuid4


def check_frozen(cls):
    """
    Check if the class is frozen.
    """
    def wrapper(self, *args, **kwargs):
        if self._frozen:
            raise Exception("Cannot modify frozen class.")
        return cls(self, *args, **kwargs)
    return wrapper


@dataclass(frozen=False, slots=True)
class ValueTypeInterface(ABC):
    """
    The interface for the Type class.
    """
    _aliases: List[str]
    _type: List[Any]
    _frozen: bool = field(init=False, default=False)

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

    @abstractmethod
    def freeze(self) -> None:
        """
        Freeze the class.
        """
        pass

    @property
    @abstractmethod
    def frozen(self) -> bool:
        """
        Check if the class is frozen.
        """
        pass


@dataclass(frozen=False, slots=True)
class ValueType(ValueTypeInterface):
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

    @property
    def frozen(self) -> bool:
        """
        Check if the class is frozen.
        """
        return self._frozen

    @frozen.setter
    @check_frozen
    def frozen(self, value: bool) -> None:
        """
        Set the frozen value.
        """
        raise AssertionError("Cannot set frozen value, use freeze() method instead.")

    @frozen.getter
    def frozen(self) -> bool:
        """
        Get the frozen value.
        """
        return self._frozen

    @check_frozen
    def freeze(self) -> None:
        """
        Freeze the class.
        """
        self._frozen = True


@dataclass(frozen=False, slots=True)
class ValueTypeGroupInterface(ABC):
    _name: str
    _group: Dict[str, ValueTypeInterface]
    _frozen: bool = field(init=False, default=False)

    @property
    @abstractmethod
    def frozen(self) -> bool:
        """
        Check if the class is frozen.
        """
        pass

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

    @abstractmethod
    def freeze(self) -> None:
        """
        Freeze the class group.
        """
        pass


@dataclass(frozen=False, slots=True)
class ValueTypeGroup(ValueTypeGroupInterface):
    """
    This class manages a group of values.
    """
    _name: str
    _group: Dict[str, ValueType]
    _frozen: bool = field(init=False, default=False)

    def __init__(self, name: Optional[str] = None, group: Dict[str, ValueType] = Dict, freeze: Optional[bool] = False) -> None:
        """
        Initialize the class.
        """
        self._name = name
        self._group = group
        self._frozen = freeze

    @property
    def frozen(self) -> bool:
        """
        Check if the class is frozen.
        """
        return self._frozen

    @frozen.setter
    @check_frozen
    def frozen(self, value: bool) -> None:
        """
        Set the frozen value.
        """
        self._frozen = value

    @frozen.getter
    def frozen(self) -> bool:
        """
        Get the frozen value.
        """
        return self._frozen

    @frozen.deleter
    @check_frozen
    def frozen(self) -> None:
        """
        Delete the frozen value.
        """
        del self._frozen

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
        del self._group

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

    def check_alias(self, aliases: List[str]) -> bool:
        for value in self.group.values():
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
        for k in self.group.keys():
            if k == key:
                return True
        else:
            return False

    def check_type(self, type_: ValueType) -> bool:
        for value_type in self.group.values():
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

        self.group[_name] = type_

    @check_frozen
    def remove(self, aliases: Optional[List[str]] = None, name: Optional[str] = None) -> None:
        """
        Remove a value type from the group.
        """

        print(aliases, name)
        if aliases is None and name is None:
            raise ValueError("You must specify at least one of the two parameters.")

        if aliases is not None and name is not None:
            raise ValueError("You must specify only one of the two parameters.")

        entries = []

        if aliases is not None:
            print(aliases)
            if not self.check_alias(aliases):
                raise ValueError(f"The alias '{aliases}' is not in use.")
            else:
                # for alias in aliases:
                for key, entry in self.group.items():
                    print(entry)
                    for alias in aliases:
                        print(alias)
                        if entry.check_alias(alias):
                            print("ok")
                            entries.append(key)

        print(entries)
        if name is not None:
            if not self.check_name(name):
                raise ValueError(f"The name '{name}' is not in use.")
            else:
                entries.append(self.group[name])

        for entry in entries:
            del self.group[entry]

    @check_frozen
    def freeze(self) -> None:
        """
        Freeze the class group.
        """
        self.frozen = True
        for value_type in self.group.values():
            value_type.freeze()

    def has_alias(self, alias: str) -> Any:
        """
        Returns the alias.
        """
        for key, value_type in self.group.items():
            if value_type.check_alias(alias):
                return key

    def get_aliases(self) -> List[str]:
        """
        Returns the aliases.
        """
        aliases = []
        for type_ in self.group.values():
            for alias in type_.aliases:
                aliases.append(alias)
        return aliases

    def get_value_type(self, alias: Optional[str] = None, value_type_id: Optional[str] = None) -> ValueType:
        """
        Returns the value type.
        """
        for id_, value_type in self.group.items():
            if value_type.check_alias(alias):
                return value_type
            if id_ == value_type_id:
                return value_type