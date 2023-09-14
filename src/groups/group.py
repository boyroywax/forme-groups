from attrs import define, field
from typing import Any, List, Dict

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


@define(frozen=True, slots=True)
class Ownership:
    owners: tuple[Unit] = field(factory=tuple)

    def __attrs_init__(self, owners: tuple[Unit] = None):
        if owners is None:
            self.owners = None
        else:
            self.owners = owners


@define(frozen=True, slots=True)
class Credentials:
    credentials: tuple[Unit] = field(factory=tuple)

    def __attrs_init__(self, credentials: tuple[Unit] = None):
        if credentials is None:
            self.credentials = None
        else:
            self.credentials = credentials


@define(frozen=True, slots=True)
class Data:
    entries: tuple[Unit] = field(factory=tuple)

    def __attrs_init__(self, data: tuple[Unit] = None, ):
        if data is None:
            self.entries = None
        else:
            self.entries = data

    def is_schema(self) -> bool:
        schema: bool = False

        if self.entries is not None and len(self.entries) > 0:
            for entry in self.entries:
                if entry.type_ref.alias == "dict":
                    if schema is False:
                        if entry.value["Schema"]:
                            schema = True
                    else:
                        raise ValueError("Multiple schemas found in Data.entries.")
        return schema


@define(frozen=True, slots=True)
class GroupUnit:
    nonce: Nonce = field(default=Nonce)
    ownership: Ownership = field(default=Ownership)
    credentials: Credentials = field(default=Credentials)
    data: Data = field(default=Data)


class GroupUnitGenerator:
    unit_generator: UnitGenerator = field(default=None)

    def __init__(self, unit_generator: UnitGenerator = None, system_types_path: str = None, custom_types_path: str = None):
        if unit_generator is None:
            self.unit_generator = UnitGenerator(system_types_path=system_types_path, custom_types_path=custom_types_path)
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
            return Ownership(owners=(self.unit_generator.create_unit(alias="str", value="did:eosio:ab.testaccount"),))
        return Ownership(owners=ownership)

    def create_credentials(self, credentials: tuple[Unit] = None) -> Credentials:
        if credentials is None:
            return Credentials(credentials=(self.unit_generator.create_unit(alias="str", value="did:ab.testaccount"),))
        return Credentials(credentials=credentials)

    def create_data(self, data: tuple[Unit] = None) -> Data:
        if data is None:
            return Data(entries=(self.unit_generator.create_unit(alias="dict", value={"test": "test_data"}),))
        return Data(entries=data)

    def create_group_unit(self, nonce: Nonce = None, ownership: Ownership = None, credentials: Credentials = None, data: Data = None) -> GroupUnit:
        return GroupUnit(
            nonce=nonce,
            ownership=ownership,
            credentials=credentials,
            data=data
        )


class Group:
    _group_unit_generator: GroupUnitGenerator = None
    group_units: List[GroupUnit] = []
    active_unit: GroupUnit = None

    def __init__(self, group_unit_generator: GroupUnitGenerator = None, system_types_path: str = None, custom_types_path: str = None):
        if group_unit_generator is None:
            self._group_unit_generator = GroupUnitGenerator(system_types_path=system_types_path, custom_types_path=custom_types_path)
        else:
            self._group_unit_generator = group_unit_generator

    def get_all_group_units(self) -> list[GroupUnit]:
        return self.group_units

    def freeze_unit_types(self):
        self._group_unit_generator.unit_generator.unit_type_pool.freeze_pool()

    def get_group_unit_by_nonce(self, nonce: Nonce) -> GroupUnit:
        for group_unit in self.group_units:
            if group_unit.nonce == nonce:
                return group_unit
        return None

    def get_nonce_tiers(self) -> int:
        highest_nonce_tier = 0
        for group_unit in self.group_units:
            if len(group_unit.nonce.units) >= highest_nonce_tier:
                highest_nonce_tier = len(group_unit.nonce.units)
        return highest_nonce_tier

    def get_highest_nonce_by_tier(self, tier: int = 1) -> Nonce:
        if tier < 1:
            raise ValueError("Nonce tier cannot be negative.")
        print("Getting highest nonce by tier: " + str(tier)
                + "\nNonce tiers: " + str(self.get_nonce_tiers()))

        if tier > self.get_nonce_tiers():
            raise ValueError("Nonce tier does not exist. " + str(tier) + " is out of range.")

        highest_nonce_value = 0
        highest_nonce = None
        for group_unit in self.group_units:
            group_unit_tiers = len(group_unit.nonce.units)
            if group_unit_tiers >= tier:
                if group_unit.nonce.units[tier-1].value >= highest_nonce_value:
                    highest_nonce_value = group_unit.nonce.units[tier-1].value
                    highest_nonce = group_unit.nonce

        return highest_nonce

    def get_highest_nonce(self) -> Dict[int, Nonce]:
        tiers = self.get_nonce_tiers()
        highest_nonces: Dict[int, Nonce] = {}

        print(tiers)

        for tier in range(tiers):
            highest_nonces[tier-1] = self.get_highest_nonce_by_tier(tier)
        return highest_nonces

    def new_group_unit(self, nonce: Nonce = None, ownership: Ownership = None, credentials: Credentials = None, data: Data = None) -> GroupUnit:
        # Check that the Nonce is available
        if nonce is not None:
            for group_unit in self.group_units:
                if group_unit.nonce == nonce:
                    raise ValueError("Nonce already exists in GroupUnit.")

        new_group_unit = self._group_unit_generator.create_group_unit(
            nonce=nonce,
            ownership=ownership,
            credentials=credentials,
            data=data
        )

        self.group_units.append(new_group_unit)
        self.active_unit = new_group_unit
        return new_group_unit

    def create_group_unit(self, active_unit: GroupUnit = None, ownership: Ownership = None, credentials: Credentials = None, data: Data = None) -> GroupUnit:
        nonce = None
        if active_unit is None and self.active_unit is None:
            # if len(self.group_units) == 0:
            print("Creating new group unit with default nonce.")
            nonce = self._group_unit_generator.create_nonce()

        elif active_unit is None and self.active_unit is not None:
            print("Creating new group unit from previous nonce.")
            nonce = self.active_unit.nonce.next_active_nonce()

        elif active_unit is not None and self.active_unit is None:
            print("Creating new group unit from active nonce.")
            nonce = active_unit.nonce.next_active_nonce()

        return self.new_group_unit(
            nonce=nonce,
            ownership=ownership,
            credentials=credentials,
            data=data
        )

    def format_group_unit(self, group_unit: GroupUnit = None) -> str:
        if group_unit is None:
            group_unit = self.active_unit

        formatted_group_unit = ""
        formatted_group_unit += "Nonce: " + str(group_unit.nonce) + "\n"

        formatted_group_unit += "Ownership: "
        if group_unit.ownership is not None:
            for owner in group_unit.ownership.owners:
                formatted_group_unit += self._group_unit_generator.unit_generator.format_unit(owner) + ", "

        formatted_group_unit += "\nCredentials: "
        if group_unit.credentials is not None:
            for credential in group_unit.credentials.credentials:
                formatted_group_unit += self._group_unit_generator.unit_generator.format_unit(credential) + ", "

        formatted_group_unit += "\nData: "
        if group_unit.data is not None:
            for entry in group_unit.data.entries:
                formatted_group_unit += self._group_unit_generator.unit_generator.format_unit(entry) + ", "

        return formatted_group_unit[:-2]

    def clear_group_units(self):
        self.group_units = []