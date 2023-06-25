import unittest
import os
from src.groups.system.defaults import SystemDefaults


class TestSystemDefaults(unittest.TestCase):
    def setUp(self):
        self.defaults = SystemDefaults()

    def test_system_types(self):
        expected_types = [
            "bytes",
            "str",
            "int",
            "float",
            "bool",
            "list",
            "tuple",
            "dict",
            "set",
            "frozenset",
            "complex",
            "range",
            "memoryview",
            "None"
        ]
        self.assertEqual(self.defaults.system_types, expected_types)

    def test_system_super_type(self):
        self.assertEqual(self.defaults.system_super_type, "str")

    def test_override_defaults(self):
        overrides = {
            "system_types": ["str", "int", "float"],
            "system_super_type": "int"
        }
        self.defaults.override_defaults(overrides)
        self.assertEqual(self.defaults.system_types, ["str", "int", "float"])
        self.assertEqual(self.defaults.system_super_type, "int")

    def test_override_defaults_system_types(self):
        overrides = {
            "system_types": ["str", "int", "float", "bool", "list", "tuple"],
        }
        self.defaults.override_defaults(overrides)
        self.assertEqual(
            self.defaults.system_types,
            ["str", "int", "float", "bool", "list", "tuple"]
        )

    def test_override_defaults_unlikely_super_type(self):
        overrides = {
            "system_types": ["str", "int", "invalid"],
            "system_super_type": "int"
        }
        self.defaults.override_defaults(overrides)
        self.assertNotEqual(self.defaults.system_types, ["str", "int"])
        self.assertEqual(self.defaults.system_super_type, "int")

    def test_system_defaults_to_json_file(self):
        # Create a temporary file path for the JSON file
        json_file = "test_system_defaults.json"

        # Call the system_defaults_to_json_file() method to write the defaults to the JSON file
        self.defaults.system_defaults_to_json_file(json_file)

        # Read the contents of the JSON file
        with open(json_file, "r") as f:
            json_contents = f.read()

        # Verify that the contents of the JSON file match the expected contents
        expected_contents = """{"system_types": ["bytes", "str", "int", "float", "bool", "list", "tuple", "dict", "set", "frozenset", "complex", "range", "memoryview", "None"], "system_super_type": "str"}"""

        self.maxDiff = None
        self.assertEqual(json_contents, expected_contents)

        # Delete the temporary JSON file
        os.remove(json_file)
