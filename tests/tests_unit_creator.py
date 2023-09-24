import unittest
import sys
from attrs import exceptions as excs

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")
from src.groups.unit_type import UnitTypeRef, UnitTypeFunction, UnitType
from src.groups.unit_type_pool import UnitTypePool
from src.groups.unit_creator import UnitCreator


class TestUnitCreator(unittest.TestCase):

    def setUp(self) -> None:
        self.unit_creator = UnitCreator()

    def test_create_unit_creator(self):
        self.assertIsInstance(self.unit_creator, UnitCreator)

    def test_unit_creator_has_unit_type_pool(self):
        self.assertIsInstance(self.unit_creator.unit_type_pool, UnitTypePool)
        self.assertGreater(len(self.unit_creator.unit_type_pool.items), 0)

    def test_unit_creator_create_unit(self):
        unit = self.unit_creator.create_unit(value="test_value", alias="str")
        self.assertEqual(unit.value, "test_value")
        self.assertEqual(unit.type_ref, "str")

    def test_unit_creator_create_unit_with_no_alias(self):
        with self.assertRaises(ValueError):
            self.unit_creator.create_unit(value="test_value", alias="not_an_alias")

    def test_unit_creator_create_unit_with_no_value(self):
        unit = self.unit_creator.create_unit(value=None, alias="str")
        self.assertEqual(unit.value, None)

    def test_unit_creator_create_unit_with_no_value_and_no_alias(self):
        with self.assertRaises(ValueError):
            self.unit_creator.create_unit(value=None, alias="not_an_alias")

    def test_unit_creator_create_unit_dict(self):
        unit = self.unit_creator.create_unit(value={"test_key": "test_value"}, alias="dict")
        print(unit)
        self.assertEqual(unit.value["test_key"], "test_value")
