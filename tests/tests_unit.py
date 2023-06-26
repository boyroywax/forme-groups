import unittest
from unittest.mock import patch
from src.groups.units import Unit, UnitType, UnitValue


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit()

    def test_set_value(self):
        # Set the value of the unit object
        self.unit.set_value(42)

        # Verify that the value was set correctly
        self.assertEqual(self.unit.get_value().get_value(), 42)

    def test_get_value(self):
        # Set the value of the unit object
        self.unit.set_value(42)

        # Get the value of the unit object
        value = self.unit.get_value().get_value()

        # Verify that the value was retrieved correctly
        self.assertEqual(value, 42)

    def test_get_value_super_type(self):
        # Set the value of the unit object
        self.unit.set_value(42)

        # Get the super type of the value
        value_super_type = self.unit.get_value().get_value_super_type()

        # Verify that the super type was retrieved correctly
        self.assertEqual(value_super_type, "int")

    def test_is_value_super_type(self):
        # Set the value of the unit object
        self.unit.set_value(42)

        # Check if the value is of the correct super type
        is_super_type = self.unit.get_value().is_value_super_type("int")

        # Verify that the check was performed correctly
        self.assertTrue(is_super_type)

    def test_force_super_type(self):
        # Set the value of the unit object
        self.unit.set_value(42)

        # Force the value to be of a different super type
        self.unit.get_value().force_super_type("float")

        # Verify that the value was forced to be of the correct super type
        self.assertEqual(self.unit.get_value().get_value_super_type(), "float")
