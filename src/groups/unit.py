from attrs import define, field
import json
from typing import Any, Optional


@define(frozen=True, slots=True)
class UnitTypeRef:
    """A reference to a UnitType.

    Attributes:
        alias (str): The alias of the UnitType.
    """
    alias: str = field(default=None)


@define(frozen=True, slots=True)
class UnitTypeFunction:
    """A function that can be used to generate a Unit.

    Attributes:
        object (callable): The function that will be called to generate a Unit.
        args (tuple): The arguments that will be passed to the function.
    """
    object: callable = field(factory=callable)
    args: tuple = field(factory=tuple)

    def call(self, input: Any = None) -> object:
        """Call the function with the given input.

        Args:
            input (Any): The input to the function.

        Returns:
            object: The result of the function call.
        """
        if input is not None and len(self.args) > 0:
            new_args = list(self.args)
            new_args.insert(0, input)
            return self.object(*new_args)
        elif input is not None:
            return self.object(input)
        else:
            return self.object(*self.args)


@define(frozen=True, slots=True)
class UnitType:
    """A type of Unit.

    Attributes:
        aliases (list[UnitTypeRef]): The aliases of the UnitType.
        super_type (list[UnitTypeRef]): The super types of the UnitType.
        prefix (str): The prefix of the UnitType. Defaults to None.
        suffix (str): The suffix of the UnitType. Defaults to None.
        separator (str): The separator of the UnitType. Defaults to None.
        sys_function (UnitTypeFunction): The system function of the UnitType. Defaults to None.
    """
    aliases: tuple[str] = field(factory=tuple)
    super_type: tuple[UnitTypeRef] = field(factory=tuple)
    prefix: Optional[str] = field(default=None)
    suffix: Optional[str] = field(default=None)
    separator: Optional[str] = field(default=None)
    sys_function: Optional[UnitTypeFunction] = field(default=None)


@define(slots=True)
class UnitTypePool:
    _frozen: bool = field(default=False)
    unit_types: list[UnitType] | tuple[UnitType] = field(factory=list)

    def __init__(self, sys_types: bool = False):
        self._frozen = False
        self.unit_types = []
        # if kwargs.get("freeze", False) is True:
        if sys_types is True:
            self.set_system_types_from_json()

    def freeze_pool(self):
        self.__setattr__("unit_types", tuple(self.unit_types))
        self.__setattr__("_frozen", True)

    @property
    def frozen(self) -> bool:
        return self._frozen

    @frozen.getter
    def frozen(self) -> bool:
        return self._frozen

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
    value: Any = field(default=None)
    type_ref: UnitTypeRef = field(default=None)


@define(slots=True)
class UnitGenerator:
    unit_type_pool: UnitTypePool = field(default=None)

    def __init__(self, unit_type_pool: UnitTypePool = None):
        self.unit_type_pool = UnitTypePool()
        self.unit_type_pool.set_system_types_from_json()

        if unit_type_pool is not None:
            for unit_type in unit_type_pool.unit_types:
                self.unit_type_pool.add_unit_type(unit_type)

    def __post_init__(self, **kwargs):
        if kwargs.get("freeze", False) is True:
            self.unit_type_pool.freeze_pool()

    def check_frozen_pool(self) -> bool:
        return self.unit_type_pool.frozen

    def create_unit(self, alias: str, value: Any = None, force: bool = True) -> Unit:
        if not self.check_frozen_pool():
            raise Exception("UnitTypePool must be frozen before generating units.")

        if not self.unit_type_pool.contains_alias(alias):
            raise ValueError("UnitTypePool does not contain alias: " + alias)

        unit_type: UnitType = self.unit_type_pool.get_type_from_alias(alias)

        if force is True:
            if unit_type.sys_function is None:
                raise ValueError("UnitType has no system function.")
            else:
                return Unit(value=unit_type.sys_function.call(value), type_ref=UnitTypeRef(alias))

        return Unit(value=value, type_ref=UnitTypeRef(alias))
