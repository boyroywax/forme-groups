import unittest
from unittest.mock import MagicMock
from src.groups.units import Unit
from src.groups.units import UnitType
from src.groups.units import UnitValue


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit()

    def test_set_value(self):
        # Set the value of the Unit object
        self.unit.set_value(UnitValue(42))

        # Verify that the value was set correctly
        self.assertEqual(self.unit.get_value_obj().get_value(), 42)

    def test_set_type(self):
        # Create a mock UnitType object
        mock_type = MagicMock()

        # Set the type of the Unit object
        self.unit.set_type_obj(mock_type)

        # Verify that the type was set correctly
        self.assertEqual(self.unit.get_type_obj(), mock_type)

    def test_create_and_set_type(self):
        # Create and set the type of the Unit object
        self.unit.create_and_set_type("m")

        # Verify that the type was created and set correctly
        self.assertEqual(self.unit.get_type_obj().get_id().__str__(), "m")

    def test_create_and_set_type_from_dict(self):
        # Create a mock UnitType object
        mock_type = MagicMock()

        # Create a dictionary representing the UnitType object
        type_dict = {"name": "m"}

        # Configure the mock UnitType object to return the dictionary
        mock_type.from_dict.return_value = type_dict

        # Create and set the type of the Unit object from the dictionary
        self.unit.create_and_set_type_from_dict(type_dict)

        # Verify that the type was created and set correctly
        self.assertEqual(self.unit.get_type_obj(), mock_type)

    def test_create_and_set_type_from_json(self):
        # Create a mock UnitType object
        mock_type = MagicMock()

        # Create a JSON string representing the UnitType object
        type_json = '{"name": "m"}'

        # Configure the mock UnitType object to return the JSON string
        mock_type.from_json.return_value = type_json

        # Create and set the type of the Unit object from the JSON string
        self.unit.create_and_set_type_from_json(type_json)

        # Verify that the type was created and set correctly
        self.assertEqual(self.unit.get_type_obj(), mock_type)

    def test_get_value(self):
        # Set the value of the Unit object
        self.unit.set_value(UnitValue(42))

        # Get the value of the Unit object
        value = self.unit.get_value()

        # Verify that the value was retrieved correctly
        self.assertEqual(value, '{"value": 42}')

    def test_get_type(self):
        # Create and set the type of the Unit object
        self.unit.create_and_set_type("m")

        # Get the type of the Unit object
        type_ = self.unit.get_type()

        # Verify that the type was retrieved correctly
        self.assertEqual(type_, '{"name": "m"}')

    def test_to_dict(self):
        # Set the value and type of the Unit object
        self.unit.set_value(UnitValue(42))
        self.unit.create_and_set_type("m")

        # Convert the Unit object to a dictionary
        unit_dict = self.unit.to_dict()

        # Verify that the dictionary was created correctly
        self.assertEqual(unit_dict["value"]["value"], 42)
        self.assertEqual(unit_dict["type"]["name"], "m")