from attrs import define, field, validators

from .log import Log


__DEFAULT_UNIT_TYPE_REF__ = "string"

@define(frozen=True, slots=True)
class UnitTypeRef:
    """A reference to a unit type.

    """
    _type_ref: str = field(default=__DEFAULT_UNIT_TYPE_REF__, validator=validators.instance_of(str))

    def __init__(self, type_ref: str = __DEFAULT_UNIT_TYPE_REF__):
        """Create a new unit type reference.

        Args:
            type_ref: The type reference.

        """
        object.__setattr__(self, "_type_ref", type_ref)
        Log().logger.debug("Created unit type reference: %s", self)

    @property
    def type_ref(self) -> str:
        """The type reference.

        """
        return self._type_ref

    @type_ref.getter
    def type_ref(self) -> str:
        return self._type_ref

    def __str__(self) -> str:
        return self.type_ref

    def __repr__(self) -> str:
        return f"UnitTypeRef(type_ref={self.type_ref})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, UnitTypeRef):
            return False
        return self.type_ref == other.type_ref

    def __hash__(self) -> int:
        return hash(self.type_ref)
