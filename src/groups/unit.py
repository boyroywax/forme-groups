import abc
import attrs
import typing
import json




@attrs.define(frozen=True, slots=True)
class UnitType:

    @attrs.define(frozen=True, slots=True)
    class Ref:
        name: str = attrs.field(default="str", validator=attrs.validators.instance_of(str))

    aliases: typing.List[Ref] = attrs.field(default=None, validator=attrs.validators.instance_of(list))
    base_type: typing.List[Ref] = attrs.field(default=None, validator=attrs.validators.optional(attrs.validators.instance_of(list)))
    prefix: typing.Optional[str] = attrs.field(default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str)))
    suffix: typing.Optional[str] = attrs.field(default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str)))
    separator: typing.Optional[str] = attrs.field(default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str)))
    function_call: typing.Optional[typing.Any] = attrs.field(default=None)


@attrs.define(slots=True)
class UnitTypePool:
    types: typing.List[UnitType] = attrs.field(factory=list, validator=attrs.validators.instance_of(list))

    def __init__(self):
        self.types = []
        try:
            self.set_system_types()
        except Exception as e:
            print(e)

    def add(self, type_: UnitType):
        self.types.append(type_)

    def get(self, type_ref: UnitType.Ref) -> UnitType:
        return self.types[type_ref]

    def remove(self, type_ref: UnitType.Ref):
        del self.types[type_ref]

    def __contains__(self, type_ref: UnitType.Ref):
        return type_ref in [alias for type_ in self.types for alias in type_.aliases]

    def __iter__(self):
        return iter(self.types)

    def __len__(self):
        return len(self.types)
    
    def set_type_from_json(self, type_list: typing.List):
        for type_entry in type_list:
            print(type_entry["aliases"])
            type_entry["aliases"] = [UnitType.Ref(name=alias) for alias in type_entry["aliases"]]
            print(type_entry["aliases"])
            type_entry["base_type"] = [UnitType.Ref(name=base_type) for base_type in type_entry["base_type"]]
            print(type_entry["base_type"])
            type_ = UnitType(**type_entry)
            self.add(type_)
    
    def set_system_types(self):
        with open("src/groups/system_types.json", "r") as f:
            system_types: dict = json.load(f)
            print(system_types["system_types"])
        self.set_type_from_json(system_types["system_types"])


@attrs.define(frozen=True, slots=True)
class Unit:
    type_ref: UnitType.Ref = attrs.field(factory=UnitType.Ref)
    value: typing.Any = attrs.field(default=None, validator=attrs.validators.optional(attrs.validators.instance_of(typing.Any)))




