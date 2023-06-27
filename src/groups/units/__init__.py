# from dataclasses import dataclass, field
# from typing import Any, Optional

from .base import Unit, UnitValue, UnitType
from .nonce import Nonce

# @dataclass
# class Units():
#     _units: list[Unit] = field(default_factory=list)

#     def __init__(self, units: list[Unit] = None) -> None:
#         """
#         Initializes the Units class.
#         """
#         if units is not None:
#             self.set_units(units)

#     def set_units(self, units: list[Unit]) -> None:
#         """
#         Sets the units.
#         """
#         self._units = units

#     def get_units(self) -> list[Unit]:
#         """
#         Gets the units.
#         """
#         return self._units

#     def get_unit(self, unit_index: int) -> Unit:
#         """
#         Gets the unit at the given index.
#         """
#         return self._units[unit_index]

#     def add_unit(self, unit: Unit) -> None:
#         """
#         Adds a unit.
#         """
#         self._units.append(unit)

#     def remove_unit(self, unit_index: int) -> None:
#         """
#         Removes a unit.
#         """
#         del self._units[unit_index]

#     @staticmethod
#     def generate_unit(unit_value: UnitValue, unit_type: UnitType) -> Unit:
#         """
#         Generates a unit.
#         """
#         return Unit(unit_value, unit_type)

#     @staticmethod
#     def generate_value(value: str, super_type: Optional[str] = None) -> UnitValue:
#         """
#         Generates a value.
#         """
#         if super_type is not None:
#             return UnitValue(value, super_type)
#         return UnitValue(value)

#     @staticmethod
#     def generate_type(type_: str, super_type: Optional[str] = None) -> UnitType:
#         """
#         Generates a type.
#         """
#         if super_type is not None:
#             return UnitType(type_, super_type)
#         return UnitType(type_)


__all__ = [
    "Nonce",
    "Unit",
    "UnitValue",
    "UnitType",
]
