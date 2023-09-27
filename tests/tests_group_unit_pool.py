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
from src.groups.group_unit_pool import GroupUnitPool


class TestGroupUnitPool(unittest.TestCase):
    def setUp(self):
        self.group_unit_creator = GroupUnitCreator()
        nonce = self.group_unit_creator.create_nonce(
            [self.group_unit_creator.create_unit(alias="int", value=1)]
        )
        owners = self.group_unit_creator.create_group_subunit(
            [self.group_unit_creator.create_unit(alias="str", value="Alice")]
        )
        creds = self.group_unit_creator.create_group_subunit(
            [self.group_unit_creator.create_unit(alias="str", value="password123")]
        )
        data = self.group_unit_creator.create_data(
            [self.group_unit_creator.create_unit(alias="bool", value=False)], None
        )
        self.group_unit1 = self.group_unit_creator.create_group_unit(nonce, owners, creds, data)

        nonce2 = self.group_unit_creator.create_nonce(
            [self.group_unit_creator.create_unit(alias="int", value=2)]
        )
        owners2 = self.group_unit_creator.create_group_subunit(
            [self.group_unit_creator.create_unit(alias="str", value="Bob")]
        )
        creds2 = self.group_unit_creator.create_group_subunit(
            [self.group_unit_creator.create_unit(alias="str", value="password456")]
        )
        data2 = self.group_unit_creator.create_data(
            [self.group_unit_creator.create_unit(alias="bool", value=True)], None
        )
        self.group_unit2 = self.group_unit_creator.create_group_unit(nonce2, owners2, creds2, data2)

    def test_add_item(self):
        pool = GroupUnitPool()
        pool.add(self.group_unit1)
        self.assertIn(self.group_unit1, pool)

    def test_add_duplicate_item(self):
        pool = GroupUnitPool()
        pool.add(self.group_unit1)
        with self.assertRaises(ValueError):
            pool.add(self.group_unit1)

    def test_contains_item(self):
        pool = GroupUnitPool([self.group_unit1])
        self.assertTrue(pool.contains(self.group_unit1))
        self.assertFalse(pool.contains(self.group_unit2))

    def test_freeze_pool(self):
        pool = GroupUnitPool([self.group_unit1])
        pool.freeze()
        with self.assertRaises(ValueError):
            pool.add(self.group_unit2)

    def test_iterate_pool(self):
        pool = GroupUnitPool([self.group_unit1, self.group_unit2])
        units = [unit for unit in pool]
        self.assertEqual(units, [self.group_unit1, self.group_unit2])

    def test_hash_tree(self):
        pool = GroupUnitPool([self.group_unit1, self.group_unit2])
        pool.freeze()
        self.assertEqual(
            pool.hash_tree().root(),
            "0e80260fe576848e54bb6207320002e7f139ab64eb64758411de7bcee376e737",
        )

    def test_hash_tree_with_new_item(self):
        nonce3 = self.group_unit_creator.create_nonce(
            [self.group_unit_creator.create_unit(alias="int", value=3)]
        )
        owners3 = self.group_unit_creator.create_group_subunit(
            [self.group_unit_creator.create_unit(alias="str", value="Charlie")]
        )
        creds3 = self.group_unit_creator.create_group_subunit(
            [self.group_unit_creator.create_unit(alias="str", value="password789")]
        )
        data3 = self.group_unit_creator.create_data(
            [self.group_unit_creator.create_unit(alias="bool", value=True)], None
        )
        group_unit3 = self.group_unit_creator.create_group_unit(nonce3, owners3, creds3, data3)

        pool = GroupUnitPool([self.group_unit1, self.group_unit2, group_unit3])
        pool.freeze()
        self.assertNotEqual(
            pool.hash_tree().root(),
            "0e80260fe576848e54bb6207320002e7f139ab64eb64758411de7bcee376e737",
        )

    def test_str(self):
        pool = GroupUnitPool([self.group_unit1, self.group_unit2])
        self.maxDiff = None
        self.assertEqual(
            pool.__str__(),
            'Nonce: 1, Owners: Alice, Creds: password123, Data: False; Nonce: 2, Owners: Bob, Creds: password456, Data: True'
        )

