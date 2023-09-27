from attrs import define, field, validators
from typing import Any, Optional

from .unit import Unit
from .unit_creator import UnitCreator
from .unit_pool import UnitPool
from .group_subunit import GroupSubUnit
from .nonce import Nonce
from .group_unit import GroupUnit


@define(slots=True)
class GroupUnitCreator:
    _unit_pool: Optional[UnitPool] = field(default=None)
    _unit_creator: Optional[UnitCreator] = field(default=None)

    def __init__(self, unit_pool: UnitPool = None, unit_creator: UnitCreator = None):
        if unit_pool is None:
            self._unit_pool = UnitPool()
        else:
            self._unit_pool = unit_pool

        if unit_creator is None:
            self._unit_creator = UnitCreator()
        else:
            self._unit_creator = unit_creator

    def check_unit_pool(self, unit: Unit) -> bool:
        return self._unit_pool.contains(unit)

    def create_unit(self, alias: str, value: Any = None, force: bool = True) -> Unit:
        # print(value)
        created_unit = self._unit_creator.create_unit(alias=alias, value=value, force=force)
        # print(created_unit)
        if self.check_unit_pool(created_unit) is False:
            self._unit_pool.add(created_unit)
        else:
            print(ValueError(f"Unit {created_unit} already in UnitPool."))
        return created_unit

    def create_nonce(self, items: list[Unit] | tuple[Unit] | None = None) -> Nonce:
        if items is None:
            items = []
        for item in items:
            assert isinstance(item, Unit)
            if self.check_unit_pool(item) is False:
                print(ValueError(f"Unit {item} is not in the UnitPool."))
                self._unit_pool.add(item)
             
        return Nonce(items=items)

    def create_group_subunit(self, items: list[Unit] | tuple[Unit] | None = None) -> GroupSubUnit:
        if items is None:
            items = []
        for item in items:
            assert isinstance(item, Unit)
            if self.check_unit_pool(item) is False:
                print(ValueError(f"Unit {item} is not in the UnitPool."))
                self._unit_pool.add(item)
        
        return GroupSubUnit(items=items)

    def create_group_unit(self, nonce: Nonce, owners: GroupSubUnit, creds: GroupSubUnit, data: GroupSubUnit) -> GroupUnit:
        return GroupUnit(nonce=nonce, owners=owners, creds=creds, data=data)

