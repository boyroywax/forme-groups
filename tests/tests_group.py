import unittest
import sys

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")

from src.groups.unit import UnitTypeRef, UnitTypeFunction, UnitType, UnitTypePool, Unit, UnitGenerator
from src.groups.group import GroupUnit, GroupUnitGenerator, Group


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

    def test_group_unit_generator_create_group_unit(self):
        self.group_unit_generator.unit_generator.unit_type_pool.freeze_pool()
        properties = tuple(self.group_unit_generator.unit_generator.create_unit(alias="str") for _ in range(4))
        group_unit = self.group_unit_generator.create_group_unit(nonce=properties[0], owners=properties[1], credentials=properties[2], data=properties[3])
        print(group_unit)
        self.assertIsInstance(group_unit, GroupUnit)


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.unit_type_ref = UnitTypeRef(alias="test_alias")
        self.unit_type_pool = UnitTypePool()
        self.unit_type_pool.add_unit_type(UnitType(aliases=[self.unit_type_ref]))
        self.unit_generator = UnitGenerator(unit_type_pool=self.unit_type_pool)
        self.group_unit_generator = GroupUnitGenerator(unit_generator=self.unit_generator)
        self.group = Group(generator=self.group_unit_generator)

    def test_create_group(self):
        self.assertIsInstance(self.group, Group)

    def test_create_group_with_default_generator(self):
        group = Group()
        self.assertIsInstance(group, Group)

    def test_get_unit_by_nonce(self):
        nonce = (Unit(value="test_value", type_ref="test_alias"),)
        group_unit = GroupUnit(nonce=nonce, owners=(), credentials=(), data=())
        self.group.units[nonce] = group_unit
        self.assertEqual(self.group.get_unit_by_nonce(nonce), group_unit)

    def test_get_unit_by_nonce_returns_none_if_not_found(self):
        nonce = (Unit(value="test_value", type_ref="test_alias"),)
        self.assertIsNone(self.group.get_unit_by_nonce(nonce))

    def test_find_next_nonce_with_int_nonce(self):
        nonce = (Unit(value=1, type_ref="test_alias"),)
        expected_next_nonce = (Unit(value=1),)
        self.assertEqual(self.group.find_next_nonce(nonce), expected_next_nonce)

    def test_find_next_nonce_raises_error_with_unsupported_nonce_type(self):
        nonce = (Unit(value="test_value", type_ref="test_alias"),)
        with self.assertRaises(ValueError):
            self.group.find_next_nonce(nonce)
