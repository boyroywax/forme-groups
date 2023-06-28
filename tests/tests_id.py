import unittest
from src.groups.base.type.id import Id


class TestId(unittest.TestCase):
    def test_init(self):
        # Test creating an Id object with no arguments
        id_obj = Id()
        self.assertIsNone(id_obj.value)

        # Test creating an Id object with a string value argument
        id_obj = Id("test")
        self.assertEqual(id_obj.value, "test")

        # Test creating an Id object with an integer value argument
        id_obj = Id(123)
        self.assertEqual(id_obj.value, 123)

        # Test creating an Id object with a float value argument
        id_obj = Id(3.14)
        self.assertEqual(id_obj.value, 3.14)

        # Test creating an Id object with a boolean value argument
        id_obj = Id(True)
        self.assertEqual(id_obj.value, True)

        # Test creating an Id object with a list value argument
        id_obj = Id(["test"])
        self.assertEqual(id_obj.value, ["test"])

        # Test creating an Id object with a dictionary value argument
        id_obj = Id({"test_key": "test_value"})
        self.assertEqual(id_obj.value, {"test_key": "test_value"})

    def test_set_value(self):
        # Test setting the value of an Id object
        id_obj = Id()
        id_obj.set_value("test")
        self.assertEqual(id_obj.value, "test")

    def test_from_dict(self):
        # Test creating an Id object from a dictionary with a value key
        id_dict = {"value": "test"}
        id_obj = Id.from_dict(id_dict)
        self.assertEqual(id_obj.value, "test")

        # Test creating an Id object from a dictionary with no value key
        id_dict = {}
        with self.assertRaises(TypeError):
            id_obj = Id.from_dict(id_dict)

        # Test creating an Id object from a dictionary with a None value key
        id_dict = {"value": None}
        with self.assertRaises(TypeError):
            id_obj = Id.from_dict(id_dict)

        # Test creating an Id object from a dictionary with an empty string value key
        id_dict = {"value": ""}
        with self.assertRaises(TypeError):
            id_obj = Id.from_dict(id_dict)

        # Test creating an Id object from a dictionary with an empty dictionary value key
        id_dict = {"value": {}}
        with self.assertRaises(TypeError):
            id_obj = Id.from_dict(id_dict)

        # Test creating an Id object from a dictionary with an empty list value key
        id_dict = {"value": []}
        with self.assertRaises(TypeError):
            id_obj = Id.from_dict(id_dict)

    def test_to_dict(self):
        # Test converting an Id object to a dictionary
        id_obj = Id("test")
        id_dict = id_obj.to_dict()
        self.assertEqual(id_dict, {"value": "test"})

    def test_str(self):
        # Test getting the string representation of an Id object
        id_obj = Id("test")
        self.assertEqual(str(id_obj), "Id(value='test')")

    def test_repr(self):
        # Test getting the string representation of an Id object
        id_obj = Id("test")
        self.assertEqual(repr(id_obj), "Id(value='test')")