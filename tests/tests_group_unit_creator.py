import unittest
import sys

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")

from src.groups.group_unit_creator import GroupUnitCreator
from src.groups.unit_pool import UnitPool
from src.groups.unit_creator import UnitCreator
from src.groups.nonce import Nonce
from src.groups.group_subunit import GroupSubUnit
from src.groups.group_unit import GroupUnit
from src.groups.unit import Unit, UnitTypeRef


class TestGroupUnitCreator(unittest.TestCase):
    def setUp(self):
        self.unit_pool = UnitPool()
        self.unit_creator = UnitCreator()
        self.group_unit_creator = GroupUnitCreator()

    def test_create_unit(self):
        unit = self.group_unit_creator.create_unit(alias="int", value=1)
        self.assertIsInstance(unit, Unit)
        self.assertEqual(unit.type_ref, "int")
        self.assertEqual(unit.value, 0)

    def test_create_nonce(self):
        unit1 = self.group_unit_creator.create_unit(alias="int", value=1)
        unit2 = self.group_unit_creator.create_unit(alias="str", value="test")
        nonce = self.group_unit_creator.create_nonce([unit1, unit2])
        self.assertIsInstance(nonce, Nonce)
        self.assertEqual(nonce.items, (unit1, unit2))

    def test_create_group_subunit(self):
        subunit = self.group_unit_creator.create_group_subunit()
        self.assertIsInstance(subunit, GroupSubUnit)
        self.assertEqual(subunit.items, ())

    def test_create_group_unit(self):
        nonce = Nonce(items=[Unit(value=1, type_ref=UnitTypeRef(alias="int"))])
        owners = GroupSubUnit(items=[Unit(value="Alice", type_ref=UnitTypeRef(alias="str"))])
        creds = GroupSubUnit(items=[Unit(value="password", type_ref=UnitTypeRef(alias="str"))])
        data = GroupSubUnit(items=[Unit(value=True, type_ref=UnitTypeRef(alias="bool"))])
        group_unit = self.group_unit_creator.create_group_unit(nonce=nonce, owners=owners, creds=creds, data=data)
        self.assertIsInstance(group_unit, GroupUnit)
        self.assertEqual(group_unit.nonce, nonce)
        self.assertEqual(group_unit.owners, owners)
        self.assertEqual(group_unit.creds, creds)
        self.assertEqual(group_unit.data, data)