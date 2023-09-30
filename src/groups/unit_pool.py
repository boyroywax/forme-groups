from attrs import define, field, validators
from typing import Any, Optional, Tuple, Dict

from .utils.merkle_tree import MerkleTree
from .unit import Unit, UnitType, UnitTypeRef, UnitTypeFunction
from .pool import PoolInterface


@define(slots=True)
class UnitPool(PoolInterface):
    _frozen: bool = field(default=False, validator=validators.instance_of(bool))
    items: list[Unit] | tuple[Unit] = field(factory=list, validator=validators.instance_of(list | tuple))

    def __init__(self, items: list[Unit] | tuple[Unit] = None, freeze: bool = False):
        self._frozen = False
        self.items = []
        # super().__init__(items=items, freeze=freeze)
        if items is not None:
            for item in items:
                assert isinstance(item, Unit)
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

    def add(self, item: Unit):
        if self.frozen is True:
            raise ValueError("Cannot add to a frozen UnitPool.")

        if self.contains(item) is True:
            raise ValueError(f"UnitPool already contains item {item}.")

        self.items.append(item)

    def add_from_dict(self, item: dict):
        self.add(Unit(value=item["value"], type_ref=item["type_ref"]))

    def contains(self, item: Unit) -> bool:
        return item in self.items

    def __str__(self) -> str:
        return f"[{[item.__str__() for item in self.items]}]"

    def __repr__(self) -> str:
        return f"UnitPool(items={[item.__repr__() for item in self.items]})"

    def __iter__(self) -> Unit:
        for item in self.items:
            yield item

    def hash_tree(self, override: bool = False) -> MerkleTree:
        if self.frozen is False and override is False:
            raise ValueError("Cannot hash a non-frozen Pool.")

        return MerkleTree(hashed_data=[item.hash_sha256() for item in self.items])