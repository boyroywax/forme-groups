import hashlib
from attrs import define, field, validators
from typing import Any, Optional, Tuple, Dict

from .unit_type import UnitType, UnitTypeRef, UnitTypeFunction
from .unit_type_pool import UnitTypePool
from .merkle_tree import MerkleTree
from .group_subunit import GroupSubUnitInterface, _convert_list_to_tuple


@define(frozen=True, slots=True, weakref_slot=False)
class DataSchema(GroupSubUnitInterface):
    items: Dict[str, UnitTypeRef] = field(factory=dict, validator=validators.instance_of(dict))

    def __str__(self) -> str:
        return f"DataSchema({self.items})"

    def __repr__(self) -> str:
        return f"DataSchema({self.items})"

    def __iter__(self) -> Any:
        return self.items.__iter__()

    def to_dict(self) -> Dict[str, UnitTypeRef]:
        return self.items

    def verify(self, unit_type_pool: UnitTypePool) -> bool:
        for key, value in self.items.items():
            if unit_type_pool.contains_alias(value.alias) is False:
                raise ValueError(f"DataSchema contains invalid alias {value.alias}.")
        return True

    def hash_tree(self) -> MerkleTree:
        item_hashes = []
        for key, value in self.items.items():
            item_hashes.append(hashlib.sha256(f"{key}:{value}".encode()).hexdigest())
        return MerkleTree(item_hashes)
