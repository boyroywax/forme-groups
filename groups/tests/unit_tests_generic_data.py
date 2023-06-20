import unittest
from datetime import datetime

from groups.modules.generic_data import GenericData


class TestGenericData(unittest.TestCase):
    def setUp(self):
        self.generic_data = GenericData()

    def test_get_data(self):
        self.assertEqual(self.generic_data.get_data(), {})

    def test_set_data(self):
        data = {"key": "value"}
        self.generic_data.set_data(data)
        self.assertEqual(self.generic_data.get_data(), data)

    def test_get_last_modified(self):
        self.assertIsInstance(self.generic_data.get_last_modified(), datetime)

    def test_set_last_modified(self):
        last_modified = datetime.now()
        self.generic_data.set_last_modified(last_modified)
        self.assertEqual(self.generic_data.get_last_modified(), last_modified)

    def test_update_data(self):
        data = {"key": "value"}
        self.generic_data.update_data(data)
        self.assertEqual(self.generic_data.get_data(), data)

    def test_update_last_modified(self):
        last_modified = self.generic_data.get_last_modified()
        self.generic_data.update_last_modified()
        self.assertNotEqual(self.generic_data.get_last_modified(), last_modified)

    def test_clear_data(self):
        self.generic_data.clear_data()
        self.assertEqual(self.generic_data.get_data(), {})

    def test_clear_last_modified(self):
        last_modified = self.generic_data.last_modified
        self.generic_data.clear_last_modified()
        self.assertNotEqual(self.generic_data.get_last_modified(), last_modified)

