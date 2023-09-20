import unittest
import sys
from unittest.mock import MagicMock

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")

from src.groups.unit import UnitTypeRef, UnitTypeFunction, UnitType, UnitTypePool, Unit, UnitGenerator
from src.groups.nonce import Pool


class TestPool(unittest.TestCase):
    def test_init(self):
        items = [1, 2, 3]
        pool = Pool(items)
        self.assertEqual(pool.items, items)

    def test_init_empty(self):
        pool = Pool()
        self.assertEqual(pool.items, [])

    def test_init_freeze(self):
        items = [1, 2, 3]
        pool = Pool(items, freeze=True)
        self.assertEqual(pool.items, tuple(items))
        self.assertTrue(pool.frozen)

    def test_freeze(self):
        items = [1, 2, 3]
        pool = Pool(items)
        pool.freeze()
        self.assertEqual(pool.items, tuple(items))
        self.assertTrue(pool.frozen)

    def test_freeze_twice(self):
        items = [1, 2, 3]
        pool = Pool(items)
        pool.freeze()
        with self.assertRaises(Exception):
            pool.freeze()

    def test_add(self):
        pool = Pool()
        pool.add(1)
        self.assertEqual(pool.items, [1])

    def test_add_frozen(self):
        pool = Pool(freeze=True)
        with self.assertRaises(ValueError):
            pool.add(1)
