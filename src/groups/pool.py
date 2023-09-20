import json
import hashlib
from abc import ABC, abstractmethod
from attrs import define, field, validators
from typing import Any, Optional, Tuple


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
class Pool(PoolInterface):
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
    

class MerkleTree:
    def __init__(self, data):
        self.data = data
        self.leaves = [hashlib.sha256(d.encode()).hexdigest() for d in data]
        self.levels = [self.leaves]

    def build(self):
        while len(self.levels[-1]) > 1:
            level = []
            for i in range(0, len(self.levels[-1]), 2):
                if i + 1 < len(self.levels[-1]):
                    level.append(hashlib.sha256((self.levels[-1][i] + self.levels[-1][i + 1]).encode()).hexdigest())
                else:
                    level.append(self.levels[-1][i])
            self.levels.append(level)

    def root(self):
        return self.levels[-1][0]

    def verify(self, data, root_hash):
        if hashlib.sha256(data.encode()).hexdigest() not in self.leaves:
            return False
        index = self.leaves.index(hashlib.sha256(data.encode()).hexdigest())
        current_hash = self.leaves[index]
        for i in range(len(self.levels) - 1):
            if index % 2 == 0:
                current_hash = hashlib.sha256((current_hash + self.levels[-i - 2][index + 1]).encode()).hexdigest()
            else:
                current_hash = hashlib.sha256((self.levels[-i - 2][index - 1] + current_hash).encode()).hexdigest()
            index //= 2
        return current_hash == root_hash


@define(slots=True)
class UnitTypePool(PoolInterface):
    _frozen: bool = field(default=False, validator=validators.instance_of(bool))
    items: list[UnitType] | tuple[UnitType] = field(factory=list)

    def __init__(self, items: list[UnitType] | tuple[UnitType] = None, freeze: bool = False):
        self._frozen = False
        self.items = []
        # super().__init__(items=items, freeze=freeze)
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

    def add(self, item: UnitType):
        if self.frozen is True:
            raise ValueError("Cannot add to a frozen UnitTypePool.")

        if item in self.items:
            raise ValueError(f"UnitTypePool already contains item {item}.")

        if item.aliases is None or len(item.aliases) == 0:
            raise ValueError(f"UnitType {item} has no aliases.")

        if item.aliases is not None:
            for alias in item.aliases:
                if self.contains_alias(alias.alias) is True:
                    raise ValueError(f"UnitTypePool already contains alias {alias.alias}.")

        self.items.append(item)

    def get_type_from_alias(self, alias: str) -> UnitType | None:
        """Get a UnitType from an alias.

        Args:
            alias (str): The alias of the UnitType.

        Returns:
            UnitType | None: The UnitType with the given alias, or None if the UnitTypePool does not contain the alias.
        """
        for unit_type in self.items:
            for aliases in unit_type.aliases:
                if aliases.alias == alias:
                    return unit_type
        return None

    def contains_alias(self, alias: str) -> bool:
        """Whether the UnitTypePool contains an alias.

        Args:
            alias (str): The alias to check.

        Returns:
            bool: Whether the UnitTypePool contains the alias.
        """
        return self.get_type_from_alias(alias) is not None

    def get_type_aliases(self) -> list[str]:
        """Get all aliases in the UnitTypePool.

        Returns:
            list[str]: All aliases in the UnitTypePool.
        """
        aliases = []
        for unit_type in self.items:
            for alias in unit_type.aliases:
                aliases.append(alias.alias)
        return aliases

    def add_unit_type_from_dict(self, dict: dict):
        """Add a UnitType from a dictionary.

        Args:
            dict (dict): The dictionary to add.
        """
        self.add(UnitType(
            aliases=[UnitTypeRef(alias=alias) for alias in dict["aliases"]],
            super_type=[UnitTypeRef(alias=alias) for alias in dict["base_type"]],
            prefix=dict["prefix"],
            suffix=dict["suffix"],
            separator=dict["separator"],
            sys_function=UnitTypeFunction(object=eval(dict["sys_function"]["object"]), args=dict["sys_function"]["args"])
        ))

    def set_types_from_json(self, path: str = None):
        """Set the UnitTypePool from a JSON file.

        Args:
            path (str, optional): The path to the JSON file. Defaults to None.
        """
        types_path = __DEFAULT_SYSTEM_TYPES_PATH__ + "/system_types.json"

        if path is not None:
            types_path = path

        with open(types_path, "r") as file:
            json_input: dict = json.load(file)
            # print(json_input["system_types"])
            for dict in json_input["system_types"]:
                self.add_unit_type_from_dict(dict)

    def __str__(self):
        return f"UnitTypePool(items={self.items})"
    
    def __iter__(self):
        return iter(self.items)
    
    def __hash__(self):

        mtree = MerkleTree([str(item) for item in self.items])
        mtree.build()
        return int(mtree.root(), 16)
