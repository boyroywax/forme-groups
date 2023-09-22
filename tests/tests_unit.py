import unittest
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.unit_type_pool import UnitTypePool


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(value="test_value", type_ref="test_type_ref")

    def test_create_unit(self):
        self.assertIsInstance(self.unit, Unit)

    def test_unit_has_value(self):
        self.assertEqual(self.unit.value, "test_value")

    def test_unit_has_type_ref(self):
        self.assertEqual(self.unit.type_ref, "test_type_ref")

