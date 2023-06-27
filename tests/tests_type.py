import json
import os
import unittest
from unittest.mock import MagicMock
from src.groups.units import UnitType as Type_
from src.groups.units import UnitValue as Value_


class TestType(unittest.TestCase):
    def setUp(self):
        self.type = Type_()

    def test_set_id(self):
        # Set the id of the Type_ object
        self.type.set_id(Value_(42))

        # Verify that the id was set correctly
        self.assertEqual(self.type.id.get_value(), 42)

    def test_set_alias(self):
        # Set the alias of the Type_ object
        self.type.set_alias(Value_("m"))

        # Verify that the alias was set correctly
        self.assertEqual(self.type.alias.get_value(), "m")

    def test_set_prefix(self):
        # Set the prefix of the Type_ object
        self.type.set_prefix(Value_("k"))

        # Verify that the prefix was set correctly
        self.assertEqual(self.type.prefix.get_value(), "k")

    def test_set_suffix(self):
        # Set the suffix of the Type_ object
        self.type.set_suffix(Value_("s"))

        # Verify that the suffix was set correctly
        self.assertEqual(self.type.suffix.get_value(), "s")

    def test_set_separator(self):
        # Set the separator of the Type_ object
        self.type.set_separator(Value_("-"))

        # Verify that the separator was set correctly
        self.assertEqual(self.type.separator.get_value(), "-")

    def test_set_super(self):
        # Create a mock Type_ object
        mock_type = MagicMock()

        # Set the super of the Type_ object
        self.type.set_super(mock_type)

        # Verify that the super was set correctly
        self.assertEqual(self.type.super, mock_type)

    def test_set_system_function(self):
        # Create a mock system function
        mock_system_function = MagicMock()

        # Set the system function of the Type_ object
        self.type.set_system_function(mock_system_function)

        # Verify that the system function was set correctly
        self.assertEqual(self.type.system_function, mock_system_function)

    def test_init(self):
        # Create a new Type_ object
        type_ = Type_()

        # Verify that all the attributes are None
        self.assertIsNone(type_.id)
        self.assertIsNone(type_.alias)
        self.assertIsNone(type_.prefix)
        self.assertIsNone(type_.suffix)
        self.assertIsNone(type_.separator)
        self.assertIsNone(type_.super)
        self.assertIsNone(type_.system_function)

    def test_init_with_arguments(self):
        # Create a new Type_ object with arguments
        type_ = Type_(
            id="test_id",
            alias="test_alias",
            prefix="test_prefix",
            suffix="test_suffix",
            separator="test_separator",
            super=None,
            system_function=str,
        )

        # Verify that all the attributes are set correctly
        self.assertEqual(type_.id, "test_id")
        self.assertEqual(type_.alias, "test_alias")
        self.assertEqual(type_.prefix, "test_prefix")
        self.assertEqual(type_.suffix, "test_suffix")
        self.assertEqual(type_.separator, "test_separator")
        self.assertEqual(type_.super, None)
        self.assertEqual(type_.system_function.__name__, "str")

    def test_to_json_file(self):
        # Create a new Type_ object with some attributes
        type_ = Type_(
            id="test_id",
            alias="test_alias",
            prefix="test_prefix",
            suffix="test_suffix",
            separator="test_separator",
            super=None,
            system_function=str.__name__,
        )

        # Write the Type_ object to a JSON file
        path = "test.json"
        type_.to_json_file(path)

        # Read the JSON file and parse the contents
        with open(path, "r") as file:
            json_str = file.read()
        json_dict = json.loads(json_str)

        # Verify that the JSON file contains the correct attributes
        self.assertEqual(json_dict["id"], "test_id")
        self.assertEqual(json_dict["alias"], "test_alias")
        self.assertEqual(json_dict["prefix"], "test_prefix")
        self.assertEqual(json_dict["suffix"], "test_suffix")
        self.assertEqual(json_dict["separator"], "test_separator")

        # Clean up the test file
        os.remove(path)
