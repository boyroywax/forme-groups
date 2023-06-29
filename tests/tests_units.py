import unittest
# from io import StringIO
from src.groups.base.units import Units


class TestUnits(unittest.TestCase):
    def setUp(self):
        self.units = Units()

    def test_load_defaults(self):
        # Test loading default units
        with open('src/groups/base/units/default_units.txt', 'r') as f:
            expected_units = f.read()
        self.units._load_defaults()
        self.assertEqual(self.units.types, expected_units)

    # def test_load_custom(self):
    #     # Test loading custom units
    #     with patch('src.groups.base.units.open') as mock_open:
    #         mock_open.return_value.__enter__.return_value.read.return_value = 'test_units'
    #         self.units._load_custom()
    #         mock_open.assert_called_once_with('src/groups/base/units/custom_units.txt', 'r')
    #         self.assertEqual(self.units._units, 'test_units')

    # def test_load_all(self):
    #     # Test loading all units
    #     with patch('src.groups.base.units.open') as mock_open:
    #         mock_open.return_value.__enter__.return_value.read.return_value = 'test_units'
    #         self.units._load_all()
    #         mock_open.assert_any_call('src/groups/base/units/default_units.txt', 'r')
    #         mock_open.assert_any_call('src/groups/base/units/custom_units.txt', 'r')
    #         self.assertEqual(self.units._units, 'test_units')

    def test_load_invalid(self):
        # Test loading invalid units
        with self.assertRaises(ValueError):
            self.units._load('invalid')

    def test_load_no_arg(self):
        # Test loading with no argument
        with self.assertRaises(TypeError):
            self.units._load()

    def test_load_multiple_args(self):
        # Test loading with multiple arguments
        with self.assertRaises(TypeError):
            self.units._load('default', 'custom')