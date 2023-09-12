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


# class TestGroupUnitGenerator(unittest.TestCase):
#     def setUp(self):
#         self.group_unit_generator = GroupUnitGenerator()

#     def test_create_group_unit_generator(self):
#         self.assertIsInstance(self.group_unit_generator, GroupUnitGenerator)

#     def test_group_unit_generator_has_unit_generator(self):
#         print(self.group_unit_generator.unit_generator)
#         self.assertIsNotNone(self.group_unit_generator.unit_generator)

#     def test_group_unit_generator_has_frozen_unit_type_pool(self):
#         self.group_unit_generator.unit_generator.unit_type_pool.freeze_pool()
#         self.assertTrue(self.group_unit_generator.unit_generator.check_frozen_pool())

#     def test_group_unit_generator_create_group_unit(self):
#         self.group_unit_generator.unit_generator.unit_type_pool.freeze_pool()
#         properties = tuple(self.group_unit_generator.unit_generator.create_unit(alias="str") for _ in range(4))
#         group_unit = self.group_unit_generator.create_group_unit(nonce=properties[0], owners=properties[1], credentials=properties[2], data=properties[3])
#         print(group_unit)
#         self.assertIsInstance(group_unit, GroupUnit)


# class TestGroup(unittest.TestCase):
#     def setUp(self):
#         self.unit_type_ref = UnitTypeRef(alias="test_alias")
#         self.unit_type_pool = UnitTypePool()
#         self.unit_type_pool.add_unit_type(UnitType(aliases=[self.unit_type_ref]))
#         self.unit_generator = UnitGenerator(unit_type_pool=self.unit_type_pool)
#         self.group_unit_generator = GroupUnitGenerator(unit_generator=self.unit_generator)
#         self.group = Group(generator=self.group_unit_generator)

#     def test_create_group(self):
#         self.assertIsInstance(self.group, Group)

#     def test_create_group_with_default_generator(self):
#         group = Group()
#         self.assertIsInstance(group, Group)

#     def test_get_unit_by_nonce(self):
#         nonce = (Unit(value=0, type_ref=UnitTypeRef(alias="int")),)
#         group_unit = GroupUnit(nonce=nonce, owners=(), credentials=(), data=())
#         self.group.units = [group_unit]
#         self.assertEqual(self.group.get_unit_by_nonce(nonce), group_unit)

#     def test_get_unit_by_nonce_returns_none_if_not_found(self):
#         nonce = (Unit(value=1, type_ref=UnitTypeRef(alias="int")),)
#         self.assertIsNone(self.group.get_unit_by_nonce(nonce))

#     def test_find_next_nonce_with_int_nonce(self):
#         nonce = (Unit(value=1, type_ref=UnitTypeRef(alias="int")),)
#         expected_next_nonce = (Unit(value=2, type_ref=UnitTypeRef(alias="int")),)
#         self.assertEqual(self.group.find_next_nonce(nonce), expected_next_nonce)

#     def test_find_next_nonce_raises_error_with_unsupported_nonce_type(self):
#         nonce = (Unit(value="string", type_ref=UnitTypeRef(alias="str")),)
#         with self.assertRaises(ValueError):
#             self.group.find_next_nonce(nonce)

#     def test_find_next_nonce_with_int_nonces(self):
#         nonce = (Unit(value=0, type_ref=UnitTypeRef(alias="int")), Unit(value=1, type_ref=UnitTypeRef(alias="int")))
#         expected_next_nonce = (Unit(value=0, type_ref=UnitTypeRef(alias="int")), Unit(value=2, type_ref=UnitTypeRef(alias="int")))
#         self.assertEqual(self.group.find_next_nonce(nonce), expected_next_nonce)

#     def test_set_active_nonce(self):
#         nonce = (Unit(value=0, type_ref=UnitTypeRef(alias="int")),)
#         self.group.set_active_nonce(nonce)
#         self.assertEqual(self.group.active_nonce, nonce)

#     def test_get_unit_by_active_nonce(self):
#         nonce = (Unit(value=0, type_ref=UnitTypeRef(alias="int")),)
#         group_unit = GroupUnit(nonce=nonce, owners=(), credentials=(), data=())
#         self.group.units = [group_unit]
#         self.group.set_active_nonce(nonce)
#         self.assertEqual(self.group.get_unit_by_active_nonce(), group_unit)

#     def test_get_unit_by_active_nonce_returns_none_if_not_found(self):
#         nonce = (Unit(value=0, type_ref=UnitTypeRef(alias="int")),)
#         unset_nonce = (Unit(value=1, type_ref=UnitTypeRef(alias="int")),)
#         self.group.set_active_nonce(nonce)
#         self.assertIsNone(self.group.get_unit_by_nonce(unset_nonce))

#     def test_find_next_active_nonce(self):
#         nonce = (Unit(value=0, type_ref=UnitTypeRef(alias="int")),)
#         expected_next_nonce = (Unit(value=1, type_ref=UnitTypeRef(alias="int")),)
#         self.group.set_active_nonce(nonce)
#         self.assertEqual(self.group.find_next_active_nonce(), expected_next_nonce)

#     def test_add_group_unit(self):
#         nonce = (Unit(value=0, type_ref=UnitTypeRef(alias="int")),)
#         group_unit = GroupUnit(nonce=nonce, owners=(), credentials=(), data=())
#         self.group.add_group_unit(group_unit)
#         self.assertEqual(self.group.units, [group_unit])

#     def test_add_group_unit_raises_error_if_nonce_already_exists(self):
#         nonce = (Unit(type_ref=UnitTypeRef(alias="int"), value=1),)
#         group_unit1 = GroupUnit(nonce=nonce, owners=(), credentials=(), data=())
#         group_unit2 = GroupUnit(nonce=nonce, owners=(), credentials=(), data=())
#         self.group.add_group_unit(group_unit1)
#         with self.assertRaises(ValueError):
#             self.group.add_group_unit(group_unit2)

#     def test_add_group_unit_raises_error_if_nonce_is_not_next(self):
#         self.group.clear_units()
#         nonce1 = (Unit(type_ref=UnitTypeRef(alias="int"), value=0),)
#         nonce2 = (Unit(type_ref=UnitTypeRef(alias="int"), value=2),)
#         group_unit1 = GroupUnit(nonce=nonce1, owners=(), credentials=(), data=())
#         group_unit2 = GroupUnit(nonce=nonce2, owners=(), credentials=(), data=())
#         self.group.add_group_unit(group_unit1)
#         with self.assertRaises(ValueError):
#             self.group.add_group_unit(group_unit2)

#     def test_add_group_unit_updates_active_nonce_if_new_nonce_is_next(self):
#         nonce1 = (Unit(type_ref=UnitTypeRef(alias="int"), value=0),)
#         nonce2 = (Unit(type_ref=UnitTypeRef(alias="int"), value=1),)
#         group_unit1 = GroupUnit(nonce=nonce1, owners=(), credentials=(), data=())
#         group_unit2 = GroupUnit(nonce=nonce2, owners=(), credentials=(), data=())
#         self.group.add_group_unit(group_unit1)
#         self.group.add_group_unit(group_unit2)
#         self.assertEqual(self.group.active_nonce, nonce2)