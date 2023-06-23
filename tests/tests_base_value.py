import unittest
from src.groups.modules.__base import Value_


class Test_Value_(unittest.TestCase):
    def setUp(self):
        self._value = Value_()
        self._value.set_value("test")

    def test_get_value(self):
        self.assertEqual(self._value.get_value(), "test")

    def test_to_json_string(self):
        expected_json = '{"_value": "test"}'
        self.assertEqual(self._value.to_json_string(), expected_json)

    def test_from_json_string(self):
        json_string = '{"_value": "test"}'
        self._value.from_json_string(json_string)
        self.assertEqual(self._value.get_value(), "test")

    def test_str(self):
        self.assertEqual(str(self._value), "test")

    def test_repr(self):
        self.assertEqual(repr(self._value), "test")

    def test_eq(self):
        self.assertTrue(self._value == Value_("test"))
        self.assertFalse(self._value == Value_("other"))

    def test_ne(self):
        self.assertTrue(self._value != Value_("other"))
        self.assertFalse(self._value != Value_("test"))