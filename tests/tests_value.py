import unittest
import json
from src.groups.units import UnitValue as Value_


class TestValue(unittest.TestCase):
    def setUp(self):
        self.value = Value_()

    def test_set_value(self):
        # Set the value of the Value_ object
        self.value.set_value(42)

        # Verify that the value was set correctly
        self.assertEqual(self.value.get_value(), 42)

    def test_set_value_super_type(self):
        # Set the value of the Value_ object
        self.value.set_value(42)

        # Verify that the value was set correctly
        self.assertEqual(self.value.get_value_super_type(), "int")

    def test_get_value(self):
        # Set the value of the Value_ object
        self.value.set_value(42)

        # Get the value of the Value_ object
        value = self.value.get_value()

        # Verify that the value was retrieved correctly
        self.assertEqual(value, 42)

    def test_get_value_super_type(self):
        # Set the value of the Value_ object
        self.value.set_value(42)

        # Get the super type of the value
        value_super_type = self.value.get_value_super_type()

        # Verify that the super type was retrieved correctly
        self.assertEqual(value_super_type, "int")

    def test_is_value_super_type(self):
        # Set the value of the Value_ object
        self.value.set_value(42)

        # Check if the value is of the correct super type
        is_super_type = self.value.is_value_super_type("int")

        # Verify that the check was performed correctly
        self.assertTrue(is_super_type)

    def test_force_super_type(self):
        # Set the value of the Value_ object
        self.value.set_value(42)

        # Force the value to be of a different super type
        self.value.force_super_type("float")

        # Verify that the value was forced to be of the correct super type
        self.assertEqual(self.value.get_value_super_type(), "float")

    def test_force_super_type_int(self):
        # Set the value of the Value_ object
        self.value.set_value(42)

        # Force the value to be an int
        self.value.force_super_type("int")

        # Verify that the value was forced to be an int
        self.assertEqual(self.value.get_value_super_type(), "int")
        self.assertEqual(self.value.get_value(), 42)

    def test_force_super_type_float(self):
        # Set the value of the Value_ object
        self.value.set_value(3.14)

        # Force the value to be a float
        self.value.force_super_type("float")

        # Verify that the value was forced to be a float
        self.assertEqual(self.value.get_value_super_type(), "float")
        self.assertEqual(self.value.get_value(), 3.14)

    def test_force_super_type_bool(self):
        # Set the value of the Value_ object
        self.value.set_value(True)

        # Force the value to be a bool
        self.value.force_super_type("bool")

        # Verify that the value was forced to be a bool
        self.assertEqual(self.value.get_value_super_type(), "bool")
        self.assertEqual(self.value.get_value(), True)

    def test_force_super_type_str(self):
        # Set the value of the Value_ object
        self.value.set_value("hello")

        # Force the value to be a str
        self.value.force_super_type("str")

        # Verify that the value was forced to be a str
        self.assertEqual(self.value.get_value_super_type(), "str")
        self.assertEqual(self.value.get_value(), "hello")

    def test_force_super_type_list(self):
        # Set the value of the Value_ object
        self.value.set_value([1, 2, 3])

        # Force the value to be a list
        self.value.force_super_type("list")

        # Verify that the value was forced to be a list
        self.assertEqual(self.value.get_value_super_type(), "list")
        self.assertEqual(self.value.get_value(), [1, 2, 3])

    def test_force_super_type_dict(self):
        # Set the value of the Value_ object
        self.value.set_value({"a": 1, "b": 2, "c": 3}, super_type="dict")

        # Force the value to be a dict
        # self.value.force_super_type("dict")

        # Verify that the value was forced to be a dict
        self.assertEqual(self.value.get_value_super_type(), "dict")
        self.assertEqual(self.value.get_value(), {"a": 1, "b": 2, "c": 3})

    def test_to_dict(self):
        # Set the value of the Value_ object
        self.value.set_value(42, super_type="int")

        # Convert the Value_ object to a dictionary
        value_dict = self.value.to_dict()

        # Verify that the dictionary contains the correct value
        self.assertEqual(value_dict["value"], 42)

    def test_to_json(self):
        # Set the value of the Value_ object
        self.value.set_value(42)

        # Convert the Value_ object to a JSON string
        value_json = self.value.to_json()

        # Parse the JSON string and verify that it contains the correct value
        value_dict = json.loads(value_json)
        self.assertEqual(value_dict["value"], 42)

