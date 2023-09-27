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
        self.assertEqual(unit.value, 1)

    def test_contains_slots(self):
        self.assertEqual(self.group_unit_creator.__slots__, ("_unit_pool", "_unit_creator",))

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

    def test_create_group_unit_with_no_nonce(self):
        owners = GroupSubUnit(items=[Unit(value="Alice", type_ref=UnitTypeRef(alias="str"))])
        creds = GroupSubUnit(items=[Unit(value="password", type_ref=UnitTypeRef(alias="str"))])
        data = GroupSubUnit(items=[Unit(value=True, type_ref=UnitTypeRef(alias="bool"))])
        with self.assertRaises(TypeError):
            self.group_unit_creator.create_group_unit(nonce=None, owners=owners, creds=creds, data=data)

    def test_create_unit_with_no_alias(self):
        with self.assertRaises(ValueError):
            self.group_unit_creator.create_unit(alias="not_an_alias", value="test_value")

    def test_create_unit_already_in_pool(self):
        unit1 = self.group_unit_creator.create_unit(alias="int", value=1)
        unit2 = self.group_unit_creator.create_unit(alias="int", value=1)
        self.assertEqual(unit1, unit2)
        self.assertEqual(len(self.group_unit_creator._unit_pool.items), 1)

    def test_create_nonce_with_unit_not_in_pool(self):
        unit1 = self.group_unit_creator.create_unit(alias="int", value=1)
        unit2 = self.group_unit_creator.create_unit(alias="str", value="test")
        nonce = self.group_unit_creator.create_nonce([unit1, unit2])
        self.assertEqual(nonce.items, (unit1, unit2))
        self.assertEqual(len(self.group_unit_creator._unit_pool.items), 2)

    def test_create_multiple_units(self):
        num_units: int = 1000
        for i in range(num_units):
            # print(i)
            self.group_unit_creator.create_unit(alias="int", value=i)
        self.assertEqual(len(self.group_unit_creator._unit_pool.items), num_units)

    def test_create_multiple_nonces_and_get_pool_hash(self):
        num_units: int = 1000
        for i in range(num_units):
            # print(i)
            self.group_unit_creator.create_unit(alias="int", value=i)
        self.assertEqual(len(self.group_unit_creator._unit_pool.items), num_units)
        self.group_unit_creator._unit_pool.freeze()
        pool_hash = self.group_unit_creator._unit_pool.hash_tree()
        self.assertEqual(pool_hash.root(), "99785fbfa2ad2f241e35df0703f90c02befc76b2461f171f8066433ab9b37d48")

    def test_create_multiple_nonces_and_get_pool_hash_with_multiple_types(self):
        num_units: int = 1000
        for i in range(num_units):
            # print(i)
            self.group_unit_creator.create_unit(alias="int", value=i)
            self.group_unit_creator.create_unit(alias="str", value=str(i))
            self.group_unit_creator.create_unit(alias="float", value=float(i))
        self.assertEqual(len(self.group_unit_creator._unit_pool.items), num_units * 3)
        self.group_unit_creator._unit_pool.freeze()
        pool_hash = self.group_unit_creator._unit_pool.hash_tree()
        self.assertEqual(pool_hash.root(), "51c317c60e8a5c9f20ecc78243791049eae62f5f93d9f87e93dcac5f133098bb")

