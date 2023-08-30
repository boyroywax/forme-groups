from attrs import define, field
from typing import List

from .unit_type import UnitType
from .unit_type_ref import UnitTypeRef


@define(slots=True)
class UnitTypePool:
    """A pool of unit types."""

    unit_types: List[UnitType] = field(factory=list)
