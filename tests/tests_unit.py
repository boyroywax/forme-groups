import unittest

from src.groups.unit import Unit
from src.groups.value import Value
from src.groups.value_type import ValueType


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.value_type = ValueType('int', ['int'])
        self.value = Value(42)
        self.unit = Unit(self.value_type, self.value)

    def test_type_getter(self):
        self.assertEqual(self.unit.type, self.value_type)

    def test_type_setter(self):
        new_value_type = ValueType('float', ['float'])
        self.unit.type = new_value_type
        self.assertEqual(self.unit.type, new_value_type)

    def test_value_getter(self):
        self.assertEqual(self.unit.value, self.value)

    def test_value_setter(self):
        new_value = Value(84)
        self.unit.value = new_value
        self.assertEqual(self.unit.value, new_value)

    def test_freeze(self):
        self.assertFalse(self.unit.frozen)
        self.unit.freeze()
        self.assertTrue(self.unit.frozen)
        with self.assertRaises(Exception):
            self.unit.value = Value(96)