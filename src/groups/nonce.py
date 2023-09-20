from abc import ABC, abstractmethod
from attrs import define, field, validators
from typing import Any, Optional, Tuple

from .unit import Unit, UnitType


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
class Pool(PoolInterface):
    _frozen: bool = field(default=False)
    items: list[Any] | tuple[Any] = field(factory=list)

    def __init__(self, items: list[Any] | tuple[Any] = None, freeze: bool = False):
        self.items = []
        if items is not None:
            self.items = items

        self._frozen = False
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

        self.items.append(item)



@define(slots=True)
class UnitTypePool(Pool):
    items: list[UnitType] | tuple[UnitType] = field(factory=list)

    def __init__(self, items: list[UnitType] | tuple[UnitType] = None, freeze: bool = False):
        if items is not None:
            for item in items:
                if not isinstance(item, UnitType):
                    raise ValueError("UnitTypePool can only contain UnitTypes.")
        super().__init__(items=items, freeze=freeze)
