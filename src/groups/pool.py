import json
import hashlib
from abc import ABC, abstractmethod
from attrs import define, field, validators
from typing import Any, Optional, Tuple, Dict

from .merkle_tree import MerkleTree
from .unit import Unit, UnitType, UnitTypeRef, UnitTypeFunction

__DEFAULT_SYSTEM_TYPES_PATH__ = "src/groups"


class PoolInterface(ABC):
    _frozen: bool
    items: list[Any] | tuple[Any]

    @abstractmethod
    def __init__(self, items: list[Any] | tuple[Any] = None, freeze: bool = False):
        pass

    @abstractmethod
    def freeze(self):
        pass

    @property
    @abstractmethod
    def frozen(self) -> bool:
        pass

    @abstractmethod
    def add(self, item: Any):
        pass


@define(slots=True)
class GenericPool(PoolInterface):
    _frozen: bool = field(default=False, validator=validators.instance_of(bool))
    items: list[Any] | tuple[Any] = field(factory=list)

    def __init__(self, items: list[Any] | tuple[Any] = None, freeze: bool = False):
        self._frozen = False
        self.items = []
        if items is not None:
            for item in items:
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

    def add(self, item: Any):
        if self.frozen is True:
            raise ValueError("Cannot add to a frozen Pool.")

        if item in self.items:
            raise ValueError(f"Pool already contains item {item}.")

        self.items.append(item)

    def __str__(self):
        return f"Pool(items={self.items})"

