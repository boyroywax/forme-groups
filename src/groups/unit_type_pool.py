import json
from attrs import define, field, validators
from typing import Any, Optional, Tuple, Dict

from .merkle_tree import MerkleTree
from .unit_type import UnitType, UnitTypeRef, UnitTypeFunction
from .pool import PoolInterface

__DEFAULT_SYSTEM_TYPES_PATH__ = "src/groups"


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

    def contains(self, item: UnitType) -> bool:
        return item in self.items

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
            json_input: Dict = json.load(file)
            # print(json_input["system_types"])
            for dict in json_input["system_types"]:
                self.add_unit_type_from_dict(dict)

    def __str__(self):
        return f"[{[item.__repr__() for item in self.items]}]"

    def __repr__(self):
        return f"UnitTypePool(items=[{[item.__repr__() for item in self.items]}])"

    def __iter__(self):
        return iter(self.items)

    def hash_tree(self, override: bool = False):
        if self.frozen is False and override is False:
            raise ValueError("Cannot hash an unfrozen UnitTypePool.")
        if self.frozen is False and override is True:
            print("Warning: Hashing an unfrozen UnitTypePool.")

        return MerkleTree([item.hash_256() for item in self.items])
