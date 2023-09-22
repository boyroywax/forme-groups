import unittest
import sys
from unittest.mock import MagicMock

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")

from src.groups.unit_type import UnitTypeRef, UnitTypeFunction, UnitType
from src.groups.pool import GenericPool, PoolInterface


class TestPool(unittest.TestCase):
    def test_init(self):
        items = [1, 2, 3]
        pool = GenericPool(items)
        self.assertEqual(pool.items, items)

    def test_init_empty(self):
        pool = GenericPool()
        self.assertEqual(pool.items, [])

    def test_init_freeze(self):
        items = [1, 2, 3]
        pool = GenericPool(items, freeze=True)
        self.assertEqual(pool.items, tuple(items))
        self.assertTrue(pool.frozen)

    def test_freeze(self):
        items = [1, 2, 3]
        pool = GenericPool(items)
        pool.freeze()
        self.assertEqual(pool.items, tuple(items))
        self.assertTrue(pool.frozen)

    def test_freeze_twice(self):
        items = [1, 2, 3]
        pool = GenericPool(items)
        pool.freeze()
        with self.assertRaises(Exception):
            pool.freeze()

    def test_add(self):
        pool = GenericPool()
        pool.add(1)
        self.assertEqual(pool.items, [1])

    def test_add_frozen(self):
        pool = GenericPool(freeze=True)
        with self.assertRaises(ValueError):
            pool.add(1)

    def test_add_duplicate(self):
        pool = GenericPool()
        pool.add(1)
        with self.assertRaises(ValueError):
            pool.add(1)

    def test_contains(self):
        pool = GenericPool()
        pool.add(1)
        self.assertTrue(pool.contains(1))
        self.assertFalse(pool.contains(2))

    def test_str(self):
        pool = GenericPool()
        pool.add(1)
        self.assertEqual(str(pool), "[1]")

    def test_repr(self):
        pool = GenericPool()
        pool.add(1)
        self.assertEqual(repr(pool), "GenericPool(items=[1])")

    def test_iter(self):
        pool = GenericPool()
        pool.add(1)
        pool.add(2)
        self.assertEqual([item for item in pool], [1, 2])

    def test_hash_tree(self):
        pool = GenericPool()
        pool.add(1)
        pool.add(2)
        pool.add(3)
        hash_tree = pool.hash_tree()
        hash_tree.build()
        print(hash_tree.levels)
        self.assertEqual(hash_tree.root(), "f3f1917304e3af565b827d1baa9fac18d5b287ae97adda22dc51a0aef900b787")
        pool.add(4)
        new_hash_tree = pool.hash_tree()
        new_hash_tree.build()
        print(new_hash_tree.levels)
        self.assertEqual(new_hash_tree.root(), "85df8945419d2b5038f7ac83ec1ec6b8267c40fdb3b1e56ff62f6676eb855e70")
