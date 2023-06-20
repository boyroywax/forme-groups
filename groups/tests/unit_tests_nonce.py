import unittest
from groups.modules.nonce import Nonce
from groups.modules.nonce_unit import NonceUnit


class TestNonce(unittest.TestCase):
    def setUp(self):
        self.nonce_list = [
            NonceUnit("0x1234", "hexadecimal"),
            NonceUnit("0d5678", "decimal"),
            NonceUnit('0b1010', "binary"),
        ]
        self.nonce = Nonce(self.nonce_list)

    def test_get_nonce_units(self):
        self.assertEqual(self.nonce.get_nonce_units(), self.nonce_list)

    def test_get_nonce_unit(self):
        self.assertEqual(self.nonce.get_nonce_unit(0), self.nonce_list[0])

    def test_get_nonce_unit_value(self):
        self.assertEqual(self.nonce.get_nonce_unit_value(0), "0x1234")

    def test_get_nonce_unit_type(self):
        self.assertEqual(self.nonce.get_nonce_unit_type(0), "hexadecimal")

    def test_set_nonce_unit(self):
        new_nonce_unit = NonceUnit("0d5678", "decimal")
        self.nonce.set_nonce_unit(0, new_nonce_unit)
        self.assertEqual(self.nonce.get_nonce_unit(0), new_nonce_unit)

    def test_add_nonce_unit(self):
        new_nonce_unit = NonceUnit("0b1100", "binary")
        self.nonce.add_nonce_unit(new_nonce_unit)
        self.assertEqual(self.nonce.get_nonce_unit(3), new_nonce_unit)

    def test_remove_nonce_unit(self):
        self.nonce.remove_nonce_unit(1)
        self.assertEqual(len(self.nonce.get_nonce_units()), 2)
        self.assertEqual(self.nonce.get_nonce_unit(1).get_nonce_unit_value(), "0b1010")

    def test_str(self):
        expected_output = "0x1234.0d5678.0b1010"
        self.assertEqual(str(self.nonce.__str__()), expected_output)

    def test_json(self):
        expected_output = {
            0: {"nonce_unit_value": "0x1234", "nonce_unit_type": "hexadecimal"},
            1: {"nonce_unit_value": "0d5678", "nonce_unit_type": "decimal"},
            2: {"nonce_unit_value": "0b1010", "nonce_unit_type": "binary"}
        }
        self.assertEqual(self.nonce.__json__(), expected_output)