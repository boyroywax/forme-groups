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
