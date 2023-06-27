import json
import uuid

from dataclasses import dataclass
from typing import Any, Optional

from .super import Super__

_FORCE_SUPER_TYPE = False


@dataclass
class Value_(Super__):
    """
    Manages the value of the unit object.
    """
    _value: Any = None

    def __init__(self, value: Optional[Any] = None, super_type: Optional[str] = None) -> None:
        """
        Initializes the Value_ class.
        """
        self.set_value(value, super_type)

    def set_value(self, value: Optional[Any] = None, super_type: Optional[str] = None) -> None:
        """
        Set the value of the unit object.
        """
        if value is not None:
            self._value = value
        else:
            self._value = uuid.uuid4().hex

        passed_value_type = self.get_value_super_type()

        if passed_value_type == super_type:
            if super_type is not None:
                self.force_super_type(super_type)
        elif _FORCE_SUPER_TYPE:
            self.force_super_type("str")

    def get_value(self) -> Any:
        """
        Returns the value of the unit object.
        """
        return self._value

    def get_value_super_type(self) -> str:
        """
        Returns the super type of the value.
        """
        return type(self._value).__name__

    def is_value_super_type(self, value_super_type_name: str) -> bool:
        """
        Returns whether the value is of the given super type.
        """
        return self.get_value_super_type() == value_super_type_name

    def force_super_type(self, value_super_type_name: str) -> None:
        """
        Forces the value to be of the given super type.
        """
        if not self.is_value_super_type(value_super_type_name):
            try:
                match value_super_type_name:
                    case "str":
                        self._value = str(self._value)
                    case "int":
                        self._value = int(self._value)
                    case "float":
                        self._value = float(self._value)
                    case "bool":
                        self._value = bool(self._value)
                    case "list":
                        self._value = list(self._value)
                    case "dict":
                        self._value = dict(self._value)
                    case "tuple":
                        self._value = tuple(self._value)
                    case "set":
                        self._value = set(self._value)
                    case "frozenset":
                        self._value = frozenset(self._value)
                    case "bytes":
                        self._value = bytes(self._value)
                    case _:
                        self._value = self
                        raise ValueError(
                            f"Unknown super type: {value_super_type_name}"
                        )
            except ValueError as error:
                raise ValueError(
                    f"Could not force value to be of the given super type: {error}"
                )

    def to_dict(self) -> dict:
        """
        Returns the dictionary representation of the value.
        """
        return {
            "value": self.get_value(),
            "value_super_type": self.get_value_super_type(),
        }

    # def to_json(self) -> dict:
    #     """
    #     Returns the JSON representation of the value.
    #     """
    #     return json.loads(self.to_json())

    def to_json(self) -> str:
        """
        Returns the JSON representation of the value.
        """
        return json.dumps(self.to_dict())

    def to_json_file(self, value_json_file_path: str) -> None:
        """
        Writes the JSON representation of the value to the given file path.
        """
        with open(value_json_file_path, "w") as value_json_file:
            value_json_file.write(self.to_json())

    @staticmethod
    def from_dict(value_dict: dict) -> 'Value_':
        """
        Returns the value object from the given dictionary.
        """
        return Value_(
            value_dict["value"],
            value_dict["value_super_type"],
        )

    @staticmethod
    def from_json(value_json: str) -> 'Value_':
        """
        Returns the value object from the given JSON.
        """
        return Value_.from_dict(json.loads(value_json))

    @staticmethod
    def from_json_file(value_json_file_path: str) -> 'Value_':
        """
        Returns the value object from the given JSON file.
        """
        with open(value_json_file_path, "r") as value_json_file:
            return Value_.from_json(value_json_file.read())

    def __str__(self) -> str:
        return str(self.to_json())

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: Any) -> bool:
        return self.to_json() == other.get_json()

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)
