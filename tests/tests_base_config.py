import unittest
from src.groups.modules.__config.__config import Config_


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config_()

    def test_set_config_list(self):
        configs = [
            {
                "name": "config1",
                "system_types": {
                    "super_type": "string",
                    "types": ["str", "int", "float"]
                }
            },
            {
                "name": "config2",
                "system_types": {
                    "super_type": "string",
                    "types": ["bool", "bytes", "list"]
                }
            }
        ]
        self.config.set_config_list(configs)
        self.assertNotEqual(self.config.loaded_configs, configs)

    def test_check_for_supported_system_types(self):
        self.config.active_config = {
            "name": "default",
            "system_types": {
                "super_type": "string",
                "types": ["str", "int", "float", "bool", "bytes", "list", "tuple", "dict"]
            }
        }
        supported_types = self.config.check_for_supported_system_types()
        expected_types = ["str", "int", "float", "bool", "bytes", "list", "tuple", "dict"]
        self.assertEqual(supported_types, expected_types)

    def test_check_for_supported_system_types_no_config(self):
        """
        When no config is set, the default config is used.
        """
        self.config.active_config = None
        supported_types = self.config.check_for_supported_system_types()
        default_supported_types = ["str", "int", "float", "bool", "bytes", "list", "tuple", "dict"]
        self.assertEqual(supported_types, default_supported_types)

    def test_check_for_supported_system_types_no_types(self):
        self.config.active_config = {
            "name": "default",
            "system_types": {
                "super_type": "string",
                "types": []
            }
        }
        supported_types = self.config.check_for_supported_system_types()
        default_supported_types = ["str", "int", "float", "bool", "bytes", "list", "tuple", "dict"]
        self.assertEqual(supported_types, default_supported_types)

