from abc import ABC, abstractmethod
from dataclasses import dataclass, field, InitVar, is_dataclass
from typing import Any, Dict, List, Optional


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
    def type(self) -> str:
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
    def type(self) -> List[str]:
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

    def __init__(self, name: str, group: Dict[str, ValueType], freeze: Optional[bool] = False) -> None:
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
    def group(self) -> Dict[str, ValueTypeInterface]:
        """
        The group of the value types.
        """
        return self._group
    
    @group.setter
    @check_frozen
    def group(self, value: Dict[str, ValueTypeInterface]) -> None:
        """
        Set the group of the value types.
        """
        self._group = value

    @group.getter
    def group(self) -> Dict[str, ValueTypeInterface]:
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

    def check_alias(self, alias: str) -> bool:
        for value_type in self.group.values():
            if value_type.check_alias(alias):
                return True
            
    def check_name(self, name: str) -> bool:
        for value_type in self.group.values():
            if value_type.name == name:
                return True

    @check_frozen
    def add(self, alias: str, type_: ValueTypeInterface) -> None:
        """
        Add a value type to the group.
        """
        if self.check_alias(alias):
            raise ValueError(f"The alias '{alias}' is already in use.")
        if self.check_name(type_.name):
            raise ValueError(f"The name '{type_.name}' is already in use.")
        self.group[alias] = type_

    @check_frozen
    def remove(self, alias: str) -> None:
        """
        Remove a value type from the group.
        """
        if not self.check_alias(alias):
            for group in self.group.values():
                if group.check_alias(alias):
                    alias = group.alias
                    break
            raise ValueError(f"The alias '{alias}' is not in use.")
        del self.group[alias]

    @check_frozen
    def freeze(self) -> None:
        """
        Freeze the class group.
        """
        self.frozen = True
        for value_type in self.group.values():
            value_type.freeze()


