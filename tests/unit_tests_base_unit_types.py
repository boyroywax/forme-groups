import unittest
from groups.modules.base_unit_types import BaseUnitTypes, BaseUnitType

class TestBaseUnitTypes(unittest.TestCase):
    def setUp(self):
        self.base_unit_types = BaseUnitTypes()

    def test_initial_state(self):
        self.assertEqual(len(self.base_unit_types.get_unit_types_list()), 1)
        self.assertEqual(self.base_unit_types.get_unit_types_list()[0].name, "string")

    def test_set_unit_types_list(self):
        unit_types_list = [BaseUnitType("integer"), BaseUnitType("float")]
        self.base_unit_types.set_unit_types_list(unit_types_list)
        self.assertEqual(len(self.base_unit_types.get_unit_types_list()), 2)
        self.assertEqual(self.base_unit_types.get_unit_types_list()[0].name, "integer")
        self.assertEqual(self.base_unit_types.get_unit_types_list()[1].name, "float")

    def test_add_unit_type(self):
        self.base_unit_types.add_unit_type(BaseUnitType("integer"))
        self.assertEqual(len(self.base_unit_types.get_unit_types_list()), 2)
        self.assertEqual(self.base_unit_types.get_unit_types_list()[1].name, "integer")

    def test_remove_unit_type(self):
        self.base_unit_types.remove_unit_type(BaseUnitType("string"))
        self.assertEqual(len(self.base_unit_types.get_unit_types_list()), 0)

    def test_get_unit_type(self):
        self.base_unit_types.add_unit_type(BaseUnitType("integer"))
        self.assertEqual(self.base_unit_types.get_unit_type(1).name, "integer")

    def test_set_unit_type(self):
        self.base_unit_types.add_unit_type(BaseUnitType("integer"))
        self.base_unit_types.set_unit_type(1, BaseUnitType("float"))
        self.assertEqual(self.base_unit_types.get_unit_type(1).name, "float")

    def test_get_unit_type_count(self):
        self.assertEqual(self.base_unit_types.get_unit_type_count(), 1)

    def test_verify_unit_type_is_allowed(self):
        self.base_unit_types.add_unit_type(BaseUnitType("integer"))
        self.assertTrue(self.base_unit_types.verify_unit_type_is_allowed(BaseUnitType("integer")))
        self.assertFalse(self.base_unit_types.verify_unit_type_is_allowed(BaseUnitType("boolean")))

    def test_to_json_string(self):
        expected_json = '{"_unit_types_list": [{"name": "string"}]}'
        self.assertEqual(self.base_unit_types.to_json_string(), expected_json)
