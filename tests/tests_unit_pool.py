import unittest
import sys
from attrs import exceptions as excs

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")
from src.groups.unit_pool import UnitPool
from src.groups.unit import Unit
from src.groups.merkle_tree import MerkleTree
from src.groups.unit_creator import UnitCreator


class TestUnitPool(unittest.TestCase):
    def setUp(self):
        self.pool = UnitPool()
        self.unit_creator = UnitCreator()

    def test_add(self):
        unit1 = self.unit_creator.create_unit(value="test_value", alias="str")
        self.pool.add(unit1)
        self.assertIn(unit1, self.pool.items)

    def test_add_frozen(self):
        unit1 = self.unit_creator.create_unit(value="test_value", alias="str")
        self.pool.freeze()
        with self.assertRaises(ValueError):
            self.pool.add(unit1)

    def test_check_slots(self):
        self.assertEqual(self.pool.__slots__, ("_frozen", "items",))

    def test_add_duplicate(self):
        unit1 = self.unit_creator.create_unit(value="test_value", alias="str")
        self.pool.add(unit1)
        with self.assertRaises(ValueError):
            self.pool.add(unit1)

    def test_contains(self):
        unit1 = self.unit_creator.create_unit(value="test_value", alias="str")
        self.pool.add(unit1)
        self.assertTrue(self.pool.contains(unit1))

    def test_not_contains(self):
        unit1 = self.unit_creator.create_unit(value="test_value", alias="str")
        unit2 = self.unit_creator.create_unit(value="test_value2", alias="str")
        self.pool.add(unit1)
        self.assertFalse(self.pool.contains(unit2))

    def test_freeze(self):
        self.pool.freeze()
        self.assertTrue(self.pool.frozen)

    def test_freeze_twice(self):
        self.pool.freeze()
        with self.assertRaises(ValueError):
            self.pool.freeze()

    def test_hash_tree(self):
        unit1 = self.unit_creator.create_unit(value="test_value", alias="str")
        self.pool.add(unit1)
        unit2 = self.unit_creator.create_unit(value="test_value2", alias="str")
        self.pool.add(unit2)
        self.pool.freeze()
        tree = self.pool.hash_tree()
        # print(tree)
        self.assertIsInstance(tree, MerkleTree)

    def test_hash_tree_not_frozen(self):
        unit1 = self.unit_creator.create_unit(value="test_value", alias="str")
        self.pool.add(unit1)
        unit2 = self.unit_creator.create_unit(value="test_value2", alias="str")
        self.pool.add(unit2)
        with self.assertRaises(ValueError):
            self.pool.hash_tree()