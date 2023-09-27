import unittest
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')
from src.groups.unit_type import UnitTypeRef, UnitTypeFunction, UnitType
from src.groups.data_schema import DataSchema
from src.groups.data import Data
from src.groups.group_unit_creator import GroupUnitCreator


class TestData(unittest.TestCase):
    def setUp(self):
        self.group_unit_creator = GroupUnitCreator()
        self.schema_dict = {"name": UnitTypeRef(alias="str"), "age": UnitTypeRef(alias="int")}
        self.data_schema = DataSchema(items=self.schema_dict)
        self.unit1 = self.group_unit_creator.create_unit(alias="str", value="Alice")
        self.unit2 = self.group_unit_creator.create_unit(alias="int", value=20)
        self.data = self.group_unit_creator.create_data(schema=self.data_schema, items=[self.unit1, self.unit2])

    def test_create_data(self):
        self.assertIsInstance(self.data, Data)

    def test_data_has_schema(self):
        self.assertEqual(self.data.schema, self.data_schema)

    def test_data_has_schema2(self):
        self.assertTrue(self.data.has_schema)

    def test_data_has_items(self):
        self.assertEqual(self.data.items, (self.unit1, self.unit2))