import unittest
from src.groups.base._unit import Unit


class TestUnit(unittest.TestCase):
    def test_dataclass(self):
        # Test creating a Unit object with no arguments
        unit = Unit()
        self.assertIsNone(unit.value)

        # Test creating a Unit object with a value argument
        unit = Unit("test")
        self.assertEqual(unit.value, "test")

        # Test creating a Unit object with a dictionary argument
        unit = Unit.from_dict({"value": "test"})
        self.assertEqual(unit.value, "test")

        # Test creating a Unit object with a dictionary argument that has extra keys
        unit = Unit.from_dict({"value": "test", "extra_key": "extra_value"})
        self.assertEqual(unit.value, "test")

        # Test creating a Unit object with a dictionary argument that has missing keys
        with self.assertRaises(TypeError):
            unit = Unit.from_dict({})

        # Test creating a Unit object with a dictionary argument that has an invalid key
        with self.assertRaises(TypeError):
            unit = Unit.from_dict({"invalid_key": "test"})

        # Test creating a Unit object with a dictionary argument that has an integer value
        unit = Unit.from_dict({"value": 123})
        self.assertEqual(unit.value, 123)

        # Test creating a Unit object with a dictionary argument that has a float value
        unit = Unit.from_dict({"value": 123.456})
        self.assertEqual(unit.value, 123.456)

        # Test creating a Unit object with a dictionary argument that has a boolean value
        unit = Unit.from_dict({"value": True})
        self.assertEqual(unit.value, True)

        # Test creating a Unit object with a dictionary argument that has a list value
        unit = Unit.from_dict({"value": ["test"]})
        self.assertEqual(unit.value, ["test"])

        # Test creating a Unit object with a dictionary argument that has a dictionary value
        unit = Unit.from_dict({"value": {"test_key": "test_value"}})
        self.assertEqual(unit.value, {"test_key": "test_value"})

        # Test creating a Unit object with a dictionary argument that has a None value
        with self.assertRaises(TypeError):
            unit = Unit.from_dict({"value": None})

    def test_init(self):
        # Test creating a Unit object with no arguments
        unit = Unit()
        self.assertIsNone(unit.value)

        # Test creating a Unit object with a boolean value argument
        unit = Unit(True)
        self.assertEqual(unit.value, True)

        # Test creating a Unit object with an integer value argument
        unit = Unit(123)
        self.assertEqual(unit.value, 123)

        # Test creating a Unit object with a float value argument
        unit = Unit(3.14)
        self.assertEqual(unit.value, 3.14)

        # Test creating a Unit object with a string value argument
        unit = Unit("test")
        self.assertEqual(unit.value, "test")

        # Test creating a Unit object with a list value argument
        unit = Unit(["test"])
        self.assertEqual(unit.value, ["test"])

        # Test creating a Unit object with a dictionary value argument
        unit = Unit({"test_key": "test_value"})
        self.assertEqual(unit.value, {"test_key": "test_value"})

    def test_get_type(self):
        # Test getting the type of a Unit object
        unit = Unit()
        self.assertEqual(unit.get_type(), "Unit")

    def test_set_value(self):
        # Test setting the value of a Unit object
        unit = Unit()
        unit.set_value("test")
        self.assertEqual(unit.value, "test")

    def test_from_dict(self):
        # Test creating a Unit object from a dictionary with a value key
        unit_dict = {"value": "test"}
        unit = Unit.from_dict(unit_dict)
        self.assertEqual(unit.value, "test")

        # Test creating a Unit object from a dictionary with no value key
        unit_dict = {}
        with self.assertRaises(TypeError):
            unit = Unit.from_dict(unit_dict)

        # Test creating a Unit object from a dictionary with a None value key
        unit_dict = {"value": None}
        with self.assertRaises(TypeError):
            unit = Unit.from_dict(unit_dict)

        # Test creating a Unit object from a dictionary with an empty string value key
        unit_dict = {"value": ""}
        with self.assertRaises(TypeError):
            unit = Unit.from_dict(unit_dict)

        # Test creating a Unit object from a dictionary with an empty dictionary value key
        unit_dict = {"value": {}}
        with self.assertRaises(TypeError):
            unit = Unit.from_dict(unit_dict)

        # Test creating a Unit object from a dictionary with an empty list value key
        unit_dict = {"value": []}
        with self.assertRaises(TypeError):
            unit = Unit.from_dict(unit_dict)

    def test_to_dict(self):
        # Test converting a Unit object to a dictionary
        unit = Unit("test")
        unit_dict = unit.to_dict()
        self.assertEqual(unit_dict, {"value": "test"})

    def test_str(self):
        # Test getting the string representation of a Unit object
        unit = Unit("test")
        self.assertEqual(str(unit), "Unit(value='test')")

    def test_repr(self):
        # Test getting the string representation of a Unit object
        unit = Unit("test")
        self.assertEqual(repr(unit), "Unit(value='test')")

    def test_slots(self):
        # Test setting a valid attribute
        unit = Unit("test")
        unit.value = "new_test"
        self.assertEqual(unit.value, "new_test")

        # Test setting an invalid attribute
        with self.assertRaises(AttributeError):
            unit.invalid_attribute = "test"

    def test_post_init_random_value_generation(self):
        # Test creating multiple Unit objects with random values
        unit_values = set()
        for i in range(100):
            unit = Unit(_random_value=True)
            unit_values.add(unit.value)
        self.assertEqual(len(unit_values), 100)

    def test_empty_value(self):
        # Test creating a Unit object with an empty value
        with self.assertRaises(TypeError):
            unit = Unit("")

    def test_invalid_value(self):
        # Test creating a Unit object with an invalid value
        self.assertIsNotNone(Unit("test"))