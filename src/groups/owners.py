from attrs import define, field
from typing import Any, List, Dict

from .unit import Unit, UnitGenerator, UnitTypeRef, UnitTypePool

__DEFAULT_NONCE_UNIT_TYPE_ALIAS__: str = "int"
__DEFAULT_NONCE_UNIT_TYPE_DIVIDER__: str = "."
__DEFAULT_NONCE_UNIT_ALLOWED_TYPES__: tuple = ("int", "integer")


@define(frozen=True, slots=True)
class Ownership:
    owners: tuple[Unit] = field(factory=tuple)

    def __attrs_init__(self, owners: tuple[Unit] = None):
        if owners is None:
            self.owners = None
        else:
            self.owners = owners