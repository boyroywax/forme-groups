from attrs import define, field, validators
from typing import Any

from .unit import Unit
from .unit_type_pool import UnitTypePool


@define(slots=True)
class UnitCreator:
    unit_type_pool: UnitTypePool = field(default=None)

    def __init__(self, unit_type_pool: UnitTypePool = None):
        if unit_type_pool is None:
            self.unit_type_pool = UnitTypePool()
            self.unit_type_pool.set_system_types_from_json()
            self.unit_type_pool.freeze()
        else:
            self.unit_type_pool = unit_type_pool

    def create_unit(self, alias: str, value: Any = None, force: bool = True) -> Unit:
        if not self.unit_type_pool.frozen:
            raise Exception("UnitTypePool must be frozen before generating units.")

        unit_type = self.unit_type_pool.get_type_from_alias(alias)
        # print(unit_type)
        if unit_type is None:
            raise ValueError(f"UnitTypePool does not contain alias {alias}.")

        if force is True:
            if unit_type.sys_function is not None:
                # print(unit_type.sys_function.function_object)
                value = unit_type.sys_function.call(value)

        return Unit(value=value, type_ref=alias)
