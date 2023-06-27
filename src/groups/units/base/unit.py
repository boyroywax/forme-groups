from dataclasses import dataclass
from typing import Optional, Dict

from .value import Value_ as UnitValue
from .type import Type_ as UnitType


@dataclass
class Unit(UnitType, UnitValue):
    """
    Manages the unit object.
    """

    def __init__(
        self,
        value: Optional[UnitValue] = None,
        type: Optional[UnitType] = None
    ) -> None:
        """
        Initializes the Unit class.
        """
        if value is not None:
            super(UnitType, self).__init__(type)

        if type is not None:
            super(UnitValue, self).__init__(value)

    def set_value(self, value: UnitValue) -> None:
        """
        Sets the value of the unit.
        """
        if value is not None:
            super(UnitType, self).set_type(value)
        else:
            raise ValueError('Cannot set value to None')

    def set_type(self, type: UnitType) -> None:
        """
        Sets the type of the unit.
        """
        if type is not None:
            super(UnitValue, self).set_value(type)
        else:
            raise ValueError('Cannot set type to None')
