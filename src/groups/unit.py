from attrs import define, field
from typing import Any


@define(slots=True, frozen=True)
class Unit:
    value: Any = field(default=None)
    type_ref: Any = field(default=None)