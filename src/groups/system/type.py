import json

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Callable, Any


@dataclass
class SystemType():
    """
    A Class that represents a System Type.
    """

    id: Optional[str] = None
    alias: List[str] = field(default_factory=list)
    super: Optional['SystemType'] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    separator: Optional[str] = None
    system_function: Optional[Callable[[Any], Any]] = None

    def __post_init__(self):
        """
        Initializes the 'SystemType' class.
        """
        if self.id is not None:
            self.set_id(self.id)

        if self.alias is not None:
            self.set_alias(self.alias)

        if self.super is not None:
            self.set_super(self.super)

        if self.prefix is not None:
            self.set_prefix(self.prefix)

        if self.suffix is not None:
            self.set_suffix(self.suffix)

        if self.separator is not None:
            self.set_separator(self.separator)

    def set_id(self, id: str) -> None:
        """
        Sets the id.
        """
        self.id = id

    def set_alias(self, alias: List[str]) -> None:
        """
        Sets the alias.
        """
        self.alias = alias

    def set_super(self, super: 'SystemType') -> None:
        """
        Sets the super.
        """
        self.super = super

    def set_prefix(self, prefix: str) -> None:
        """
        Sets the prefix.
        """
        self.prefix = prefix

    def set_suffix(self, suffix: str) -> None:
        """
        Sets the suffix.
        """
        self.suffix = suffix

    def set_separator(self, separator: str) -> None:
        """
        Sets the separator.
        """
        self.separator = separator

    def set_system_function(self, system_function: Callable[[Any], Any]) -> None:
        """
        Sets the system_function.
        """
        self.system_function = system_function

    def get_id(self) -> str:
        """
        Returns the id.
        """
        return self.id

    def get_alias(self) -> List[str]:
        """
        Returns the alias.
        """
        return self.alias

    def get_super(self) -> Optional['SystemType']:
        """
        Returns the super.
        """
        return self.super

    def get_prefix(self) -> Optional[str]:
        """
        Returns the prefix.
        """
        return self.prefix

    def get_suffix(self) -> Optional[str]:
        """
        Returns the suffix.
        """
        return self.suffix

    def get_separator(self) -> Optional[str]:
        """
        Returns the separator.
        """
        return self.separator

    def get_system_function(self) -> Optional[Callable[[Any], Any]]:
        """
        Returns the system_function.
        """
        return self.system_function

    def __str__(self) -> str:
        """
        Returns the string representation.
        """
        return self.id

    def __repr__(self) -> str:
        """
        Returns the string representation.
        """
        return self.__str__()

    def __eq__(self, other: 'SystemType') -> bool:
        """
        Returns the equality.
        """
        return self.id == other.id

    def __ne__(self, other: 'SystemType') -> bool:
        """
        Returns the inequality.
        """
        return not self.__eq__(other)

    def __hash__(self) -> int:
        """
        Returns the hash.
        """
        return hash(self.id)

    def to_dict(self) -> Dict:
        """
        Returns the dict representation.
        """
        return {
            "id": self.id,
            "alias": self.alias,
            "super": self.super,
            "prefix": self.prefix,
            "suffix": self.suffix,
            "separator": self.separator,
            "system_function": self.system_function
        }

    def to_json(self) -> str:
        """
        Returns the json representation.
        """
        return json.dumps(self.to_dict())

    def to_json_file(self, file: str) -> None:
        """
        Writes the json representation to the file.
        """
        with open(file, "w") as f:
            f.write(self.to_json())

    @staticmethod
    def from_dict(dict: Dict) -> 'SystemType':
        """
        Returns the SystemType from the dict.
        """
        return SystemType(
            id=dict["id"],
            alias=dict["alias"],
            super=dict["super"],
            prefix=dict["prefix"],
            suffix=dict["suffix"],
            separator=dict["separator"],
            system_function=dict["system_function"]
        )

    @staticmethod
    def from_json(json: str) -> 'SystemType':
        """
        Returns the SystemType from the json.
        """
        return SystemType.from_dict(dict=json)
