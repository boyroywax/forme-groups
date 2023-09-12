from attrs import define, field
from typing import Any

from .unit import Unit, UnitGenerator, UnitTypeRef

__DEFAULT_NONCE_UNIT_TYPE_ALIAS__ = "int"
__DEFAULT_NONCE_UNIT_TYPE_DIVIDER__ = "."
__DEFAULT_NONCE_UNIT_ALLOWED_TYPES__ = ("int", "integer")


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

    def next_active_value(self) -> Unit:
        type_ = self.active_unit().type_ref.alias
        print(type_)
        match(type_):
            case("int" | "integer"):
                return Unit(value=self.active_unit().value + 1, type_ref=self.active_unit().type_ref)
            
            case("str" | "string"):
                return ValueError("Nonce active unit type not supported.")

            case _:
                raise ValueError("Nonce active unit type not supported.")


@define(frozen=True, slots=True)
class Ownership:
    owners: tuple[Unit] = field(factory=tuple)

    def __init__(self, owners: tuple[Unit] = None):
        if owners is None:
            self.owners = tuple()
        else:
            self.owners = owners


@define(frozen=True, slots=True)
class Credentials:
    credentials: tuple[Unit] = field(factory=tuple)

    def __init__(self, credentials: tuple[Unit] = None):
        if credentials is None:
            self.credentials = tuple()
        else:
            self.credentials = credentials


@define(frozen=True, slots=True)
class Data:
    entries: tuple[Unit] = field(factory=tuple)

    def __init__(self, data: tuple[Unit] = None):
        if data is None:
            self.entries = tuple()
        else:
            self.entries = data


@define(frozen=True, slots=True)
class GroupUnit:
    nonce: Nonce = field(default=Nonce)
    ownership: Ownership = field(default=Ownership)
    credentials: Credentials = field(default=Credentials)
    data: Data = field(default=Data)


class GroupUnitGenerator:
    unit_generator: UnitGenerator = field(default=None)

    def __init__(self, unit_generator: UnitGenerator = None):
        if unit_generator is None:
            self.unit_generator = UnitGenerator()
        else:
            self.unit_generator = unit_generator

    def create_nonce(self, nonce: tuple[Unit] = None) -> Nonce:
        if nonce is None:
            return Nonce(units=(self.unit_generator.create_unit(alias=__DEFAULT_NONCE_UNIT_TYPE_ALIAS__, value=0),))
        
        for unit in nonce:
            if unit.type_ref.alias not in __DEFAULT_NONCE_UNIT_ALLOWED_TYPES__:
                raise ValueError("Nonce unit type must be int or integer. " + unit.type_ref.alias + " is not supported.")
        return Nonce(units=nonce)

    def create_ownership(self, ownership: tuple[Unit] = None) -> Ownership:
        if ownership is None:
            return Ownership(units=(self.unit_generator.create_unit(alias="str", value="did:eosio:ab.testaccount"),))
        return Ownership(units=ownership)

    def create_credentials(self, credentials: tuple[Unit] = None) -> Credentials:
        if credentials is None:
            return Credentials(units=(self.unit_generator.create_unit(alias="str", value="did:ab.testaccount"),))
        return Credentials(units=credentials)

    def create_data(self, data: tuple[Unit] = None) -> Data:
        if data is None:
            return Data(units=(self.unit_generator.create_unit(alias="str", value="test_data"),))
        return Data(units=data)

    def create_group_unit(self, nonce: Nonce = None, ownership: Ownership = None, credentials: Credentials = None, data: Data = None) -> GroupUnit:
        return GroupUnit(
            nonce=self.create_nonce(nonce.units),
            ownership=self.create_ownership(ownership.owners),
            credentials=self.create_credentials(credentials.credentials),
            data=self.create_data(data.entries)
        )
