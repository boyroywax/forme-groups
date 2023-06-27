from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .base import Unit, UnitValue, UnitType

@dataclass
class Nonce(Unit):
    """
    Manages the nonce of the group object.
    """
    def __init__(
        self,
        value_: Optional[UnitValue] = None,
        type_: Optional[UnitType] = None
    ) -> None:
        """
        Initializes the Nonce class.
        """
        super().__init__(value_, type_)
        self.set_type_obj(UnitType('nonce'))

    def set_value_obj(self, value_: UnitValue) -> None:
        """
        Sets the value of the nonce.
        """
        if value_.super_type is None:
            super().set_value_obj(value_)
        else:
            raise ValueError(f'Cannot set nonce value with super type {value_.super_type}')

    def create_and_set_value(self, value: str) -> None:
        """
        Creates and sets the value of the nonce.
        """
        super().create_and_set_value(value)

    def create_and_set_value_from_dict(self, value_dict: dict) -> None:
        """
        Creates and sets the value of the nonce from the given dictionary.
        """
        super().create_and_set_value_from_dict(value_dict)

    def create_and_set_value_from_json(self, value_json: str) -> None:
        """
        Creates and sets the value of the nonce from the given JSON.
        """
        super().create_and_set_value_from_json(value_json)

    @staticmethod
    def generate_unit(unit_value: UnitValue, unit_type: UnitType) -> Unit:
        """
        Generates a nonce.
        """
        return Nonce(unit_value, unit_type)

    @staticmethod
    def generate_value(value: str) -> UnitValue:
        """
        Generates a nonce value.
        """
        return UnitValue(value)