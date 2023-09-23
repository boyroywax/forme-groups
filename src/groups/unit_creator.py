from attrs import define, field, validators
from typing import Any, Optional, Tuple, Dict

from .unit import Unit
from .unit_type_pool import UnitTypePool




@define(slots=True)
class UnitCreator:
    unit_type_pool: UnitTypePool = field(default=None)

    def __init__(self, unit_type_pool: UnitTypePool = None):
        if unit_type_pool is None:
            self.unit_type_pool = UnitTypePool()
            self.unit_type_pool.set_types_from_json()
            self.unit_type_pool.freeze()
        else:
            self.unit_type_pool = unit_type_pool

    def create_unit(self, alias: str, value: Any = None) -> Unit:
        if not self.unit_type_pool.frozen:
            raise Exception("UnitTypePool must be frozen before generating units.")
        
        unit_type = self.unit_type_pool.get_type_from_alias(alias)
        print(unit_type)
        if unit_type is None:
            raise ValueError(f"UnitTypePool does not contain alias {alias}.")
        
        if value is not None:
            if unit_type.sys_function is None:
                return Unit(value=value, type_ref=alias)
            else:
                return Unit(value=unit_type.sys_function.call(value), type_ref=alias)
        
    
    


# @define(slots=True)
# class UnitGenerator:
#     unit_type_pool: UnitTypePool = field(default=None)

#     def __init__(self, unit_type_pool: UnitTypePool = None, freeze: bool = False, system_types_path: str = None, custom_types_path: str = None):
#         self.unit_type_pool = UnitTypePool()
#         self.unit_type_pool.set_types_from_json(path=system_types_path)

#         if custom_types_path is not None:
#             self.unit_type_pool.set_types_from_json(path=custom_types_path)

#         if unit_type_pool is not None:
#             for unit_type in unit_type_pool.unit_types:
#                 self.unit_type_pool.add_unit_type(unit_type)

#         if freeze is True:
#             self.__post_init__(freeze=True)

#     def __post_init__(self, **kwargs):
#         if kwargs.get("freeze", False) is True:
#             self.unit_type_pool.freeze_pool()

#     def check_frozen_pool(self) -> bool:
#         return self.unit_type_pool.frozen

#     def create_unit(self, alias: str, value: Any = None, force: bool = True) -> Unit:
#         if not self.check_frozen_pool():
#             raise Exception("UnitTypePool must be frozen before generating units.")

#         unit_type: UnitType = self.unit_type_pool.get_type_from_alias(alias)

#         if unit_type is None:
#             raise ValueError("UnitTypePool does not contain alias: " + alias)

#         if force is True:
#             if unit_type.sys_function is None:
#                 return Unit(value=value, type_ref=UnitTypeRef(alias))
#             else:
#                 return Unit(value=unit_type.sys_function.call(value), type_ref=UnitTypeRef(alias))

#         return Unit(value=value, type_ref=UnitTypeRef(alias))

#     def format_unit(self, unit: Unit) -> str:
#         unit_type: UnitType = self.unit_type_pool.get_type_from_alias(unit.type_ref.alias)
#         formatted_unit = ""

#         if unit_type.prefix is not None:
#             formatted_unit += unit_type.prefix

#         if unit_type.separator is not None:
#             if isinstance(unit.value, tuple | list):
#                 for value in unit.value:
#                     formatted_unit += str(value) + unit_type.separator
#                 formatted_unit = formatted_unit[:-1]
#             else:
#                 formatted_unit += str(unit.value)

#         if unit_type.suffix is not None:
#             formatted_unit += unit_type.suffix

#         return formatted_unit

