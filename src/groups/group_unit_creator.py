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

    def create_unit(self, alias: str, value: Any = None, force: bool = True) -> Unit:
        return self._unit_creator.create_unit(alias=alias, value=value, force=force)

    def create_nonce(self, items: list[Unit] | tuple[Unit] | None = None) -> Nonce:
        if items is None:
            items = []
        for item in items:
            assert isinstance(item, Unit)
            if self._unit_pool.contains(item) is False:
                print(ValueError(f"UnitPool does not contain item {item}. Adding to Unit Pool."))
                self._unit_pool.add(item)
            else:
                print(ValueError(f"UnitPool already contains item {item}."))        
        return Nonce(items=items)

    def create_group_subunit(self, items: list[Unit] | tuple[Unit] | None = None) -> GroupSubUnit:
        if items is None:
            items = []
        return GroupSubUnit(items=items)

    def create_group_unit(self, nonce: Nonce, owners: GroupSubUnit, creds: GroupSubUnit, data: GroupSubUnit) -> GroupUnit:
        return GroupUnit(nonce=nonce, owners=owners, creds=creds, data=data)

