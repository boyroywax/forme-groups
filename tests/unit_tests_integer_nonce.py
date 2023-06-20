import unittest
from groups.modules.nonce_unit import NonceUnit
from groups.modules.nonce_types import NonceTypes
from groups.modules.integer_nonce import IntegerNonce


class TestIntegerNonce(unittest.TestCase):
    def setUp(self):
        self.nonce_value = [
            NonceUnit(1234, NonceTypes.INTEGER_NONCE[0]),
            NonceUnit(5678, NonceTypes.INTEGER_NONCE[0]),
            NonceUnit(91011, NonceTypes.INTEGER_NONCE[0])
        ]
        self.integer_nonce = IntegerNonce(self.nonce_value, 0)

    def test_get_nonce_type(self):
        self.assertEqual(self.integer_nonce.get_nonce_type(), NonceTypes.INTEGER_NONCE)

    def test_copy(self):
        copied_nonce = self.integer_nonce.__copy__()
        self.assertEqual(copied_nonce.get_nonce_units(), self.nonce_value)

    def test_invalid_nonce_unit(self):
        with self.assertRaises(Exception):
            invalid_nonce_value = [
                NonceUnit(1234, NonceTypes.INTEGER_NONCE[0]),
                NonceUnit("5678", NonceTypes.HEX_NONCE[0]),
                NonceUnit(91011, NonceTypes.INTEGER_NONCE[0])
            ]
            IntegerNonce(invalid_nonce_value)

    def test_get_active_nonce_unit(self):
        self.assertEqual(self.integer_nonce.get_active_nonce_unit(), self.nonce_value[0])

    def test_get_active_nonce_unit_index(self):
        self.assertEqual(self.integer_nonce.get_active_nonce_unit_index(), 0)

    def test_get_active_nonce_unit_value(self):
        self.assertEqual(self.integer_nonce.get_active_nonce_unit_value(), 1234)

    def test_get_active_nonce_unit_type(self):
        self.assertEqual(self.integer_nonce.get_active_nonce_unit_type(), NonceTypes.INTEGER_NONCE[0])

    def test_next_nonce_unit(self):
        self.integer_nonce.next_nonce_unit()
        self.assertEqual(self.integer_nonce.get_active_nonce_unit().__json__(), self.nonce_value[1].__json__())

    def test_previous_nonce_unit(self):
        self.setUp()
        self.integer_nonce.next_nonce_unit()
        self.integer_nonce.previous_nonce_unit()
        self.assertEqual(self.integer_nonce.get_active_nonce_unit().__json__(), self.nonce_value[0].__json__())

    def test_increment_active_nonce_unit(self):
        self.integer_nonce.increment_active_nonce_unit()
        self.assertEqual(self.integer_nonce.get_active_nonce_unit_value(), 1235)

    def test_decrement_active_nonce_unit(self):
        self.integer_nonce.decrement_active_nonce_unit()
        self.assertEqual(self.integer_nonce.get_active_nonce_unit_value(), 1233)

    def test_set_active_nonce_unit(self):
        self.integer_nonce.set_active_nonce_unit(1)
        self.assertEqual(self.integer_nonce.get_active_nonce_unit(), self.nonce_value[1])

    def test_set_active_nonce_unit_out_of_range(self):
        with self.assertRaises(Exception):
            self.integer_nonce.set_active_nonce_unit(3)

    def test_set_active_nonce_unit_negative_index(self):
        with self.assertRaises(Exception):
            self.integer_nonce.set_active_nonce_unit(-1)