import unittest
from src.groups.base.super.schema import SuperUnit

class TestSchemaSuperUnit(unittest.TestCase):
    def test_init_with_no_args(self):
        unit = SuperUnit()
        self.assertIsNone(unit.value)

    def test_init_with_value(self):
        unit = SuperUnit(value="test")
        self.assertEqual(unit.value, "test")

    def test_init_with_positional_arg(self):
        unit = SuperUnit("test")
        self.assertEqual(unit.value, "test")

    def test_init_with_dict_arg(self):
        unit = SuperUnit({"value": "test"})
        self.assertEqual(unit.value, "test")

    def test_init_with_random_true(self):
        unit = SuperUnit(random=True)
        self.assertIsNotNone(unit.value)

    def test_init_with_random_false(self):
        unit = SuperUnit(random=False)
        self.assertIsNone(unit.value)

    def test_init_with_random_and_value_raises_error(self):
        with self.assertRaises(ValueError):
            SuperUnit(random=True, value="test")

    def test_init_with_value_and_positional_arg_raises_error(self):
        with self.assertRaises(ValueError):
            SuperUnit("test", value="test")

    def test_has_type_returns_true_for_correct_type(self):
        unit = SuperUnit(value=1)
        self.assertTrue(unit.has_type(int))

    def test_has_type_returns_false_for_incorrect_type(self):
        unit = SuperUnit(value=1)
        self.assertFalse(unit.has_type(str))

    def test_force_type_converts_value_to_correct_type(self):
        unit = SuperUnit(value="1")
        unit.force_type(int)
        self.assertEqual(unit.value, 1)

    def test_force_type_does_not_convert_value_if_already_correct_type(self):
        unit = SuperUnit(value=1)
        unit.force_type(int)
        self.assertEqual(unit.value, 1)

    def test_random_value_returns_random_hex_string(self):
        value1 = SuperUnit.random_value()
        value2 = SuperUnit.random_value()
        self.assertIsInstance(value1, str)
        self.assertIsInstance(value2, str)
        self.assertNotEqual(value1, value2)

    def test_get_type_returns_name_of_value_type(self):
        unit = SuperUnit(value=1)
        self.assertEqual(unit.get_type(), "int")

    def test_from_dict_returns_unit_with_correct_value(self):
        unit_dict = {"value": "test"}
        unit = SuperUnit.from_dict(unit_dict)
        self.assertEqual(unit.value, "test")