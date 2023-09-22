import unittest
import sys

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")
from src.groups.unit_type_pool import UnitTypePool

class TestUnitTypePool(unittest.TestCase):

    def setUp(self):
        self.unit_type_pool = UnitTypePool()
        self.unit_type_pool.set_types_from_json()

    def test_create_unit_type_pool(self):
        self.assertIsInstance(self.unit_type_pool, UnitTypePool)

    def test_unit_type_pool_has_unit_types(self):
        self.assertGreater(len(self.unit_type_pool.items), 0)