import unittest
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')
from src.groups.unit_type import UnitTypeRef, UnitTypeFunction, UnitType
from src.groups.data_schema import DataSchema
from src.groups.group_unit_creator import GroupUnitCreator


class TestDataSchema(unittest.TestCase):
    def setUp(self):
        self.group_unit_creator = GroupUnitCreator()
        self.data_dict = {"name": UnitTypeRef(alias="str"), "age": UnitTypeRef(alias="int")}
        self.data_schema = DataSchema(items=self.data_dict)

    def test_create_data_schema(self):
        self.assertIsInstance(self.data_schema, DataSchema)

    def test_data_schema_has_items(self):
        self.assertEqual(self.data_schema.items, self.data_dict)

    def test_data_schema_is_frozen(self):
        data_schema = DataSchema(items=self.data_dict)
        with self.assertRaises(FrozenInstanceError):
            data_schema.items = {"test": UnitTypeRef(alias="str")}

    def test_data_schema_slots(self):
        self.assertEqual(self.data_schema.__slots__, ("items",))
