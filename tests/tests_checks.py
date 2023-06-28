import unittest
from src.groups.base.type.checks import Checks


class TestChecks(unittest.TestCase):
    def test_check_value_for_empty(self):
        # Test checking an empty string
        self.assertTrue(Checks.check_value_for_empty(""))

        # Test checking a non-empty string
        self.assertFalse(Checks.check_value_for_empty("test"))

        # Test checking an empty dictionary
        self.assertTrue(Checks.check_value_for_empty({}))

        # Test checking a non-empty dictionary
        self.assertFalse(Checks.check_value_for_empty({"test_key": "test_value"}))

        # Test checking an empty list
        self.assertTrue(Checks.check_value_for_empty([]))

        # Test checking a non-empty list
        self.assertFalse(Checks.check_value_for_empty(["test"]))

        # Test checking None
        self.assertTrue(Checks.check_value_for_empty(None))

        # Test checking a non-empty boolean
        self.assertFalse(Checks.check_value_for_empty(True))