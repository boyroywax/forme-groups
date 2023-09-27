from attrs import define, field, validators
from typing import Any

from .merkle_tree import MerkleTree
from .group_subunit import GroupSubUnitInterface


@define(frozen=True, slots=True, weakref_slot=False)
class Data(GroupSubUnitInterface):
    
