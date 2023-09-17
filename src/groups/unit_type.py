from attrs import define, field, validators

from .unit_type_ref import UnitTypeRef


@define(slots=True, frozen=True)
class UnitType:
    """A type of unit."""

    name = field(type=str, validator=validator.instance_of(str))
    """The name of the unit type."""

    def __str__(self):
        return self.name