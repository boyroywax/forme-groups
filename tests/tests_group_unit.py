import unittest
import sys

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")

from src.groups.group_unit_creator import GroupUnitCreator
from src.groups.unit_type import UnitTypeRef
from src.groups.unit_pool import UnitPool
from src.groups.unit_creator import UnitCreator
from src.groups.nonce import Nonce
from src.groups.data import Data
from src.groups.group_subunit import GroupSubUnit
from src.groups.group_unit import GroupUnit
from src.groups.unit import Unit, UnitTypeRef
from src.groups.group_unit_pool import GroupUnitPool

class TestGroupUnit(unittest.TestCase):
    def setUp(self):
        self.nonce = Nonce(items=[Unit(value=1, type_ref=UnitTypeRef(alias="int"))])
        self.owners = GroupSubUnit(items=[Unit(value="Alice", type_ref=UnitTypeRef(alias="str"))])
        self.creds = GroupSubUnit(items=[Unit(value="password", type_ref=UnitTypeRef(alias="str"))])
        self.data = Data(items=[Unit(value=True, type_ref=UnitTypeRef(alias="bool"))])
        self.group_unit = GroupUnit(nonce=self.nonce, owners=self.owners, creds=self.creds, data=self.data)

    def test_init(self):
        self.assertEqual(self.group_unit.nonce, self.nonce)
        self.assertEqual(self.group_unit.owners, self.owners)
        self.assertEqual(self.group_unit.creds, self.creds)
        self.assertEqual(self.group_unit.data, self.data)

    def tests_hash_slots(self):
        self.assertEqual(self.group_unit.__slots__, ("nonce", "owners", "creds", "data"))

    def test_str(self):
        expected_str = f"GroupUnit(nonce={self.nonce}, owners={self.owners}, creds={self.creds}, data={self.data})"
        self.assertEqual(str(self.group_unit), expected_str)

    def test_eq(self):
        group_unit2 = GroupUnit(nonce=self.nonce, owners=self.owners, creds=self.creds, data=self.data)
        self.assertEqual(self.group_unit, group_unit2)

    def test_neq(self):
        nonce2 = Nonce(items=[Unit(value=2, type_ref=UnitTypeRef(alias="int"))])
        group_unit2 = GroupUnit(nonce=nonce2, owners=self.owners, creds=self.creds, data=self.data)
        self.assertNotEqual(self.group_unit, group_unit2)