import json
from dataclasses import dataclass
from typing import Optional, List, Dict


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
class Unit():
    """
    An UniversalObject's base unit
    Units are expected to be strings
    :param unit: The unit
    """

    _value: str = "Universal serializable object base unit"
    _type: str = "string"

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

    def get_type(self) -> str:
        """
        Returns the type.
        """
        return self._type
    
    def set_type(self, type: str) -> None:
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
class UnitList():
    """
    An UniversalObject's unit
    All units are stored in a list
    Units are expected to be strings
    :
    
    """

    def __init__(self, unit: List[Unit]) -> None:
        """
        Constructor for the Unit class.
        """
        self._unit: List[str] = unit

    def get_unit(self) -> List:
        """
        Returns the unit.
        """
        return self._unit
    
    def set_unit(self, unit: List) -> None:
        """
        Sets the unit.
        """
        self._unit = unit

    def get_unit_length(self) -> int:
        """
        Returns the length of the unit.
        """
        return len(self._unit)
    
    def add_unit(self, unit: str) -> None:
        """
        Adds a unit to the unit.
        """
        self._unit.append(unit)

    def remove_unit(self, unit_index: int) -> None:

    
