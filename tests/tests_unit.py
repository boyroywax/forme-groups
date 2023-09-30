import unittest
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.unit import Unit
from src.groups.interfaces.value import ValueInterface


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(ValueInterface(value=1))

    def test_create_unit(self):
        self.assertIsInstance(self.unit, Unit)

    def test_unit_slots(self):
        self.assertEqual(self.unit.__slots__, ("_unit",))

    def test_unit_value(self):
        self.assertEqual(self.unit.value, 1)

    def test_unit_type_ref(self):
        self.assertEqual(self.unit.type_ref, "int")



