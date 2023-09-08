import unittest
import sys

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")

from src.groups.group import GroupUnit, GroupUnitGenerator


class TestGroupUnit(unittest.TestCase):
    def setUp(self):
        self.group_unit = GroupUnit()

    def test_create_group_unit(self):
        self.assertIsInstance(self.group_unit, GroupUnit)

    def test_group_unit_has_nonce(self):
        self.assertIsNone(self.group_unit.nonce)

    def test_group_unit_has_owners(self):
        self.assertIsNone(self.group_unit.owners)

    def test_group_unit_has_credentials(self):
        self.assertIsNone(self.group_unit.credentials)

    def test_group_unit_has_data(self):
        self.assertIsNone(self.group_unit.data)


class TestGroupUnitGenerator(unittest.TestCase):
    def setUp(self):
        self.group_unit_generator = GroupUnitGenerator()

    def test_create_group_unit_generator(self):
        self.assertIsInstance(self.group_unit_generator, GroupUnitGenerator)

    def test_group_unit_generator_has_unit_generator(self):
        print(self.group_unit_generator.unit_generator)
        self.assertIsNotNone(self.group_unit_generator.unit_generator)

    def test_group_unit_generator_has_frozen_unit_type_pool(self):
        self.group_unit_generator.unit_generator.unit_type_pool.freeze_pool()
        self.assertTrue(self.group_unit_generator.unit_generator.check_frozen_pool())
