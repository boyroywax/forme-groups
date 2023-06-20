import unittest
from groups.modules.nonce_types import NonceTypes

class TestNonceTypes(unittest.TestCase):
    def setUp(self):
        self.nonce_types = NonceTypes()

    def test_check_nonce_unit_type(self):
        # Test string
        self.assertEqual(self.nonce_types.check_nonce_unit_type('test'), 'string')

        # Test integer
        self.assertEqual(self.nonce_types.check_nonce_unit_type(123), 'integer')

        # Test float
        self.assertEqual(self.nonce_types.check_nonce_unit_type(3.14), 'float')

        # Test boolean
        self.assertEqual(self.nonce_types.check_nonce_unit_type(True), 'boolean')

        # Test list
        self.assertEqual(self.nonce_types.check_nonce_unit_type([1, 2, 3]), 'list')

        # Test tuple
        self.assertEqual(self.nonce_types.check_nonce_unit_type((1, 2, 3)), 'tuple')

        # Test dictionary
        self.assertEqual(self.nonce_types.check_nonce_unit_type({'a': 1, 'b': 2}), 'dictionary')

        # Test unknown type
        self.assertEqual(self.nonce_types.check_nonce_unit_type(None), "unknown")

    def test_set_active_nonce_type(self):
        # Test valid nonce type
        self.nonce_types.set_active_nonce_type('string')
        self.assertEqual(self.nonce_types.get_active_nonce_type(), 'string')

        # Test invalid nonce type
        with self.assertRaises(Exception):
            self.nonce_types.set_active_nonce_type('invalid')

        # Test unknown nonce type
        with self.assertRaises(Exception):
            self.nonce_types.set_active_nonce_type('unknown')

    def test_get_active_nonce_type(self):
        # Test active nonce type
        self.nonce_types.set_active_nonce_type('string')
        self.assertEqual(self.nonce_types.get_active_nonce_type(), 'string')

        # Test no active nonce type
        with self.assertRaises(Exception):
            self.nonce_types.set_active_nonce_type(None)

    def test_json(self):
        # Test JSON serialization
        expected_json = {"active_nonce_type": None}
        self.assertEqual(self.nonce_types.__json__(), expected_json)

    def test_str(self):
        # Test string representation
        self.assertEqual(str(self.nonce_types), 'None')

    def test_repr(self):
        # Test string representation
        self.assertEqual(repr(self.nonce_types), 'None')

    def test_eq(self):
        # Test equality
        nonce_types_1 = NonceTypes()
        nonce_types_2 = NonceTypes()
        self.assertEqual(nonce_types_1, nonce_types_2)
