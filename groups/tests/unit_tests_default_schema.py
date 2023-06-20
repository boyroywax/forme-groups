import unittest
from groups.modules.default_schema import DefaultSchema


class TestDefaultSchema(unittest.TestCase):
    def setUp(self):
        self.default_schema = DefaultSchema(None)

    def test_get_title(self):
        self.assertEqual(self.default_schema.get_title(), self.default_schema.title)

    def test_set_title(self):
        self.default_schema.set_title("New Title")
        self.assertEqual(self.default_schema.get_title(), "New Title")

    def test_default_title(self):
        default_schema = DefaultSchema(None)
        self.assertIsNotNone(default_schema.get_title())

    def test_default_entries(self):
        default_schema = DefaultSchema(None)
        self.assertIsNotNone(default_schema.entries)
        self.assertIsNotNone(default_schema.entries.get("link"))
        self.assertIsNotNone(default_schema.entries.get("schema"))
