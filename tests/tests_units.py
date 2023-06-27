import unittest
from unittest.mock import MagicMock
from src.groups.units import Units
from src.groups.units import UnitType as Type_
from src.groups.units import UnitValue as Value_


class TestUnits(unittest.TestCase):
    def setUp(self):
        self.units = Units()

    def test_add_unit(self):
        # Create a mock Type_ object
        unit = Units().generate_unit()

        # Add a unit to the Units object
        self.units.add_unit(unit)

        # Verify that the unit was added correctly
        self.assertEqual(self.units.units["m"], mock_type)

    def test_remove_unit(self):
        # Create a mock Type_ object
        mock_type = MagicMock()

        # Add a unit to the Units object
        self.units.add_unit("m", mock_type)

        # Remove the unit from the Units object
        self.units.remove_unit("m")

        # Verify that the unit was removed correctly
        self.assertNotIn("m", self.units.units)

    def test_get_unit(self):
        # Create a mock Type_ object
        mock_type = MagicMock()

        # Add a unit to the Units object
        self.units.add_unit("m", mock_type)

        # Get the unit from the Units object
        unit = self.units.get_unit("m")

        # Verify that the unit was retrieved correctly
        self.assertEqual(unit, mock_type)

    def test_get_unit_with_alias(self):
        # Create a mock Type_ object
        mock_type = MagicMock()

        # Add a unit with an alias to the Units object
        self.units.add_unit("m", mock_type)
        self.units.add_alias("meter", "m")

        # Get the unit using the alias from the Units object
        unit = self.units.get_unit("meter")

        # Verify that the unit was retrieved correctly
        self.assertEqual(unit, mock_type)

    def test_add_alias(self):
        # Create a mock Type_ object
        mock_type = MagicMock()

        # Add a unit to the Units object
        self.units.add_unit("m", mock_type)

        # Add an alias to the Units object
        self.units.add_alias("meter", "m")

        # Verify that the alias was added correctly
        self.assertEqual(self.units.aliases["meter"], "m")

    def test_remove_alias(self):
        # Create a mock Type_ object
        mock_type = MagicMock()

        # Add a unit to the Units object
        self.units.add_unit("m", mock_type)

        # Add an alias to the Units object
        self.units.add_alias("meter", "m")

        # Remove the alias from the Units object
        self.units.remove_alias("meter")

        # Verify that the alias was removed correctly
        self.assertNotIn("meter", self.units.aliases)

    def test_get_alias(self):
        # Create a mock Type_ object
        mock_type = MagicMock()

        # Add a unit to the Units object
        self.units.add_unit("m", mock_type)

        # Add an alias to the Units object
        self.units.add_alias("meter", "m")

        # Get the alias from the Units object
        alias = self.units.get_alias("meter")

        # Verify that the alias was retrieved correctly
        self.assertEqual(alias, "m")
