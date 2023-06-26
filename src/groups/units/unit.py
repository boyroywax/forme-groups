from dataclasses import dataclass, field
from typing import Optional

from .value import Value_ as UnitValue
from .type import Type_ as UnitType


@dataclass
class Unit():
    _value: UnitValue = field(default_factory=UnitValue())
    _type: UnitType = field(default_factory=UnitType())

    def __init__(
        self,
        value_: Optional[UnitValue] = None,
        type_: Optional[UnitType] = None
    ) -> None:
        """
        Initializes the Unit class.
        """
        if value_ is not None:
            self.set_value(value_)

        if type_ is not None:
            self.set_type(type_)

    def set_value(self, value_: UnitValue) -> None:
        """
        Sets the value of the unit.
        """
        self._value = UnitValue(value_)

    def set_type(self, type_: UnitType) -> None:
        """
        Sets the type of the unit.
        """
        self._type = UnitType(type_)

    def get_value(self) -> UnitValue:
        """
        Gets the value of the unit.
        """
        return self._value

    def get_type(self) -> UnitType:
        """
        Gets the type of the unit.
        """
        return self._type

    def to_dict(self) -> dict:
        """
        Returns the dictionary representation of the unit.
        """
        return {
            "value": self.get_value().to_dict(),
            "type": self.get_type().to_dict(),
        }

    def __str__(self) -> str:
        """
        Returns the string representation of the unit.
        """
        return f"value: {self.get_value().get_value()} type: {self.get_type().to_json()}"
