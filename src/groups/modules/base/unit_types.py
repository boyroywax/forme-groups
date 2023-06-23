import json
from dataclasses import dataclass, field
from typing import List, Optional

from .type import BaseUnitType
from .unit_types_defaults import _DEFUALT_UNIT_TYPES_LIST


@dataclass(
    init=False,
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
class BaseUnitTypes():
    """
    The UnitType class manages the unit types.
    A Unit object can only have a single unit type.  Defaults to a string.
    The default unit type list containts only an entry for string
    - param unit_types_list: A list of unit types
    """

    _unit_types_list: List[BaseUnitType] = field(
        default_factory=lambda: List[BaseUnitType])

    def __init__(
            self,
            unit_types_list: Optional[List[BaseUnitType]] = None,
    ) -> None:
        """
        Constructor for the UnitType class.  Defaults are loaded if no unit types list is provided.
        """
        if unit_types_list is not None:
            self.set_unit_types_list(unit_types_list)
        else:
            self.set_unit_types_list(_DEFUALT_UNIT_TYPES_LIST)

    def get_unit_types_list(self) -> List[BaseUnitType]:
        """
        Returns the unit types list.
        """
        return self._unit_types_list

    def set_unit_types_list(self, unit_types_list: List[BaseUnitType]) -> None:
        """
        Sets the unit types list.
        """
        self._unit_types_list = unit_types_list

    def add_unit_type(self, unit_type: BaseUnitType) -> None:
        """
        Adds a unit type to the unit types list.
        """
        self._unit_types_list.append(unit_type)

    def remove_unit_type(self, unit_type: BaseUnitType) -> None:
        """
        Removes a unit type from the unit types list.
        """
        self._unit_types_list.remove(unit_type)

    def get_unit_type(self, index: int) -> BaseUnitType:
        """
        Returns the unit type at the specified index.
        """
        return self._unit_types_list[index]

    def set_unit_type(self, index: int, unit_type: BaseUnitType) -> None:
        """
        Sets the unit type at the specified index.
        """
        self._unit_types_list[index] = unit_type

    def get_unit_type_count(self) -> int:
        """
        Returns the number of unit types in the unit types list.
        """
        return len(self._unit_types_list)

    def verify_unit_type_is_allowed(self, unit_type: BaseUnitType) -> bool:
        """
        Verifies that the specified unit type is allowed.
        """
        return unit_type in self._unit_types_list

    def to_json_string(self) -> str:
        """
        Returns the object in a JSON string format.
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
