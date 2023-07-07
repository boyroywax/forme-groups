import unittest

from src.groups.value import Value


class TestValue(unittest.TestCase):
    def setUp(self):
        self.value = Value(42)

    def test_value_deletion(self):
        self.value.value = None
        self.assertIsNone(self.value.value)

    def test_value_getter(self):
        self.assertEqual(self.value.value, 42)

    def test_check_empty(self):
        self.assertFalse(self.value.check_empty())
        empty_value = Value("")
        self.assertTrue(empty_value.check_empty())

    def test_check_none(self):
        self.assertFalse(self.value.check_none())
        none_value = Value(None)
        self.assertTrue(none_value.check_none())

    def test_freeze(self):
        self.assertFalse(self.value.frozen)
        self.value.freeze()
        self.assertTrue(self.value.frozen)
        with self.assertRaises(Exception):
            self.value.value = 84