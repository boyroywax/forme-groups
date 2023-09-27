from attrs import define, field, validators
from typing import Any, Optional

from .unit import Unit
from .data_schema import DataSchema
from .merkle_tree import MerkleTree
from .group_subunit import GroupSubUnitInterface, _convert_list_to_tuple


@define(frozen=True, slots=True, weakref_slot=False)
class Data(GroupSubUnitInterface):
    items: tuple[Unit] = field(validator=validators.instance_of(list | tuple), converter=_convert_list_to_tuple)
    schema: Optional[DataSchema] = field(validator=validators.instance_of(Optional[DataSchema]), default=None)

    def __str__(self) -> str:
        output = ""
        for item in self.items:
            output += str(item) + ", "
            if self.has_schema:
                output += str(self.schema)
        return output

    def __repr__(self) -> str:
        return f"Data(items={[item.__repr__() for item in self.items]})"

    def __iter__(self):
        return self.items.__iter__()

    @property
    def has_schema(self) -> bool:
        return self.schema is not None

    def hash_tree(self) -> MerkleTree:
        item_hashes = []
        for item in self.items:
            item_hashes.append(item.hash_tree().root())
        if self.has_schema:
            item_hashes.append(self.schema.hash_tree().root())
        return MerkleTree(item_hashes)