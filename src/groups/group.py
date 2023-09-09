from attrs import define, field

from .unit import Unit, UnitGenerator


@define(frozen=True, slots=True)
class GroupUnit:
    nonce: tuple[Unit] = field(default=None)
    owners: tuple[Unit] = field(default=None)
    credentials: tuple[Unit] = field(default=None)
    data: tuple[Unit] = field(default=None)


class GroupUnitGenerator:
    unit_generator: UnitGenerator = UnitGenerator()

    def __init__(self, unit_generator: UnitGenerator = None):
        if unit_generator is not None:
            self.unit_generator = unit_generator
            self.unit_generator.unit_type_pool.freeze_pool()
        else:
            self.unit_generator = UnitGenerator()

    def create_group_unit(self, nonce: tuple[Unit], owners: tuple[Unit], credentials: tuple[Unit], data: tuple[Unit]) -> GroupUnit:
        return GroupUnit(
            nonce=nonce,
            owners=owners,
            credentials=credentials,
            data=data,
        )
    

class Group:
    generator: GroupUnitGenerator = GroupUnitGenerator()
    units: dict[tuple[Unit], GroupUnit] = {}

    def __init__(self, generator: GroupUnitGenerator = None):
        if generator is not None:
            self.generator = generator
        else:
            self.generator = GroupUnitGenerator()

    def get_unit_by_nonce(self, nonce: tuple[Unit]) -> GroupUnit:
        for unit in self.units:
            if unit.nonce == nonce:
                return unit
        return None

    def find_next_nonce(self, nonce: tuple[Unit]) -> tuple[Unit]:
        # Find the active nonce type
        active_nonce = nonce[-1]
        nonce_type = type(active_nonce)

        match(nonce_type):
            case "int":
                return nonce[:-1] + (nonce_type(active_nonce) + 1,)

            case _:
                raise ValueError("Nonce type not supported.")
