import unittest
import sys
from unittest.mock import MagicMock

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")

from src.groups.unit import Unit
from src.groups.unit_type import UnitTypeRef
from src.groups.group_unit import GroupUnit
from src.groups.group_subunit import GroupSubUnit
from src.groups.group_unit_creator import GroupUnitCreator
from src.groups.unit_creator import UnitCreator
from src.groups.group import Group


class TestGroupSubUnit(unittest.TestCase):
    def setUp(self):
        self.unit1 = Unit(value="Alice", type_ref=UnitTypeRef(alias="str"))
        self.unit2 = Unit(value=30, type_ref=UnitTypeRef(alias="int"))
        self.group_subunit = GroupSubUnit(items=[self.unit1, self.unit2])

    def test_init(self):
        self.assertEqual(self.group_subunit.items, [self.unit1, self.unit2])

    def test_str(self):
        expected_str = f"GroupSubUnit(items=[{str(self.unit1)}, {str(self.unit2)}])"
        self.assertEqual(str(self.group_subunit), expected_str)

    def test_eq(self):
        group_subunit2 = GroupSubUnit(items=[self.unit1, self.unit2])
        self.assertEqual(self.group_subunit, group_subunit2)

    def test_neq(self):
        unit3 = Unit(value="Bob", type_ref=UnitTypeRef(alias="str"))
        group_subunit2 = GroupSubUnit(items=[self.unit1, unit3])
        self.assertNotEqual(self.group_subunit, group_subunit2)