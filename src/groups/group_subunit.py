from abc import ABC, abstractmethod
from attrs import define, field, validators
from typing import List, Any

from .unit import Unit
from .merkle_tree import MerkleTree

__DEFAULT_NONCE_SEPARATOR__ = "."


class GroupSubUnitInterface(ABC):
    """An abstract interface for a GroupUnit Object.

    Attributes:
        items (list[Any] | tuple[Any]): The items in the GroupUnit.]

    Methods:
        __init__(items: list[Any] | tuple[Any] = None, freeze: bool = False)
        __str__() -> str
        __repr__() -> str
        __iter__() -> Any
        hash_tree(override: bool = False) -> MerkleTree
    """
    items: list[Any] | tuple[Any]

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __iter__(self) -> Any:
        pass

    @abstractmethod
    def hash_tree(self) -> MerkleTree:
        pass


def _convert_list_to_tuple(items: list[Unit] | tuple[Unit]) -> tuple[Unit]:
    if isinstance(items, list):
        return tuple(items)
    elif isinstance(items, tuple):
        return items
    

@define(frozen=True, slots=True)
class GroupSubUnit(GroupSubUnitInterface):
    items: tuple[Unit] = field(validator=validators.instance_of(tuple | list), converter=_convert_list_to_tuple)

    def __str__(self) -> str:
        output = ""
        for item in self.items:
            output += str(item) + "\n"
        return output[:-1]

    def __repr__(self) -> str:
        return f"GroupUnit(items={[item.__repr__() for item in self.items]})"

    def __iter__(self):
        return self

    def hash_tree(self) -> MerkleTree:
        group_unit_items: list[Unit] = []
        for item in self.items:
            if not isinstance(item, Unit):
                raise ValueError(f"Invalid item {item} in GroupUnit.")
            group_unit_items.append(item.hash_256())
        return MerkleTree(hashed_data=group_unit_items)
