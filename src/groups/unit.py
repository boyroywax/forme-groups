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
            print(self.__slots__)
        except Exception as e:
            print(e, self.__slots__)

    def add(self, type_: UnitType):
        self.types.append(type_)

    def get(self, type_ref: UnitType.Ref) -> UnitType | None:
        for type_ in self.types:
            print(type_.__slots__)
            for stored_type_ref in type_.aliases:
                if type_ref == stored_type_ref:
                    return type_
        return None

    def remove(self, type_ref: UnitType.Ref) -> None:
        for type_ in self.types:
            if (type_ref in type_.aliases) or (type_.base_type.startswith("__SYSTEM_RESERVED_")):
                raise Exception("Cannot remove system type")
            if type_ref in type_.aliases and not type_.base_type.startswith("__SYSTEM_RESERVED_"):
                self.types.remove(type_)

    def set_type_from_json(self, type_list: typing.List):
        for type_entry in type_list:
            # print(type_entry["aliases"])
            type_entry["aliases"] = [UnitType.Ref(name=alias) for alias in type_entry["aliases"]]
            # print(type_entry["aliases"])
            type_entry["base_type"] = [UnitType.Ref(name=base_type) for base_type in type_entry["base_type"]]
            # print(type_entry["base_type"])
            type_ = UnitType(**type_entry)
            self.add(type_)

    def set_system_types(self):
        with open("src/groups/system_types.json", "r") as f:
            system_types: dict = json.load(f)
            # print(system_types["system_types"])
        self.set_type_from_json(system_types["system_types"])

    def enforce_type(self, type_ref: UnitType.Ref, value: typing.Any) -> typing.Any:
        function_call = self.get(type_ref).function_call
        print(function_call)
        if function_call is not None:
            try:
                if function_call == "<class 'str'>":
                    return str(value)
                class_name = function_call.strip("<class '").strip("'>")
                print(class_name)
                class_ = eval(class_name)
                print(class_)
                return class_(value)
            except Exception as e:
                raise Exception("Function call failed") from e

    def create_unit(self, type_ref: UnitType.Ref, value: typing.Any, force: bool = True) -> 'Unit':
        if self.get(type_ref) is None:
            raise Exception("Type not found")
        if force:
            value = self.enforce_type(type_ref, value)
            print(value)
        return Unit(type_ref=type_ref, value=value)

    def __contains__(self, type_ref: UnitType.Ref) -> bool:
        return self.get(type_ref) is not None

    def __iter__(self):
        return iter(self.types)

    def __len__(self):
        return len(self.types)


@attrs.define(frozen=True, slots=True)
class Unit:
    type_ref: UnitType.Ref = attrs.field(factory=UnitType.Ref)
    value: typing.Any = attrs.field(default=None)


@attrs.define(slots=True)
class GroupUnit:

    nonce: 'GroupUnit.Nonce' = attrs.field(default=None)
    ownership: 'GroupUnit.Ownership' = attrs.field(default=None)
    credentials: 'GroupUnit.Credentials' = attrs.field(default=None)
    data: 'GroupUnit.Data' = attrs.field(default=None)

    def __init__(self, nonce: typing.Optional['GroupUnit.Nonce'] = None, ownership: typing.Optional['GroupUnit.Ownership'] = None, credentials: typing.Optional['GroupUnit.Credentials'] = None, data: typing.Optional['GroupUnit.Data'] = None):
        if nonce.value is None:
            nonce = GroupUnit.Nonce()
        if ownership is None:
            ownership = GroupUnit.Ownership()
        if credentials is None:
            credentials = GroupUnit.Credentials()
        if data is None:
            data = GroupUnit.Data()
        self.nonce = nonce
        self.ownership = ownership
        self.credentials = credentials
        self.data = data

    @attrs.define(frozen=True, slots=True)
    class Nonce:
        value: typing.List[Unit] = attrs.field(factory=list, validator=attrs.validators.instance_of(list))

    @attrs.define(frozen=True, slots=True)
    class Ownership:
        value: typing.List[Unit] = attrs.field(factory=list, validator=attrs.validators.instance_of(list))

    @attrs.define(frozen=True, slots=True)
    class Credentials:
        value: typing.List[Unit] = attrs.field(factory=list, validator=attrs.validators.instance_of(list))

    @attrs.define(frozen=True, slots=True)
    class Data:
        value: typing.List[Unit] = attrs.field(factory=list, validator=attrs.validators.instance_of(list))


@attrs.define(slots=True)
class Group:
    type_pool: UnitTypePool = attrs.field(factory=UnitTypePool)
    units: typing.List[GroupUnit] = attrs.field(factory=list, validator=attrs.validators.instance_of(list))

    def __init__(self):
        self.type_pool = UnitTypePool()
        self.units = []

    def pool_has_nonce(self, nonce: GroupUnit.Nonce) -> bool:
        for unit in self.units:
            if unit.nonce == nonce:
                return True
        return False

    def add_group_unit(self, group_unit: GroupUnit) -> None:
        if self.pool_has_nonce(group_unit.nonce):
            raise Exception("Nonce already exists")
        self.units.append(group_unit)

    def get_next_nonce(self, group_unit: typing.Optional[GroupUnit] = None) -> GroupUnit.Nonce:
        if group_unit is None:
            return GroupUnit.Nonce(value=[self.type_pool.create_unit(UnitType.Ref(name="int"), 0)])
        else:
            nonce = group_unit.nonce
            nonce.value[0].value += 1
            return nonce


    

        