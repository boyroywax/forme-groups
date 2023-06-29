import unittest

from src.groups.base.units import Units
from src.groups.base.type import Type_, Id, Alias, Super, Prefix, Suffix, Separator, Function


class TestUnits(unittest.TestCase):
    def setUp(self):
        self.units = Units()

    def test_load_defaults(self):
        # Test loading default units
        expected_units = [Type_(id_=Id(value='string'), alias=Alias(value=['string', 'str']), super_=Super(value='RESERVED'), prefix=Prefix(value=None), suffix=Suffix(value=None), separator=Separator(value=None), function_=Function(value=str)), Type_(id_=Id(value='integer'), alias=Alias(value=['integer', 'int']), super_=Super(value='RESERVED'), prefix=Prefix(value=None), suffix=Suffix(value=None), separator=Separator(value=None), function_=Function(value=int)), Type_(id_=Id(value='float'), alias=Alias(value=['float']), super_=Super(value='RESERVED'), prefix=Prefix(value=None), suffix=Suffix(value=None), separator=Separator(value=None), function_=Function(value=float)), Type_(id_=Id(value='boolean'), alias=Alias(value=['boolean', 'bool']), super_=Super(value='RESERVED'), prefix=Prefix(value=None), suffix=Suffix(value=None), separator=Separator(value=None), function_=Function(value=bool)), Type_(id_=Id(value='list'), alias=Alias(value=['list']), super_=Super(value='RESERVED'), prefix=Prefix(value='['), suffix=Suffix(value=']'), separator=Separator(value=','), function_=Function(value=list)), Type_(id_=Id(value='tuple'), alias=Alias(value=['tuple']), super_=Super(value='RESERVED'), prefix=Prefix(value='('), suffix=Suffix(value=')'), separator=Separator(value=','), function_=Function(value=tuple)), Type_(id_=Id(value='dictionary'), alias=Alias(value=['dictionary', 'dict']), super_=Super(value='RESERVED'), prefix=Prefix(value='{'), suffix=Suffix(value='}'), separator=Separator(value=','), function_=Function(value=dict)), Type_(id_=Id(value='bytes'), alias=Alias(value=['bytes']), super_=Super(value='RESERVED'), prefix=Prefix(value="b'"), suffix=Suffix(value="'"), separator=Separator(value=None), function_=Function(value=bytes))]
        self.units._load_defaults()
        self.assertEqual(self.units.types, expected_units)

    def test_load_custom(self):
        # Test loading custom units
        expected_units = [Type_(id_=Id(value='custom'), alias=Alias(value=['custom']), super_=Super(value='RESERVED'), prefix=Prefix(value='['), suffix=Suffix(value=']'), separator=Separator(value=','), function_=Function(value=list))] 


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