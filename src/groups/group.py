from attrs import define, field, validators
from typing import Any, List, Dict, Optional

from .unit import Unit
from .group_unit_creator import GroupUnitCreator
from .group_unit import GroupUnit
from .nonce import Nonce
from .data import Data
from .group_subunit import GroupSubUnit
from .merkle_tree import MerkleTree
from .group_unit_pool import GroupUnitPool


@define(slots=True, weakref_slot=False)
class Group:
    _group_unit_creator: Optional[GroupUnitCreator] = field(default=None, validator=validators.instance_of(Optional[GroupUnitCreator]))
    _group_unit_pool: Optional[GroupUnitPool] = field(default=None, validator=validators.instance_of(Optional[GroupUnitPool]))
    _active_unit: Optional[GroupUnit] = field(default=None, validator=validators.instance_of(Optional[GroupUnit]))

    def __init__(self, group_unit_creator: GroupUnitCreator = None, group_unit_pool: GroupUnitPool = None, active_unit: GroupUnit = None):
        if group_unit_creator is None:
            group_unit_creator = GroupUnitCreator()
        self._group_unit_creator = group_unit_creator

        if group_unit_pool is None:
            group_unit_pool = GroupUnitPool()
        self._group_unit_pool = group_unit_pool

        if active_unit is None:
            active_unit = self.create_group_unit(nonce=Nonce(items=(Unit(value=0, type_ref="int"),)), data=Data(items=(Unit(value="Hello, world!", type_ref="str"),)))
        self._active_unit = active_unit

    def contains(self, item: GroupUnit) -> bool:
        return self._group_unit_pool.contains(item)

    def add(self, item: GroupUnit):
        if self.contains(item) is True:
            raise ValueError(f"Group already contains item {item}.")

        if self._group_unit_pool.contains_nonce(item.nonce) is True:
            raise ValueError(f"Group already contains nonce {item.nonce}.")

        self._group_unit_pool.add(item)

    def next_nonce(self, previous: Nonce = None) -> Nonce:
        if previous is None:
            nonce: Nonce = self._active_unit.nonce.__next__()
        else:
            nonce: Nonce = previous.__next__()

        if self._group_unit_pool.contains_nonce(nonce) is True:
            print(ValueError(f"Group already contains nonce {nonce}."))
            nonce = self.next_nonce(previous=nonce)
        return nonce
    
    def next_nonce_tier(self, type_: str ) -> Nonce:
        nonce: Nonce = self._active_unit.nonce._create_next_tier()
        if self._group_unit_pool.contains_nonce(nonce) is True:
            print(ValueError(f"Group already contains nonce {nonce}."))
            nonce = nonce.__next__()
        return nonce


    def create_group_unit(self, nonce: Nonce, data: Data, owners: GroupSubUnit, creds: GroupSubUnit) -> GroupUnit:
        new_group_unit = self._group_unit_creator.create_group_unit(nonce=nonce, data=data, owners=owners, creds=creds)

        self.add(new_group_unit)
        return new_group_unit
    
    def create_next_group_unit(self, data: Data, owners: GroupSubUnit, creds: GroupSubUnit) -> GroupUnit:
        nonce = self.next_nonce()
        return self.create_group_unit(nonce=nonce, data=data, owners=owners, creds=creds)
    

    




