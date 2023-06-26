import unittest
from src.groups.system.type import SystemType


class TestSystemType(unittest.TestCase):
    def test_to_dict(self):
        # Create a new SystemType object
        system_type = SystemType(
            id="test_type",
            alias=["test_alias"],
            super=None,
            prefix=None,
            suffix=None,
            separator=None,
            system_function=None
        )

        # Verify that the to_dict() method returns the correct dictionary
        expected_dict = {
            "id": "test_type",
            "alias": ["test_alias"],
            "super": None,
            "prefix": None,
            "suffix": None,
            "separator": None,
            "system_function": None
        }
        self.assertEqual(system_type.to_dict(), expected_dict)

    def test_to_json(self):
        # Create a new SystemType object
        system_type = SystemType(
            id="test_type",
            alias=["test_alias"],
            super=None,
            prefix=None,
            suffix=None,
            separator=None,
            system_function=None
        )

        # Verify that the to_json() method returns the correct JSON string
        expected_json = '{"id": "test_type", "alias": ["test_alias"], "super": null, "prefix": null, "suffix": null, "separator": null, "system_function": null}'
        self.assertEqual(system_type.to_json(), expected_json)

    def test_from_dict(self):
        # Create a dictionary representing a SystemType object
        system_type_dict = {
            "id": "test_type",
            "alias": ["test_alias"],
            "super": None,
            "prefix": None,
            "suffix": None,
            "separator": None,
            "system_function": None
        }

        # Verify that the from_dict() method returns the correct SystemType object
        expected_system_type = SystemType(
            id="test_type",
            alias=["test_alias"],
            super=None,
            prefix=None,
            suffix=None,
            separator=None,
            system_function=None
        )
        self.assertEqual(SystemType.from_dict(system_type_dict), expected_system_type)
