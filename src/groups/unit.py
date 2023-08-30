from attrs import define, field


@define(frozen=True, slots=True)
class UnitTypeRef:
    alias: str = field(default=None)


@define(frozen=True, slots=True)
class UnitTypeFunction:
    object: callable = field()
    args: list[str] = field(factory=list)


@define(frozen=True, slots=True)
class UnitType:
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
        return any(alias in unit_type.aliases for unit_type in self.unit_types)

    def get_type_from_alias(self, alias: str) -> UnitType:
        for unit_type in self.unit_types:
            if alias in unit_type.aliases:
                return unit_type
        raise ValueError("UnitTypePool does not contain alias: " + alias)

    def add_unit_type(self, unit_type: UnitType):
        for alias in unit_type.aliases:
            if self.contains_alias(alias):
                raise ValueError("UnitTypePool already contains alias")
        self.unit_types.append(unit_type)


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
        

        