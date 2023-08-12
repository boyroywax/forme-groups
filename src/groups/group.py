import attrs
import typing

from .unit import Unit, UnitType, UnitTypePool


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
