from attrs import define, field

from .unit import Unit, UnitGenerator, UnitTypeRef


@define(frozen=True, slots=True)
class GroupUnit:
    nonce: 'GroupUnit.Nonce' = field(default=None)
    owners: 'GroupUnit.Owners' = field(default=None)
    credentials: 'GroupUnit.Credentials' = field(default=None)
    data: 'GroupUnit.Data' = field(default=None)
    unit_generator: UnitGenerator = field(default=None)

    @define(frozen=True, slots=True)
    class Nonce:
        nonce: tuple[Unit] = field(default=None)

        def get_active_nonce(self) -> Unit:
            return self.nonce[-1]

        def get_active_nonce_type(self) -> UnitTypeRef:
            return self.get_active_nonce().type_ref

        def next_active_nonce(self) -> Unit:
            active_nonce = self.get_active_nonce()
            nonce_type = active_nonce.type_ref

            match(nonce_type.alias):
                case "int":
                    return self.unit_generator.create_unit(value=active_nonce.value + 1, type_ref=nonce_type)

                case _:
                    raise ValueError("Nonce type not supported. " + nonce_type.__str__())

        def next_nonce(self) -> 'GroupUnit.Nonce':
            return GroupUnit.Nonce(nonce=self.nonce[:-1] + (self.next_active_nonce(),))

    @define(frozen=True, slots=True)
    class Owners:
        owners: tuple[Unit] = field(default=None)

    @define(frozen=True, slots=True)
    class Credentials:
        credentials: tuple[Unit] = field(default=None)

    @define(frozen=True, slots=True)
    class Data:
        data: tuple[Unit] = field(default=None)


class GroupUnitGenerator:
    unit_generator: UnitGenerator = UnitGenerator()

    def __init__(self, unit_generator: UnitGenerator = None):
        if unit_generator is not None:
            self.unit_generator = unit_generator
            self.unit_generator.unit_type_pool.freeze_pool()
        else:
            self.unit_generator = UnitGenerator()


class Group:
    generator: GroupUnitGenerator = GroupUnitGenerator()
    units: list[GroupUnit] = []
    active_nonce: tuple[Unit] = None

    def __init__(self, generator: GroupUnitGenerator = None):
        if generator is not None:
            self.generator = generator
        else:
            self.generator = GroupUnitGenerator()

    def clear_units(self):
        self.units = []

    def get_unit_by_nonce(self, nonce: tuple[Unit]) -> GroupUnit:
        print(self.units)
        for group_unit in self.units:
            if group_unit.nonce == nonce:
                return group_unit
        return None

    def set_active_nonce(self, nonce: tuple[Unit]):
        self.active_nonce = nonce

    def get_unit_by_active_nonce(self) -> GroupUnit:
        return self.get_unit_by_nonce(self.active_nonce)

    def find_next_nonce(self, nonce: tuple[Unit]) -> tuple[Unit]:
        active_nonce = nonce[-1]
        nonce_type = active_nonce.type_ref.alias

        match(nonce_type):
            case "int":
                if len(nonce) == 1:
                    return (Unit(value=active_nonce.value + 1, type_ref=UnitTypeRef(alias="int")),)
                else:
                    print(nonce[:-1])
                    return nonce[:-1] + (Unit(value=active_nonce.value + 1, type_ref=UnitTypeRef(alias="int")),)

            case _:
                raise ValueError("Nonce type not supported. " + nonce_type.__str__())

    def find_next_active_nonce(self) -> tuple[Unit]:
        return self.find_next_nonce(self.active_nonce)

    def add_group_unit(self, group_unit: GroupUnit):
        if self.get_unit_by_nonce(group_unit.nonce) is not None:
            raise ValueError("GroupUnit with nonce already exists. Nonce: " + group_unit.nonce.__str__())
        else:
            if self.find_next_nonce(group_unit.nonce) != self.find_next_active_nonce():
                raise ValueError("GroupUnit nonce does not match the next active nonce.")
            self.units.append(group_unit)

    def create_and_add_group_unit(self, owners: tuple[Unit], credentials: tuple[Unit], data: tuple[Unit]):
        nonce = self.find_next_active_nonce()
        group_unit = self.generator.create_group_unit(nonce=nonce, owners=owners, credentials=credentials, data=data)
        self.add_group_unit(group_unit)
