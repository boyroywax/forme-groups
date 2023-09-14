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
        print(self.group.group_units)

    def test_create_group(self):
        self.assertIsInstance(self.group, Group)

    def test_get_all_group_units(self):
        group_units = self.group.get_all_group_units()
        self.assertIsInstance(group_units, list)

    def test_get_group_unit_by_nonce(self):
        self.group.clear_group_units()
        nonce = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)])
        group_unit = self.group.new_group_unit(nonce=nonce)
        found_group_unit = self.group.get_group_unit_by_nonce(nonce)
        self.assertEqual(group_unit, found_group_unit)

    def test_get_nonce_tiers(self):
        self.group.clear_group_units()
        nonce1 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)])
        nonce2 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1), self.unit_generator.create_unit(alias="int", value=2)])
        self.group.new_group_unit(nonce=nonce1)
        self.group.new_group_unit(nonce=nonce2)
        nonce_tiers = self.group.get_nonce_tiers()
        self.assertEqual(nonce_tiers, 3)

    def test_get_highest_nonce_by_tier(self):
        self.group.clear_group_units()
        nonce1 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)])
        nonce2 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0)])
        self.group.new_group_unit(nonce=nonce1)
        self.group.new_group_unit(nonce=nonce2)
        highest_nonce_by_tier = self.group.get_highest_nonce_by_tier()
        self.assertEqual(highest_nonce_by_tier, nonce2)

    def test_get_highest_nonce_by_tier_with_tier(self):
        self.group.clear_group_units()
        nonce1 = self.group._group_unit_generator.create_nonce(nonce=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)])
        nonce2 = self.group._group_unit_generator.create_nonce(nonce=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0)])
        self.group.new_group_unit(nonce=nonce1)
        self.group.new_group_unit(nonce=nonce2)
        highest_nonce_by_tier = self.group.get_highest_nonce_by_tier(tier=2)
        self.assertEqual(highest_nonce_by_tier, nonce1)

    def test_get_highest_nonce_by_tier_with_tier_out_of_range(self):
        self.group.clear_group_units()
        nonce1 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)])
        nonce2 = Nonce(units=[self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0)])
        self.group.new_group_unit(nonce=nonce1)
        self.group.new_group_unit(nonce=nonce2)
        with self.assertRaises(ValueError):
            self.group.get_highest_nonce_by_tier(tier=4)

    def test_get_highest_nonce_by_tier_with_tier_negative(self):
        self.group.clear_group_units()
        nonce1 = self.group._group_unit_generator.create_nonce(nonce=(self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)))
        nonce2 = self.group._group_unit_generator.create_nonce(nonce=(self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0)))
        owners = self.group._group_unit_generator.create_ownership()
        creds = self.group._group_unit_generator.create_credentials()
        data = self.group._group_unit_generator.create_data()
        self.group.new_group_unit(nonce=nonce1, ownership=owners, credentials=creds, data=data)
        self.group.new_group_unit(nonce=nonce2, ownership=owners, credentials=creds, data=data)
        with self.assertRaises(ValueError):
            self.group.get_highest_nonce_by_tier(tier=-1)

    def test_get_highest_nonce_by_tier_with_tier_zero(self):
        self.group.clear_group_units()
        nonce1 = self.group._group_unit_generator.create_nonce(nonce=(self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=1)))
        nonce2 = self.group._group_unit_generator.create_nonce(nonce=(self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0), self.unit_generator.create_unit(alias="int", value=0)))
        owners = self.group._group_unit_generator.create_ownership()
        creds = self.group._group_unit_generator.create_credentials()
        data = self.group._group_unit_generator.create_data()
        self.group.new_group_unit(nonce=nonce1, ownership=owners, credentials=creds, data=data)
        self.group.new_group_unit(nonce=nonce2, ownership=owners, credentials=creds, data=data)
        with self.assertRaises(ValueError):
            self.group.get_highest_nonce_by_tier(tier=0)

    def test_create_defualt_group_unit(self):
        self.group.clear_group_units()
        self.group.create_group_unit()
        print(self.group.group_units)
        self.assertIsInstance(self.group.get_all_group_units()[0], GroupUnit)

    def test_group_unit_is_schema(self):
        self.group.clear_group_units()
        print(self.group.group_units)
        schema_unit: Unit = self.group._group_unit_generator.unit_generator.create_unit(alias="dict", value={"Schema": {"test": "test"}})
        print(schema_unit)
        schema_data: Data = self.group._group_unit_generator.create_data(data=(schema_unit,))
        print(schema_data)
        new_unit = self.group.create_group_unit(data=schema_data)
        print(self.group.group_units)
