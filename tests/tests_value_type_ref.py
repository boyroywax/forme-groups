import unittest
from src.groups.value_type_ref import ValueTypeRef


class TestValueTypeRef(unittest.TestCase):
    def test_init(self):
        alias = 'int'
        value_type_ref = ValueTypeRef(alias)

        self.assertEqual(value_type_ref.alias, alias)

    def test_alias(self):
        alias = 'int'
        value_type_ref = ValueTypeRef(alias)

        new_alias = 'float'
        value_type_ref.alias = new_alias

        self.assertEqual(value_type_ref.alias, new_alias)

    def test_frozen(self):
        alias = 'int'
        value_type_ref = ValueTypeRef(alias)
        value_type_ref.freeze()

        with self.assertRaises(Exception):
            value_type_ref.alias = 'float'