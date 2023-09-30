from attrs import define, field, validators
from typing import Any

from .utils.merkle_tree import MerkleTree
from .group_subunit import GroupSubUnit
from .nonce import Nonce
from .group_unit import GroupUnit
from .pool import PoolInterface


@define(slots=True, weakref_slot=False)
class GroupUnitPool(PoolInterface):
    _frozen: bool = field(default=False, validator=validators.instance_of(bool))
    items: list[GroupUnit] | tuple[GroupUnit] = field(factory=list, validator=validators.instance_of(list | tuple))

    def __init__(self, items: list[GroupUnit] | tuple[GroupUnit] = None, freeze: bool = False):
        self._frozen = False
        self.items = []
        # super().__init__(items=items, freeze=freeze)
        if items is not None:
            for item in items:
                assert isinstance(item, GroupUnit)
                self.add(item)

        if freeze is True:
            self.freeze()

    def freeze(self):
        if self.frozen is True:
            raise ValueError("Cannot freeze a frozen Pool.")

        if self.items is not None and self.items is not tuple:
            self.__setattr__("items", tuple(self.items))

        self.__setattr__("_frozen", True)

    @property
    def frozen(self) -> bool:
        return self._frozen

    @frozen.getter
    def frozen(self) -> bool:
        return self._frozen

    def add(self, item: GroupUnit):
        if self.frozen is True:
            raise ValueError("Cannot add to a frozen GroupUnitPool.")

        if self.contains(item) is True:
            raise ValueError(f"GroupUnitPool already contains item {item}.")

        self.items.append(item)

    def contains(self, item: GroupUnit) -> bool:
        return item in self.items
    
    def contains_nonce(self, nonce: Nonce) -> bool:
        for item in self.items:
            if item.nonce == nonce:
                return True
        return False

    def __str__(self) -> str:
        output = ""
        for item in self.items:
            output += str(item) + ", "
        return output[:-1]

    def __repr__(self) -> str:
        return f"GroupUnitPool(items={[item.__str__() for item in self.items]})"

    def __iter__(self) -> Any:
        for item in self.items:
            yield item

    def hash_tree(self, override: bool = False) -> MerkleTree:
        group_unit_items: list[GroupSubUnit] = []
        for item in self.items:
            if not isinstance(item, GroupUnit):
                raise ValueError(f"Invalid item {item} in GroupUnitPool.")
            group_unit_items.append(item.hash_tree().root())
        return MerkleTree(hashed_data=group_unit_items)