from attrs import define, field, validators


@define(slots=True, frozen=True)
class UnitTypeRef:
    """A reference to a unit type."""

    alias = field(type=str, validator=validators.instance_of(str))

    def __str__(self):
        return self.alias
    
    def __repr__(self):
        return f"UnitTypeRef({self.alias!r})"
    
    def __eq__(self, other):
        if isinstance(other, UnitTypeRef):
            return self.alias == other.alias
        return NotImplemented
    
    def __hash__(self):
        return hash(self.alias)