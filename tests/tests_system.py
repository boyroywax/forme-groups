import unittest
from src.groups.system import System


class TestSystem(unittest.TestCase):
    def test_init_with_defaults(self):
        # Create a new System object with default values
        system = System()

        # Verify that the supported types are correct
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
        self.assertEqual(system.defaults.get_system_types(), expected_types)

    def test_init_with_overrides(self):
        # Create a new System object with overridden values
        overrides = {
            "system_types": ["str", "int", "float"],
            "system_super_type": "int"
        }
        system = System(default_override=True, **overrides)

        # Verify that the supported types and super type are correct
        expected_types = ["str", "int", "float"]
        self.assertEqual(system.defaults.get_system_types(), expected_types)
        self.assertEqual(system.defaults.system_super_type, "int")

    def test_init_with_missing_overrides(self):
        # Verify that an error is raised when overrides are missing
        with self.assertRaises(ValueError):
            system = System(default_override=True, **{})

    def test_init_with_invalid_overrides(self):
        # Verify that an error is raised when overrides are invalid
        overrides = {
            "system_types": ["str", "int", "float"],
            "system_super_type": "int",
            "invalid": "invalid"
        }
        with self.assertRaises(ValueError):
            system = System(default_override=True, **overrides)
