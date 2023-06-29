import unittest

from src.groups.base.units import Units
from src.groups.base.type import Type_, Id, Alias, Super, Prefix, Suffix, Separator, Function


class TestUnits(unittest.TestCase):
    def setUp(self):
        self.units = Units()

    def test_load_defaults(self):
        # Test loading default units
        # with open('src/groups/base/units/default_units.txt', 'r') as f:
        #     expected_units = json.loads(f.read())
        expected_units = [Type_(id=Id(value='string'), alias=Alias(value=['string', 'str']), super=Super(value='RESERVED'), prefix=Prefix(value=None), suffix=Suffix(value=None), separator=Separator(value=None), function=Function(value=str)), Type_(id=Id(value='integer'), alias=Alias(value=['integer', 'int']), super=Super(value='RESERVED'), prefix=Prefix(value=None), suffix=Suffix(value=None), separator=Separator(value=None), function=Function(value=int)), Type_(id=Id(value='float'), alias=Alias(value=['float']), super=Super(value='RESERVED'), prefix=Prefix(value=None), suffix=Suffix(value=None), separator=Separator(value=None), function=Function(value=float)), Type_(id=Id(value='boolean'), alias=Alias(value=['boolean', 'bool']), super=Super(value='RESERVED'), prefix=Prefix(value=None), suffix=Suffix(value=None), separator=Separator(value=None), function=Function(value=bool)), Type_(id=Id(value='list'), alias=Alias(value=['list']), super=Super(value='RESERVED'), prefix=Prefix(value='['), suffix=Suffix(value=']'), separator=Separator(value=','), function=Function(value=list)), Type_(id=Id(value='tuple'), alias=Alias(value=['tuple']), super=Super(value='RESERVED'), prefix=Prefix(value='('), suffix=Suffix(value=')'), separator=Separator(value=','), function=Function(value=tuple)), Type_(id=Id(value='dictionary'), alias=Alias(value=['dictionary', 'dict']), super=Super(value='RESERVED'), prefix=Prefix(value='{'), suffix=Suffix(value='}'), separator=Separator(value=','), function=Function(value=dict)), Type_(id=Id(value='bytes'), alias=Alias(value=['bytes']), super=Super(value='RESERVED'), prefix=Prefix(value="b'"), suffix=Suffix(value="'"), separator=Separator(value=None), function=Function(value=bytes))]
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