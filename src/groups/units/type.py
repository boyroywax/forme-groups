import json

from .value import Value_ as UnitValue
from dataclasses import dataclass
from typing import Optional, Callable


@dataclass
class Type_():
    """
    Manages the type of the unit object.
    """

    id: Optional[UnitValue] = None
    alias: Optional[UnitValue] = None
    prefix: Optional[UnitValue] = None
    suffix: Optional[UnitValue] = None
    separator: Optional[UnitValue] = None
    super: Optional['Type_'] = None
    system_function: Optional[Callable] = None

    def __init__(
        self,
        id_: Optional[UnitValue] = None,
        alias_: Optional[UnitValue] = None,
        prefix_: Optional[UnitValue] = None,
        suffix_: Optional[UnitValue] = None,
        separator_: Optional[UnitValue] = None,
        super_: Optional['Type_'] = None,
        system_function_: Optional[Callable] = None,
    ) -> None:
        """
        Initializes the Type_ class.
        """
        if id_ is not None:
            self.set_id(id_)

        if alias_ is not None:
            self.set_alias(alias_)

        if prefix_ is not None:
            self.set_prefix(prefix_)

        if suffix_ is not None:
            self.set_suffix(suffix_)

        if separator_ is not None:
            self.set_separator(separator_)

        if super_ is not None:
            self.set_super(super_)

        if system_function_ is not None:
            self.set_system_function(system_function_)

    def set_id(self, id_: UnitValue) -> None:
        """
        Sets the id of the unit type.
        """
        self.id = id_

    def set_alias(self, alias_: UnitValue) -> None:
        """
        Sets the alias of the unit type.
        """
        self.alias = alias_

    def set_prefix(self, prefix_: UnitValue) -> None:
        """
        Sets the prefix of the unit type.
        """
        self.prefix = prefix_

    def set_suffix(self, suffix_: UnitValue) -> None:
        """
        Sets the suffix of the unit type.
        """
        self.suffix = suffix_

    def set_separator(self, separator_: UnitValue) -> None:
        """
        Sets the separator of the unit type.
        """
        self.separator = separator_

    def set_super(self, super_: 'Type_') -> None:
        """
        Sets the super of the unit type.
        """
        self.super = super_

    def set_system_function(self, system_function_: Callable) -> None:
        """
        Sets the system function of the unit type.
        """
        self.system_function = system_function_
    
    def get_id(self) -> UnitValue:
        """
        Gets the id of the unit type.
        """
        return self.id

    def get_alias(self) -> UnitValue:
        """
        Gets the alias of the unit type.
        """
        return self.alias
    
    def get_prefix(self) -> UnitValue:
        """
        Gets the prefix of the unit type.
        """
        return self.prefix
    
    def get_suffix(self) -> UnitValue:
        """
        Gets the suffix of the unit type.
        """
        return self.suffix
    
    def get_separator(self) -> UnitValue:
        """
        Gets the separator of the unit type.
        """
        return self.separator
    
    def get_super(self) -> 'Type_':
        """
        Gets the super of the unit type.
        """
        return self.super
    
    def get_system_function(self) -> Callable:
        """
        Gets the system function of the unit type.
        """
        return self.system_function
    
    def to_dict(self) -> dict:
        """
        Returns the JSON representation of the unit type.
        """
        return {
            "id": self.get_id(),
            "alias": self.get_alias(),
            "prefix": self.get_prefix(),
            "suffix": self.get_suffix(),
            "separator": self.get_separator(),
            "super": self.get_super(),
            "system_function": self.get_system_function(),
        }
    
    def to_json(self) -> str:
        """
        Returns the JSON representation of the unit type.
        """
        return json.dumps(self.to_dict())
    
    def to_json_file(self, path: str) -> None:
        """
        Returns the JSON representation of the unit type.
        """
        with open(path, "w") as file:
            file.write(self.to_json())

    @staticmethod
    def from_dict(data: dict) -> 'Type_':
        """
        Returns the unit type from the JSON representation.
        """
        return Type_(
            id_=data.get("id"),
            alias_=data.get("alias"),
            prefix_=data.get("prefix"),
            suffix_=data.get("suffix"),
            separator_=data.get("separator"),
            super_=data.get("super"),
            system_function_=data.get("system_function"),
        )
    
    @staticmethod
    def from_json(data: str) -> 'Type_':
        """
        Returns the unit type from the JSON representation.
        """
        return Type_.from_dict(json.loads(data))
    
    @staticmethod
    def from_json_file(path: str) -> 'Type_':
        """
        Returns the unit type from the JSON file.
        """
        with open(path, "r") as file:
            return Type_.from_json(file.read())
    
    def __str__(self) -> str:
        """
        Returns the string representation of the unit type.
        """
        return f"{self.get_id()}"
    
    def __repr__(self) -> str:
        """
        Returns the string representation of the unit type.
        """
        return f"{self.get_id()}"

