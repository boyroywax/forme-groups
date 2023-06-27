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
        id: Optional[UnitValue] = None,
        alias: Optional[UnitValue] = None,
        prefix: Optional[UnitValue] = None,
        suffix: Optional[UnitValue] = None,
        separator: Optional[UnitValue] = None,
        super: Optional['Type_'] = None,
        system_function: Optional[Callable] = None
    ) -> None:
        """
        Initializes the Type_ class.
        """
        if id is not None:
            self.set_id(id)

        if alias is not None:
            self.set_alias(alias)

        if prefix is not None:
            self.set_prefix(prefix)

        if suffix is not None:
            self.set_suffix(suffix)

        if separator is not None:
            self.set_separator(separator)

        if super is not None:
            self.set_super(super)

        if system_function is not None:
            self.set_system_function(system_function)

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

    def set_separator(self, separator: UnitValue) -> None:
        """
        Sets the separator of the unit type.
        """
        self.separator = separator

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
            "id": self.get_id().get_value() if self.get_id() is not None else None,
            "alias": self.get_alias().get_value() if self.get_alias() is not None else None,
            "prefix": self.get_prefix().get_value() if self.get_prefix() is not None else None,
            "suffix": self.get_suffix().get_value() if self.get_suffix() is not None else None,
            "separator": self.get_separator().get_value() if self.get_separator() is not None else None,
            "super": self.get_super().get_id().get_value() if self.get_super() is not None else None,
            "system_function": self.get_system_function() if self.get_system_function() is not None else None,
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
            id=data.get("id"),
            alias=data.get("alias"),
            prefix=data.get("prefix"),
            suffix=data.get("suffix"),
            separator=data.get("separator"),
            super=data.get("super"),
            system_function=data.get("system_function"),
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
