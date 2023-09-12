import unittest
import sys
from unittest.mock import MagicMock

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")

from src.groups.unit import UnitTypeRef, UnitTypeFunction, UnitType, UnitTypePool, Unit, UnitGenerator
from src.groups.group import GroupUnit, GroupUnitGenerator, Nonce, Ownership, Credentials, Data, Group


class TestGroupUnit(unittest.TestCase):
    def setUp(self):
        self.unit_type_ref = UnitTypeRef(alias="int")
        self.unit_generator = UnitGenerator(freeze=True)
        self.group_unit_generator = GroupUnitGenerator(unit_generator=self.unit_generator)

    def test_create_group_unit_generator(self):
        self.assertIsInstance(self.group_unit_generator, GroupUnitGenerator)

    def test_group_unit_generator_has_unit_generator(self):
        self.assertEqual(self.group_unit_generator.unit_generator, self.unit_generator)

    def test_create_nonce(self):
        nonce = self.group_unit_generator.create_nonce()
        self.assertIsInstance(nonce, Nonce)

    def test_create_nonce_with_nonce(self):
        nonce = self.group_unit_generator.create_nonce(nonce=(self.unit_generator.create_unit(alias="int", value=2),))
        self.assertIsInstance(nonce, Nonce)
        self.assertEqual(nonce.units[0].value, 2)

    def test_create_nonce_with_invalid_nonce(self):
        with self.assertRaises(ValueError):
            self.group_unit_generator.create_nonce(nonce=(self.unit_generator.create_unit(alias="str", value="test"),))

    def test_create_nonce_with_invalid_nonce_type(self):
        with self.assertRaises(ValueError):
            self.group_unit_generator.create_nonce(nonce=(self.unit_generator.create_unit(alias="float", value=2.0),))

    def test_create_ownership(self):
        ownership = self.group_unit_generator.create_ownership()
        self.assertIsInstance(ownership, Ownership)


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.unit_type_ref = UnitTypeRef(alias="int")
        self.unit_generator = UnitGenerator(freeze=True)
        self.group_unit_generator = GroupUnitGenerator(unit_generator=self.unit_generator)
        self.group = Group(group_unit_generator=self.group_unit_generator)

    def test_create_group(self):
        self.assertIsInstance(self.group, Group)

    def test_get_all_group_units(self):
        group_units = self.group.get_all_group_units()
        self.assertIsInstance(group_units, list)

    def test_get_group_unit_by_nonce(self):
        nonce = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)])
        group_unit = self.group.new_group_unit(nonce=nonce)
        found_group_unit = self.group.get_group_unit_by_nonce(nonce)
        self.assertEqual(group_unit, found_group_unit)

    def test_get_nonce_tiers(self):
        nonce1 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)])
        nonce2 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1), self.unit_generator.create_unit(alias="int", value=2)])
        self.group.new_group_unit(nonce=nonce1)
        self.group.new_group_unit(nonce=nonce2)
        nonce_tiers = self.group.get_nonce_tiers()
        self.assertEqual(nonce_tiers, 3)

    def test_get_highest_nonce_by_tier(self):
        nonce1 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)])
        nonce2 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0)])
        self.group.new_group_unit(nonce=nonce1)
        self.group.new_group_unit(nonce=nonce2)
        highest_nonce_by_tier = self.group.get_highest_nonce_by_tier()
        self.assertEqual(highest_nonce_by_tier, nonce2)

    def test_get_highest_nonce_by_tier_with_tier(self):
        nonce1 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)])
        nonce2 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0)])
        self.group.new_group_unit(nonce=nonce1)
        self.group.new_group_unit(nonce=nonce2)
        highest_nonce_by_tier = self.group.get_highest_nonce_by_tier(tier=2)
        self.assertEqual(highest_nonce_by_tier, nonce2)

    def test_get_highest_nonce_up_to_tier(self):
        nonce1 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)])
        nonce2 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0)])
        self.group.new_group_unit(nonce=nonce1)
        self.group.new_group_unit(nonce=nonce2)
        highest_nonce_by_tier = self.group.get_highest_nonce(tier=2)
        self.assertEqual(highest_nonce_by_tier, nonce1)