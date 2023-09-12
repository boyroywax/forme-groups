import unittest
import sys

sys.path.append("/Users/j/Documents/Forme/code/forme-groups")

from src.groups.unit import UnitTypeRef, UnitTypeFunction, UnitType, UnitTypePool, Unit, UnitGenerator
from src.groups.group import GroupUnit, GroupUnitGenerator, Nonce, Ownership, Credentials, Data


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