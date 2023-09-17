from attrs import define, field
from typing import Any, List, Dict

from .unit import Unit, UnitGenerator, UnitTypeRef, UnitTypePool

__DEFAULT_NONCE_UNIT_TYPE_ALIAS__: str = "int"
__DEFAULT_NONCE_UNIT_TYPE_DIVIDER__: str = "."
__DEFAULT_NONCE_UNIT_ALLOWED_TYPES__: tuple = ("int", "integer")


@define(frozen=True, slots=True)
class Nonce:
    units: tuple[Unit] = field(factory=tuple)

    def __attrs_init__(self, units: tuple[Unit] = None):
        if units is None:
            self.units = (Unit(value=0, type_ref=UnitTypeRef(alias="int")),)
        else:
            self.units = units

    def active_unit(self) -> Unit:
        return self.units[-1]

    def next_active_unit(self) -> Unit:
        match(self.active_unit().type_ref.alias):
            case("int" | "integer"):
                return Unit(value=self.active_unit().value + 1, type_ref=self.active_unit().type_ref)

            case("str" | "string"):
                raise ValueError("Nonce active unit type not supported.")

            case _:
                raise ValueError("Nonce active unit type not supported.")

    def next_active_nonce(self) -> 'Nonce':
        return Nonce(units=self.units[:-1] + (self.next_active_unit(),))

    def __str__(self) -> str:
        nonce_string = ""
        for unit in self.units:
            nonce_string += str(unit.value) + __DEFAULT_NONCE_UNIT_TYPE_DIVIDER__
        return nonce_string[:-1]

    def __repr__(self) -> str:
        return self.__str__()