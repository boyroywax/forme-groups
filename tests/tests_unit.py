import unittest
from unittest.mock import MagicMock
from src.groups.units import Unit, UnitType, UnitValue


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit()

    def test_set_value(self):
        # Set the value of the Unit object
        self.unit.set_value(UnitValue(42))

        # Verify that the value was set correctly
        self.assertEqual(self.unit.get_value(), 42)

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
        self.assertEqual(value.to_json(), '{"value": 42}')

    def test_get_type(self):
        # Create and set the type of the Unit object
        self.unit.create_and_set_type("m")

        # Get the type of the Unit object
        type_ = self.unit.get_type()

        # Verify that the type was retrieved correctly
        self.assertEqual(type_, 'm')

    def test_to_dict(self):
        # Set the value and type of the Unit object
        self.unit.set_value(UnitValue(42))
        # self.unit.create_and_set_type("m")

        # Convert the Unit object to a dictionary
        unit_dict = self.unit.to_dict()

        # Verify that the dictionary was created correctly
        self.assertEqual(unit_dict["value"], 42)
        # self.assertEqual(unit_dict["type"]["name"], "m")

    # def test_set_value_obj(self):
    #     # Test setting the value object
    #     value = UnitValue("test")
    #     unit = Unit()
    #     unit.set_value_obj(value)
    #     self.assertEqual(unit.value_, value)

    # def test_set_value(self):
    #     # Test setting the value with a string
    #     unit = Unit()
    #     unit.set_value("test")
    #     self.assertEqual(unit.value_.get_value(), "test")

    #     # Test setting the value with a string and super type
    #     unit.set_value("test", "str")
    #     self.assertEqual(unit.value_.get_value(), "test")
    #     self.assertEqual(unit.value_.get_value_super_type(), "str")

    def test_set_type_obj(self):
        # Test setting the type object
        type_ = UnitType("test_type")
        unit = Unit()
        unit.set_type_obj(type_)
        self.assertEqual(unit.type_, type_)

    def test_init(self):
        # Test initializing the Unit class with a value object and type object
        value_ = UnitValue("test")
        type_ = UnitType("str")
        unit = Unit(value_, type_)
        self.assertEqual(unit.value_, value_)
        self.assertEqual(unit.type_, type_)

        # Test initializing the Unit class with a value object
        unit = Unit(value_)
        self.assertEqual(unit.value_, value)

        # Test initializing the Unit class with a type object
        unit = Unit(type_=type_)
        self.assertEqual(unit.type_, type_)