import unittest

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')
from src.groups.nonce import Nonce
from src.groups.unit import Unit
from src.groups.unit_type import UnitTypeRef


class TestNonce(unittest.TestCase):
    def test_init(self):
        items = [Unit(value=1, type_ref=UnitTypeRef(alias="int"))]
        nonce = Nonce(items=items)
        self.assertEqual(nonce.items, items)

    def test_init_with_tuple(self):
        items = (Unit(value=1, type_ref=UnitTypeRef(alias="int")),)
        nonce = Nonce(items=items)
        self.assertEqual(nonce.items, tuple(items))

    def test_init_with_none(self):
        with self.assertRaises(ValueError):
            nonce = Nonce(items=None)

    def test_get_by_tier(self):
        items = [
            Unit(value=1, type_ref=UnitTypeRef(alias="int")),
            Unit(value="test", type_ref=UnitTypeRef(alias="str")),
            Unit(value=True, type_ref=UnitTypeRef(alias="bool")),
        ]
        nonce = Nonce(items=items)
        self.assertEqual(nonce.get_by_tier(0), items[0])
        self.assertEqual(nonce.get_by_tier(1), items[1])
        self.assertEqual(nonce.get_by_tier(2), items[2])

    def test_str(self):
        items = [
            Unit(value=1, type_ref=UnitTypeRef(alias="int")),
            Unit(value="test", type_ref=UnitTypeRef(alias="str")),
            Unit(value=True, type_ref=UnitTypeRef(alias="bool")),
        ]
        nonce = Nonce(items=items)
        self.assertEqual(str(nonce), "1.test.True")

    def test_repr(self):
        items = [
            Unit(value=1, type_ref=UnitTypeRef(alias="int")),
            Unit(value="test", type_ref=UnitTypeRef(alias="str")),
            Unit(value=True, type_ref=UnitTypeRef(alias="bool")),
        ]
        nonce = Nonce(items=items)
        self.assertEqual(repr(nonce), f"Nonce(items={[repr(item) for item in items]})")

    def test_iter_int(self):
        items = [
            Unit(value=1, type_ref=UnitTypeRef(alias="int")),
            Unit(value=2, type_ref=UnitTypeRef(alias="int")),
            Unit(value=3, type_ref=UnitTypeRef(alias="int")),
        ]
        nonce = Nonce(items=items)
        nonce_iter = iter(nonce)
        next_nonce = next(nonce_iter)
        self.assertEqual(next_nonce.items[-1].value, 4)

    def test_iter_non_int(self):
        items = [
            Unit(value="test", type_ref=UnitTypeRef(alias="str")),
            Unit(value=True, type_ref=UnitTypeRef(alias="bool")),
        ]
        nonce = Nonce(items=items)
        with self.assertRaises(ValueError):
            nonce_iter = iter(nonce)
            next(nonce_iter)