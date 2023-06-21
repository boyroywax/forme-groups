import unittest

from groups.modules.unit_type import UnitType


class TestUnitType(unittest.TestCase):
    def setUp(self):
        self.unit_type = UnitType()

    def test_check_for_type(self):
        self.assertTrue(self.unit_type.check_for_type("str"))
        self.assertFalse(self.unit_type.check_for_type("foo"))

    def test_get_unit_types(self):
        self.assertIsInstance(self.unit_type.get_unit_types(), dict)

    def test_get_unit_type(self):
        self.assertEqual(self.unit_type.get_unit_type(), "meter")

    def test_set_unit_type(self):
        self.unit_type.set_unit_type("second")
        self.assertEqual(self.unit_type.get_unit_type(), "second")

        with self.assertRaises(ValueError):
            self.unit_type.set_unit_type("foo")

    def test_to_json(self):
        self.assertIsInstance(self.unit_type.to_json(), dict)

    def test_from_json(self):
        json_data = '{"unit_type": "second"}'
        self.unit_type.from_json(json_data)
        self.assertEqual(self.unit_type.get_unit_type(), "second")
