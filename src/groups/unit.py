from attrs import define, field
from attrs.exceptions import FrozenInstanceError
import json
from typing import Any


@define(frozen=True, slots=True)
class UnitTypeRef:
    """A reference to a UnitType.

    Attributes:
        alias (str): The alias of the UnitType.
    """
    alias: str = field(default=None)

    def __str__(self) -> str:
        return self.alias


@define(frozen=True, slots=True)
class UnitTypeFunction:
    """A function that can be used to generate a Unit.

    Attributes:
        object (callable): The function that will be called to generate a Unit.
        args (list[str]): The arguments that will be passed to the function.
    """
    object: callable = field(factory=callable)
    args: list = field(factory=list)

    def call(self, input: Any = None) -> object:
        """Call the function with the given input.

        Args:
            input (Any): The input to the function.

        Returns:
            object: The result of the function call.
        """
        if input is not None:
            self.args.append(input)

        return self.object(*self.args)


@define(frozen=True, slots=True)
class UnitType:
    """A type of Unit.

    Attributes:
        aliases (list[UnitTypeRef]): The aliases of the UnitType.
        super_type (list[UnitTypeRef]): The super types of the UnitType.
        prefix (str): The prefix of the UnitType.
        suffix (str): The suffix of the UnitType.
        separator (str): The separator of the UnitType.
        sys_function (UnitTypeFunction): The system function of the UnitType.
    """
    aliases: list[UnitTypeRef] = field(factory=list)
    super_type: list[UnitTypeRef] = field(factory=list)
    prefix: str = field(default=None)
    suffix: str = field(default=None)
    separator: str = field(default=None)
    sys_function: UnitTypeFunction = field(default=None)


@define(slots=True)
class UnitTypePool:
    _frozen: bool = field(default=False)
    unit_types: list[UnitType] | tuple[UnitType] = field(factory=list)

    def freeze_pool(self):
        self.__setattr__("unit_types", tuple(self.unit_types))
        self.__setattr__("_frozen", True)

    def get_type_from_alias(self, alias: str) -> UnitType | None:
        for unit_type in self.unit_types:
            for aliases in unit_type.aliases:
                if aliases.alias == alias:
                    return unit_type
        return None

    def contains_alias(self, alias: str) -> bool:
        return self.get_type_from_alias(alias) is not None

    def add_unit_type(self, unit_type: UnitType):
        for aliases in unit_type.aliases:
            if self.contains_alias(aliases.alias):
                raise ValueError("UnitTypePool already contains alias: " + aliases.alias)
        self.unit_types.append(unit_type)

    def add_unit_type_from_json(self, json: dict):
        unit_type = UnitType(
            aliases=[UnitTypeRef(alias=alias) for alias in json["aliases"]],
            super_type=[UnitTypeRef(alias=alias) for alias in json["base_type"]],
            prefix=json["prefix"],
            suffix=json["suffix"],
            separator=json["separator"],
            sys_function=UnitTypeFunction(object=eval(json["sys_function"]["object"]), args=json["sys_function"]["args"]),
        )
        self.add_unit_type(unit_type)

    def set_system_types_from_json(self):
        with open("src/groups/system_types.json", "r") as f:
            sys_types = json.load(f)
            for type_ in sys_types["system_types"]:
                self.add_unit_type_from_json(type_)


@define(frozen=True, slots=True)
class Unit:
    value: str = field(default=None)
    type_ref: UnitTypeRef = field(default=None)


@define(frozen=True, slots=True)
class UnitGenerator:
    unit_type_pool: UnitTypePool = field(default=None)

    def check_frozen_pool(self) -> bool:
        return self.unit_type_pool._frozen

    def create_unit(self, alias: str, value: str = None, force: bool = True) -> Unit:
        if not self.check_frozen_pool():
            raise Exception("UnitTypePool must be frozen before generating units.")

        if not self.unit_type_pool.contains_alias(alias):
            raise ValueError("UnitTypePool does not contain alias: " + alias)

        unit_type: UnitType = self.unit_type_pool.get_type_from_alias(alias)

        if unit_type.sys_function is not None and force is True:
            value = unit_type.sys_function.call(value)

        return Unit(value=value, type_ref=alias)
