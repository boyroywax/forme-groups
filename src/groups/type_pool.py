from attrs import define, field


@define(slots=True)
class UnitType:
    aliases = field(default_factory=list)
    super_type = field(default=None)
    prefix = field(default=None)
    suffix = field(default=None)
    seperator = field(default=None)
    container = field(default=False)
    function_call = field(default=None)


@define(slots=True)
class UnitTypePool:
    types = field(default_factory=list)

    def __getitem__(self, item):
        for