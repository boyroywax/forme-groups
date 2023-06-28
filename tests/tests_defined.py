import unittest
from unittest.mock import mock_open, patch
from src.groups.types.defined import Defined
from src.groups.types.type import Type as TypeClass


class TestDefined(unittest.TestCase):
    def setUp(self) -> None:
        self.defined = Defined()

    # @patch("builtins.open", new_callable=mock_open, read_data='[{"id": "type1", "aliases": ["alias1", "alias2"]}]')
    def test_load(self):
        # Test loading defined types from JSON file

        defined = self.defined._load()
        self.assertEqual(len(defined), 2)
        self.assertEqual(defined[0].id, "type1")
        self.assertEqual(defined[0].aliases, ["alias1", "alias2"])

    def test_load_from_list(self):
        # Test loading defined types from list
        data = [
            {"id": "type1", "aliases": ["alias1", "alias2"], "super_type": "string", "prefix": "1:", "suffix": ":1", "separator": "", "system_function": "<class 'string'>"},
            {"id": "type2", "aliases": ["alias3", "alias4"], "super_type": "string", "prefix": "2:", "suffix": ":2", "separator": "", "system_function": "<class 'string'>"}
        ]
        defined = self.defined._load_from_list(data)
        self.assertEqual(len(defined), 2)
        self.assertEqual(defined[0].id['id'], "type1")
        self.assertEqual(defined[0].aliases, ["alias1", "alias2"])
        self.assertEqual(defined[1].id, "type2")
        self.assertEqual(defined[1].aliases, ["alias3", "alias4"])

    def test_get_defined(self):
        # Test getting defined types when no defined types are set
        # self.assertEqual(self.defined.get_defined(), [])

        # Test getting defined types when defined types are set
        type1 = TypeClass("type1", ["alias1", "alias2"], "string", "1:", ":1", "", "<class 'string'>")
        type2 = TypeClass("type2", ["alias3", "alias4"], "string", "2:", ":2", "", "<class 'string'>")
        self.defined._defined = [type1, type2]
        self.assertEqual(self.defined.get_defined(), [type1, type2])

    def test_get(self):
        # Test getting a defined type by ID when no defined types are set
        # self.assertIsNone(self.defined.get("type1"))

        # Test getting a defined type by ID when defined types are set
        type1 = TypeClass("type1", ["alias1", "alias2"], "string", "1:", ":1", "", "<class 'string'>")
        type2 = TypeClass("type2", ["alias3", "alias4"], "string", "2:", ":2", "", "<class 'string'>")
        self.defined._defined = [type1, type2]
        self.assertEqual(self.defined.get("type1"), type1)
        self.assertEqual(self.defined.get("type2"), type2)
        self.assertIsNone(self.defined.get("type3"))

    def test_get_by_alias(self):
        # Test getting a defined type by alias when no defined types are set
        # self.assertIsNone(self.defined.get_by_alias("alias1"))

        # Test getting a defined type by alias when defined types are set
        type1 = TypeClass("type1", ["alias1", "alias2"])
        type2 = TypeClass("type2", ["alias3", "alias4"])
        self.defined._defined = [type1, type2]
        self.assertEqual(self.defined.get_by_alias("alias1"), type1)
        self.assertEqual(self.defined.get_by_alias("alias2"), type1)
        self.assertEqual(self.defined.get_by_alias("alias3"), type2)
        self.assertEqual(self.defined.get_by_alias("alias4"), type2)
        self.assertIsNone(self.defined.get_by_alias("alias5"))

    def test_set_defined(self):
        # Test setting defined types
        type1 = TypeClass("type1", ["alias1", "alias2"])
        type2 = TypeClass("type2", ["alias3", "alias4"])
        self.defined.set_defined([type1, type2])
        self.assertEqual(self.defined.get_defined(), [type1, type2])