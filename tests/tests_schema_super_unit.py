import unittest
from src.groups.base.super.schema import SuperUnit


class TestSchemaSuperUnit(unittest.TestCase):
    def test_init_with_no_args(self):
        unit = SuperUnit()
        self.assertIsNone(unit.value)

    def test_init_with_random_true(self):
        unit = SuperUnit(random=True)
        self.assertIsNotNone(unit.value)

    def test_init_with_random_false(self):
        unit = SuperUnit(random=False)
        self.assertIsNone(unit.value)

    def test_init_with_value(self):
        unit = SuperUnit(value="test")
        self.assertEqual(unit.value, "test")

    def test_init_with_positional_arg(self):
        unit = SuperUnit("test")
        self.assertEqual(unit.value, "test")

    def test_init_with_random_and_value_raises_error(self):
        with self.assertRaises(ValueError):
            SuperUnit(random=True, value="test")

    def test_init_with_value_and_positional_arg_raises_error(self):
        with self.assertRaises(ValueError):
            SuperUnit("test", value="test")

    def test_to_dict(self):
        unit = SuperUnit(value="test")
        self.assertEqual(unit.to_dict(), {"value": "test"})

    def test_from_dict(self):
        unit_dict = {"value": "test"}
        unit = SuperUnit.from_dict(unit_dict)
        self.assertEqual(unit.value, "test")