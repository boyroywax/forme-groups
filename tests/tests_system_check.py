import unittest
from unittest.mock import MagicMock
from src.groups.system.check import SystemCheck


class TestSystemCheck(unittest.TestCase):
    def setUp(self):
        self.check = SystemCheck()

    def test_check_system_with_system_types(self):
        # Mock the check_supported_system_types() method
        self.check.check_supported_system_types = MagicMock()

        # Call the check_system() method with "system_types" in the process list
        self.check.check_system(["system_types"])

        # Verify that the check_supported_system_types() method was called
        self.check.check_supported_system_types.assert_called_once()

    def test_check_system_without_system_types(self):
        # Mock the check_supported_system_types() method
        self.check.check_supported_system_types = MagicMock()

        # Call the check_system() method without "system_types" in the process list
        self.check.check_system([])

        # Verify that the check_supported_system_types() method was called
        self.check.check_supported_system_types.assert_called_once()

    def test_check_supported_system_types(self):
        # Call the check_supported_system_types() method
        supported_types = self.check.check_supported_system_types()

        # Verify that the supported types are correct
        expected_types = ["bytes", "str", "int", "float", "bool", "list", "tuple", "dict", "set", "frozenset", "complex", "range", "memoryview", "None"]
        self.assertEqual(supported_types, expected_types)
