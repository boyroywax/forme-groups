import unittest
from groups.modules.nonce_unit import NonceUnit
from groups.modules.nonce_types import NonceTypes


class TestNonceUnit(unittest.TestCase):
    def setUp(self):
        self.nonce_unit = NonceUnit('test', 'string')

    def test_get_nonce_unit_value(self):
        # Test get nonce unit value
        self.assertEqual(self.nonce_unit.get_nonce_unit_value(), 'test')

    def test_get_nonce_unit_type(self):
        # Test get nonce unit type
        self.assertEqual(self.nonce_unit.get_nonce_unit_type(), 'string')

    def test_set_nonce_unit(self):
        # Test set nonce unit
        self.nonce_unit.set_nonce_unit('new_test')
        self.assertEqual(self.nonce_unit.get_nonce_unit_value(), 'new_test')

    def test_set_nonce_unit_type(self):
        # Test set nonce unit type
        self.nonce_unit.set_nonce_unit_type(NonceTypes('integer'))
        self.assertEqual(self.nonce_unit.get_nonce_unit_type(), 'integer')

    def test_invalid_nonce_unit_type(self):
        # Test invalid nonce unit type
        with self.assertRaises(Exception):
            NonceUnit('test', 'invalid')

    def test_unsupported_nonce_unit_type(self):
        # Test unsupported nonce unit type
        with self.assertRaises(Exception):
            NonceUnit('test', 'unknown')
