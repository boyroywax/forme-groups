from attrs import define, field
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
    args: list[str] = field(factory=list)

    def call(self, input: Any = None) -> object:
        """Call the function with the arguments.

        Returns:
            object: The result of calling the function.
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
    unit_types: list[UnitType] = field(factory=list)

    def contains_alias(self, alias: str) -> bool:
        for unit_type in self.unit_types:
            if alias in unit_type.aliases:
                return True

    def get_type_from_alias(self, alias: str) -> UnitType:
        for unit_type in self.unit_types:
            if alias in unit_type.aliases:
                return unit_type
        raise ValueError("UnitTypePool does not contain alias: " + alias)

    def add_unit_type(self, unit_type: UnitType):
        for alias in unit_type.aliases:
            if self.contains_alias(alias):
                raise ValueError("UnitTypePool already contains alias: " + alias.__str__())
        self.unit_types.append(unit_type)
        print(self.unit_types)


@define(frozen=True, slots=True)
class Unit:
    value: str = field(default=None)
    type_ref: UnitTypeRef = field(default=None)


@define(frozen=True, slots=True)
class UnitGenerator:
    unit_type_pool: UnitTypePool = field(default=None)

    def create_unit(self, alias: str, value: str = None, force: bool = True) -> Unit:
        if not self.unit_type_pool.contains_alias(alias):
            raise ValueError("UnitTypePool does not contain alias: " + alias)


