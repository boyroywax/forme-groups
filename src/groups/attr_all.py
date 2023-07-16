from typing import Any
from attrs import define, field, fields, validators, exceptions, make_class, asdict, astuple, has, evolve

__SYSTEM_TYPES__ = str | int | float | bool | list | tuple | dict | bytes


@define(slots=True)
class UnitTypeRef:
    type_ref: str = field(default="str", validator=validators.instance_of(str))

    def freeze(self) -> 'FrozenUnitTypeRef':
        print("Freezing UnitTypeRef" + str(self))
        return FrozenUnitTypeRef(self.type_ref)


@define(slots=True, frozen=True)
class FrozenUnitTypeRef(UnitTypeRef):
    type_ref: str = field(default="str", validator=validators.instance_of(str))


@define(slots=True)
class UnitValue(UnitTypeRef):
    value: __SYSTEM_TYPES__ = field(default=None, validator=validators.instance_of(__SYSTEM_TYPES__))


@define(slots=True, frozen=True)
class FrozenUnitValue(UnitValue):
    pass


@define(slots=True)
class Unit(UnitValue):

    def freeze(self) -> 'FrozenUnit':
        print("Freezing Unit" + str(self))
        frozen_unit_type_ref = FrozenUnitTypeRef(self.type_ref)
        frozen_unit_value = FrozenUnitValue(self.type_ref, self.value)
        return FrozenUnit(frozen_unit_type_ref, frozen_unit_value)


@define(slots=True, frozen=True)
class FrozenUnit(UnitValue):
    pass

