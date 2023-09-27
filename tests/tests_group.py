import unittest
import sys
from unittest.mock import MagicMock

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")

from src.groups.unit import Unit
from src.groups.unit_type import UnitTypeRef
from src.groups.group_unit import GroupUnit
from src.groups.group_subunit import GroupSubUnit
from src.groups.group_unit_pool import GroupUnitPool
from src.groups.group_unit_creator import GroupUnitCreator
from src.groups.unit_creator import UnitCreator
from src.groups.group import Group


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.group_unit1 = MagicMock(spec=GroupUnit)
        self.group_unit2 = MagicMock(spec=GroupUnit)
        self.group_unit_pool = MagicMock(spec=GroupUnitPool)
        self.group_unit_pool.contains.return_value = True
        self.group_unit_pool.__iter__.return_value = iter([self.group_unit1, self.group_unit2])
        self.group = Group(self.group_unit_pool)

    def test_init(self):
        self.assertEqual(self.group.unit_pool, self.group_unit_pool)

    def test_add_unit(self):
        self.group_unit_creator = MagicMock()
        self.group_unit_creator.create.return_value = self.group_unit1
        self.group.add_unit(self.group_unit_creator)
        self.group_unit_pool.add.assert_called_once_with(self.group_unit1)

    def test_add_unit_duplicate(self):
        self.group_unit_creator = MagicMock()
        self.group_unit_creator.create.return_value = self.group_unit1
        self.group_unit_pool.contains.return_value = True
        with self.assertRaises(ValueError):
            self.group.add_unit(self.group_unit_creator)

    def test_get_units(self):
        units = self.group.get_units()
        self.assertEqual(units, [self.group_unit1, self.group_unit2])