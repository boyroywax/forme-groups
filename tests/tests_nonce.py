import unittest

from src.groups import Nonce, UnitValue


class TestNonce(unittest.TestCase):
    def setUp(self):
        self.nonce = Nonce()

    def test_set_value_obj(self):
        # Set the value of the nonce
        value = UnitValue(42, "nonce")
        self.nonce.set_value_obj(value)

        # Verify that the value was set correctly
        self.assertEqual(self.nonce.get_value(), value)

    def test_set_value_obj_with_super_type(self):
        # Try to set the value of the nonce with a super type
        value = UnitValue(42, "length")
        with self.assertRaises(ValueError):
            self.nonce.set_value_obj(value)

    def test_create_and_set_value(self):
        # Create and set the value of the nonce
        self.nonce.create_and_set_value("abc123")

        # Verify that the value was set correctly
        self.assertEqual(self.nonce.get_value().get_value(), "abc123")

    def test_create_and_set_value_from_dict(self):
        # Create a dictionary representing the value of the nonce
        value_dict = {"value": "abc123", "type": "nonce"}

        # Create and set the value of the nonce from the dictionary
        self.nonce.create_and_set_value_from_dict(value_dict)

        # Verify that the value was set correctly
        self.assertEqual(self.nonce.get_value().to_dict(), value_dict)

    def test_create_and_set_value_from_json(self):
        # Create a JSON string representing the value of the nonce
        value_json = '{"value": "abc123", "type": "nonce"}'

        # Create and set the value of the nonce from the JSON string
        self.nonce.create_and_set_value_from_json(value_json)

        # Verify that the value was set correctly
        self.assertEqual(self.nonce.get_value().to_json(), value_json)

    def test_generate_unit(self):
        # Generate a nonce
        value = UnitValue(42, "nonce")
        type_ = UnitType("nonce")
        nonce = Nonce.generate_unit(value, type_)

        # Verify that the nonce was generated correctly
        self.assertEqual(nonce.get_value(), value)
        self.assertEqual(nonce.get_type(), type_)
