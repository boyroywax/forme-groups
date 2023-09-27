import unittest
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.unit import Unit


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(value="test_value", type_ref="test_type_ref")

    def test_create_unit(self):
        self.assertIsInstance(self.unit, Unit)

    def test_unit_has_value(self):
        self.assertEqual(self.unit.value, "test_value")

    def test_unit_has_type_ref(self):
        print(self.unit.type_ref)
        self.assertEqual(self.unit.type_ref, "test_type_ref")

    def test_unit_is_frozen(self):
        unit = Unit(value="test_value", type_ref="test_type_ref")
        with self.assertRaises(FrozenInstanceError):
            unit.value = "new_value"

    def test_unit_str(self):
        self.assertEqual(str(self.unit), 'test_value')

    def test_unit_repr(self):
        self.assertEqual(repr(self.unit), "Unit(value=test_value, type_ref=test_type_ref)")

    def test_unit_slots(self):
        self.assertEqual(self.unit.__slots__, ("_value", "_type_ref",))


