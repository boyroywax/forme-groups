import json
from dataclasses import dataclass
from typing import Optional, List, Dict

from groups.modules.base_unit import BaseUnitType


@dataclass(
    init=True,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False,
    match_args=True,
    kw_only=False,
    slots=False,
    weakref_slot=False
)
class BaseUnit():
    """
    An UniversalObject's base unit
    Units value is expected to to be string.
    Unit Type is expected to be supplied a BaseUnitType class.
    - param value: The value
    - param type: The type in BaseUnitType class format
    """

    _value: str = "Universal serializable object base unit"
    _type: BaseUnitType = BaseUnitType("string")

    def get_value(self) -> str:
        """
        Returns the value.
        """
        return self._value

    def set_value(self, value: str) -> None:
        """
        Sets the value.
        """
        self._value = value

    def get_type(self) -> BaseUnitType:
        """
        Returns the type.
        """
        return self._type

    def set_type(self, type: BaseUnitType) -> None:
        """
        Sets the type.
        """
        self._type = type

    def to_json_string(self) -> str:
        """
        Returns the object in a JSON string format.
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def to_json(self) -> Dict:
        """
        Returns the object in a JSON format.
        """
        return json.loads(self.to_json_string())

    def from_json_string(self, json_string: str) -> None:
        """
        Loads the object from a JSON string.
        """
        self.__dict__ = json.loads(json_string)

    def from_json(self, json_object: Dict) -> None:
        """
        Loads the object from a JSON object.
        """
        self.__dict__ = json_object
