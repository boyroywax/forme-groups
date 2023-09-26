import unittest
import sys
from attrs import exceptions as excs

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")
from src.groups.unit_type_pool import UnitTypePool


class TestUnitTypePool(unittest.TestCase):

    def setUp(self):
        self.unit_type_pool = UnitTypePool()
        self.unit_type_pool.set_system_types_from_json()

    def test_create_unit_type_pool(self):
        self.assertIsInstance(self.unit_type_pool, UnitTypePool)

    def test_unit_type_pool_has_unit_types(self):
        self.assertGreater(len(self.unit_type_pool.items), 0)

    def test_unit_type_pool_has_unit_types_with_aliases(self):
        self.assertGreater(len(self.unit_type_pool.get_type_aliases()), 0)

    def test_unit_type_pool_contains_alias(self):
        self.assertTrue(self.unit_type_pool.contains_alias("dict"))
        self.assertFalse(self.unit_type_pool.contains_alias("not_an_alias"))

    def test_unit_type_pool_get_type_from_alias(self):
        self.assertIsNotNone(self.unit_type_pool.get_type_from_alias("dict"))
        self.assertIsNone(self.unit_type_pool.get_type_from_alias("not_an_alias"))

    def test_unit_type_pool_add_unit_type_from_dict(self):
        self.unit_type_pool.add_unit_type_from_dict({
            "aliases": ["test_alias"],
            "base_type": ["test_base_type"],
            "prefix": "test_prefix",
            "suffix": "test_suffix",
            "separator": "test_separator",
            "sys_function": {
                "object": "str.upper",
                "args": ["test_arg1", "test_arg2"]
            }
        })
        self.assertTrue(self.unit_type_pool.contains_alias("test_alias"))

    def test_unit_type_pool_add_unit_type_from_dict_with_no_aliases(self):
        with self.assertRaises(ValueError):
            self.unit_type_pool.add_unit_type_from_dict({
                "aliases": [],
                "base_type": ["test_base_type"],
                "prefix": "test_prefix",
                "suffix": "test_suffix",
                "separator": "test_separator",
                "sys_function": {
                    "object": "str.upper",
                    "args": ["test_arg1", "test_arg2"]
                }
            })

    def test_unit_type_pool_hash_tree(self):
        self.unit_type_pool.freeze()
        self.assertEqual(self.unit_type_pool.hash_tree().root(), "899b00b441418db6c599aa3f59ef96319c37095a857750f216a27c398e5ac4aa")

    def test_unit_type_pool_hash_tree_with_test_value(self):
        self.unit_type_pool.add_unit_type_from_dict({
            "aliases": ["test_alias"],
            "base_type": ["test_base_type"],
            "prefix": "test_prefix",
            "suffix": "test_suffix",
            "separator": "test_separator",
            "sys_function": {
                "object": "str.upper",
                "args": ["test_arg1", "test_arg2"]
            }
        })
        self.assertTrue(self.unit_type_pool.contains_alias("test_alias"))
        self.unit_type_pool.freeze()
        self.assertNotEqual(self.unit_type_pool.hash_tree().root(), "899b00b441418db6c599aa3f59ef96319c37095a857750f216a27c398e5ac4aa")

    def test_unit_type_pool_hash_tree_is_frozen(self):
        self.unit_type_pool.freeze()
        with self.assertRaises(ValueError):
            self.unit_type_pool.add_unit_type_from_dict({
                "aliases": ["test_alias"],
                "base_type": ["test_base_type"],
                "prefix": "test_prefix",
                "suffix": "test_suffix",
                "separator": "test_separator",
                "sys_function": {
                    "object": "str.upper",
                    "args": ["test_arg1", "test_arg2"]
                }
            })