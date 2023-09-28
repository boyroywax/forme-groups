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
        self.group = Group()

    def test_init(self):
        self.assertIsInstance(self.group, Group)

    def test_add_unit(self):
        nonce = self.group._group_unit_creator.create_nonce(items=[self.group._group_unit_creator.create_unit(value=1, alias=UnitTypeRef(alias="int"))])
        owners = self.group._group_unit_creator.create_group_subunit(items=[self.group._group_unit_creator.create_unit(value="Alice", alias=UnitTypeRef(alias="str"))])
        creds = self.group._group_unit_creator.create_group_subunit(items=[self.group._group_unit_creator.create_unit(value="password", alias=UnitTypeRef(alias="str"))])
        data = self.group._group_unit_creator.create_data(items=[self.group._group_unit_creator.create_unit(value=True, alias=UnitTypeRef(alias="bool"))])

        group_unit = self.group.create_group_unit(nonce=nonce, owners=owners, creds=creds, data=data)
        self.assertTrue(self.group.contains(group_unit))