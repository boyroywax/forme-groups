from abc import ABC, abstractmethod
from attrs import define, field, validators
from typing import List, Any

from .unit import Unit
from .group_subunit import GroupSubUnitInterface, _convert_list_to_tuple
from .merkle_tree import MerkleTree

__DEFAULT_NONCE_SEPARATOR__ = "."


@define(frozen=True, slots=True)
class Nonce(GroupSubUnitInterface):
    items: tuple[Unit] = field(validator=validators.instance_of(tuple | list), converter=_convert_list_to_tuple)

    def get_by_tier(self, tier: int) -> Unit:
        return self.items[tier]

    def _create_next_tier(self, type_ref: Unit | str = None) -> 'Nonce':
        if isinstance(type_ref, Unit):
            type_ref = type_ref.type_ref
        if type_ref is None:
            type_ref = self.items[-1].type_ref

        match(type_ref):
            case("int" | "integer" | "i"):
                return Nonce(items=self.items + (Unit(value=0, type_ref="int"),))
            case("float" | "f"):
                return Nonce(items=self.items + (Unit(value=0.0, type_ref="float"),))
            case("str" | "string" | "s"):
                return Nonce(items=self.items + (Unit(value="a", type_ref="str"),))
            case _:
                raise ValueError(f"Cannot create next tier for Nonce with type {type_ref}.")

    def __str__(self) -> str:
        output = ""
        for item in self.items:
            output += str(item) + __DEFAULT_NONCE_SEPARATOR__
        return output[:-1]

    def __repr__(self) -> str:
        return f"Nonce(items={[item.__repr__() for item in self.items]})"

    def __next__(self) -> 'Nonce':
        active_unit = self.items[-1]
        match(active_unit.type_ref):
            case("int" | "integer" | "i"):
                next_nonce: int = active_unit.value + 1
            case("float" | "f"):
                next_nonce: float = active_unit.value + 1.0
            case("str" | "string" | "s"):
                if active_unit.value[-1] == "z":
                    next_nonce: str = active_unit.value + "a"
                else:
                    next_nonce: str = active_unit.value[:-1] + chr(ord(active_unit.value[-1]) + 1)
            case _:
                raise ValueError(f"Cannot iterate on Nonce with type {active_unit.type_ref}.")

        return Nonce(items=self.items[:-1] + (Unit(value=next_nonce, type_ref=active_unit.type_ref),))

    def __iter__(self):
        return self

    def hash_tree(self) -> MerkleTree:
        nonce_items: list[Unit] = []
        for item in self.items:
            if not isinstance(item, Unit):
                raise ValueError(f"Invalid item {item} in Nonce.")
            nonce_items.append(item.hash_sha256())
        return MerkleTree(hashed_data=nonce_items)
