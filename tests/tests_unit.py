
import unittest
import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.unit import Unit, UnitType, UnitTypePool, GroupUnit, Group


class TestUnit(unittest.TestCase):
    def SetUp(self):
        self.unit_type_pool = UnitTypePool()

    def test_init(self):
        # Test that the UnitTypePool is initialized
        self.SetUp()
        self.assertIsInstance(self.unit_type_pool, UnitTypePool)

        # Test that the UnitTypePool contains the system types
        self.assertEqual(len(self.unit_type_pool), 8)

    def test_unit_type_pool_get(self):
        # Test that the UnitTypePool returns the correct UnitType
        self.SetUp()
        unit_type = self.unit_type_pool.get(UnitType.Ref(name="string"))
        self.assertEqual(unit_type, self.unit_type_pool.types[0])

    def test_unit_type_pool_add(self):
        # Test that the UnitTypePool adds a UnitType
        self.SetUp()
        unit_type = UnitType(aliases=[UnitType.Ref(name="test")], base_type=[UnitType.Ref(name="string")])
        self.unit_type_pool.add(unit_type)
        self.assertEqual(len(self.unit_type_pool), 9)

    def test_unit_type_pool_remove(self):
        # Test that the UnitTypePool removes a UnitType
        self.SetUp()
        unit_type = self.unit_type_pool.get(UnitType.Ref(name="string"))
        with self.assertRaises(Exception):
            self.unit_type_pool.remove(unit_type)
        self.assertEqual(len(self.unit_type_pool), 8)

    def test_unit_type_pool_contains(self):
        # Test that the UnitTypePool contains a UnitType
        self.SetUp()
        self.assertTrue(UnitType.Ref(name="string") in self.unit_type_pool)

    def test_create_unit(self):
        # Test that the UnitTypePool creates a Unit
        self.SetUp()
        unit = self.unit_type_pool.create_unit(UnitType.Ref(name="string"), "test")
        self.assertIsInstance(unit, Unit)

    def test_create_unit_bad_type(self):
        # Test that the UnitTypePool raises an Exception when creating a Unit with a bad type
        self.SetUp()
        with self.assertRaises(Exception):
            self.unit_type_pool.create_unit(UnitType.Ref(name="bad_type"), "test")

        frozen_unit = self.unit_type_pool.create_unit(UnitType.Ref(name="string"), "test_bad_type")
        with self.assertRaises(Exception):
            frozen_unit.value = "test"

    def test_create_unit_bad_value(self):
        # Test that the UnitTypePool raises an Exception when creating a Unit with a bad value
        self.SetUp()
        mismatched_Unit_type = self.unit_type_pool.create_unit(UnitType.Ref(name="string"), 1)
        self.assertEqual(mismatched_Unit_type.value, "1")

    def test_enforce_type(self):
        # Test that the UnitTypePool enforces a type
        self.SetUp()
        enforced_type = self.unit_type_pool.enforce_type(UnitType.Ref(name="int"), 1)
        self.assertEqual(enforced_type, 1)

    def test_enforce_type_bad_type(self):
        # Test that the UnitTypePool raises an Exception when enforcing a bad type
        self.SetUp()
        with self.assertRaises(Exception):
            self.unit_type_pool.enforce_type(UnitType.Ref(name="bad_type"), 1)

    def test_nonce_value(self):
        nonce = GroupUnit.Nonce(value=[Unit(type_ref='foo'), Unit(type_ref='bar')])
        self.assertEqual(nonce.value, [Unit(type_ref='foo'), Unit(type_ref='bar')])

    def test_ownership_value(self):
        ownership = GroupUnit.Ownership(value=[Unit(type_ref='baz')])
        self.assertEqual(ownership.value, [Unit(type_ref='baz')])

    def test_credentials_value(self):
        credentials = GroupUnit.Credentials(value=[Unit(type_ref='qux')])
        self.assertEqual(credentials.value, [Unit(type_ref='qux')])

    def test_data_value(self):
        data = GroupUnit.Data(value=[Unit(type_ref='quux')])
        self.assertEqual(data.value, [Unit(type_ref='quux')])

    def test_pool_has_nonce(self):
        group = Group()
        nonce = GroupUnit.Nonce(value=[Unit(type_ref='foo'), Unit(type_ref='bar')])
        group_unit = GroupUnit(nonce=nonce)
        group.units.append(group_unit)
        self.assertTrue(group.pool_has_nonce(nonce.value))

    def test_add_group_unit(self):
        group = Group()
        nonce = GroupUnit.Nonce(value=[Unit(type_ref='foo'), Unit(type_ref='bar')])
        group_unit = GroupUnit(nonce=nonce)
        group.add_group_unit(group_unit)
        self.assertIn(group_unit, group.units)

    def test_get_next_nonce(self):
        group = Group()
        nonce = group.get_next_nonce()
        self.assertIsInstance(nonce, GroupUnit.Nonce)
        self.assertEqual(nonce.value, [Unit(type_ref='int', value=1)])

        group_unit = GroupUnit(nonce=nonce)
        nonce = self.group.get_next_nonce(group_unit)
        self.assertIsInstance(nonce, GroupUnit.Nonce)
        self.assertEqual(nonce.value, [Unit(type_ref='int', value=2)])