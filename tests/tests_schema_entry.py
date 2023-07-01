import unittest
from src.groups.base.super.schema import SchemaEntry


class TestSchemaEntry(unittest.TestCase):
    def test_init_with_valid_args(self):
        entry = SchemaEntry(
            level=0,
            schema={"key": ["value"]},
            types={"key": ["int"]},
            functions={},
            overrides={}
        )
        self.assertEqual(entry.level, 0)
        self.assertEqual(entry.schema, {"key": ["value"]})
        self.assertEqual(entry.types, {"key": ["int"]})
        self.assertEqual(entry.functions, {})
        self.assertEqual(entry.overrides, {})

    def test_init_with_invalid_level_raises_error(self):
        with self.assertRaises(ValueError):
            SchemaEntry(
                level=-1,
                schema={"key": ["value"]},
                types={"key": ["int"]},
                functions={},
                overrides={}
            )

    def test_init_with_invalid_schema_raises_error(self):
        with self.assertRaises(TypeError):
            SchemaEntry(
                level=0,
                schema="invalid",
                types={"key": ["int"]},
                functions={},
                overrides={}
            )

    def test_validate_level_with_none_level_raises_error(self):
        entry = SchemaEntry(
            level=0,
            schema={"key": ["value"]},
            types={"key": ["int"]},
            functions={},
            overrides={}
        )
        with self.assertRaises(TypeError):
            entry.validate_level(None)

    def test_validate_level_with_invalid_level_type_raises_error(self):
        entry = SchemaEntry(
            level=0,
            schema={"key": ["value"]},
            types={"key": ["int"]},
            functions={},
            overrides={}
        )
        with self.assertRaises(TypeError):
            entry.validate_level("invalid")

    def test_validate_level_with_negative_level_raises_error(self):
        entry = SchemaEntry(
            level=0,
            schema={"key": ["value"]},
            types={"key": ["int"]},
            functions={},
            overrides={}
        )
        with self.assertRaises(ValueError):
            entry.validate_level(-1)

    def test_validate_schema_with_none_schema_raises_error(self):
        entry = SchemaEntry(
            level=0,
            schema={"key": ["value"]},
            types={"key": ["int"]},
            functions={},
            overrides={}
        )
        with self.assertRaises(TypeError):
            entry.validate_schema(None)

    def test_match_schema_and_types_with_matching_schema_and_types_returns_true(self):
        entry = SchemaEntry(
            level=0,
            schema={"key": ["value"]},
            types={"key": ["int"]},
            functions={},
            overrides={}
        )
        self.assertTrue(entry.match_schema_and_types({"key": "value"}, {"key": "int"}))

    def test_match_schema_and_types_with_mismatched_schema_returns_false(self):
        entry = SchemaEntry(
            level=0,
            schema={"key": ["value"]},
            types={"key": ["int"]},
            functions={},
            overrides={}
        )
        self.assertFalse(entry.match_schema_and_types({"other_key": "value"}, {"key": "int"}))

    def test_match_schema_and_types_with_mismatched_types_returns_false(self):
        entry = SchemaEntry(
            level=0,
            schema={"key": ["str"]},
            types={"key": [1234]},
            functions={},
            overrides={}
        )
        self.assertFalse(entry.match_schema_and_types({"key": "value"}, {"key1": "value1" }))

    def test_match_schema_and_types_with_empty_schema_and_types_returns_true(self):
        entry = SchemaEntry(
            level=0,
            schema={"key": ["value"]},
            types={"key": ["int"]},
            functions={},
            overrides={}
        )
        self.assertTrue(entry.match_schema_and_types(entry.schema, entry.types))

    def test_match_schema_and_types_with_empty_schema_and_nonempty_types_raises_error(self):
        with self.assertRaises(ValueError):
            entry = SchemaEntry(
                level=0,
                schema={},
                types={},
                functions={},
                overrides={}
            )

    def test_match_schema_and_types_with_nonempty_schema_and_empty_types_returns_false(self):
        entry = SchemaEntry(
            level=0,
            schema={"key": ["value"]},
            types={"key": ["int"]},
            functions={},
            overrides={}
        )
        self.assertFalse(entry.match_schema_and_types({"key": "value"}, {}))