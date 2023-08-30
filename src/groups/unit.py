from attrs import define, field
from typing import Any

from .unit_type_ref import UnitTypeRef


@define(slots=True, frozen=True)
class Unit:
    value: Any = field(default=None)
    type_ref: UnitTypeRef = field(default=None)
