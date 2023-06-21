import json
from dataclasses import dataclass
from typing import Dict


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
class BaseUnitType():
    """
    The UnitType class manages the unit types.
    A Unit object can only have a single unit type.
    """

    _unit_types: Dict = {
        'string': ['string', 'str'],
        'integer': ['integer', 'int'],
        'float': ['float'],
        'boolean': ['boolean', 'bool'],
        'list': ['list'],
        'tuple': ['tuple'],
        'dictionary': ['dictionary', 'dict'],
        'hexadecimal': ['hexadecimal', 'hex'],
        'binary': ['binary'],
        'decimal': ['decimal'],
        'unknown': ['unknown']
    }

    _unit_type: str = "string"

    def check_for_type(self, unit_type: str) -> bool:
        """
        Check if the unit type exists.
        Either as a key or a value in the dictionary.
        """
        if unit_type in self._unit_types.keys():
            return True
        elif unit_type in self._unit_types.values():
            return True
        else:
            return False

    def get_unit_types(self) -> Dict:
        """
        Returns the unit types.
        """
        return self._unit_types

    def get_unit_type(self) -> str:
        """
        Returns the unit type.
        """
        return self._unit_type

    def set_unit_type(self, unit_type: str) -> None:
        """
        Sets the unit type.
        """
        if self.check_for_type(unit_type):
            self._unit_type = unit_type
        else:
            raise ValueError(f"Unit type {unit_type} does not exist.")

    def to_json(self) -> Dict:
        """
        Returns the unit type as a dictionary.
        """
        return {"unit_type": self._unit_type}

    def from_json(self, unit_type: str) -> None:
        """
        Sets the unit type from a dictionary.
        """
        return json.loads(unit_type)
