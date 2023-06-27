import unittest
from unittest.mock import patch
from groups.manager.system import System


class TestSystem(unittest.TestCase):
    def test_init(self):
        # Create a new System object
        system = System()

        # Verify that the ID is not None
        self.assertIsNotNone(system.id)

        # Verify that the config is None
        self.assertIsNone(system.config)

    def test_init_with_id(self):
        # Create a new System object with a specific ID
        system = System(id="test_id")

        # Verify that the ID is set correctly
        self.assertEqual(system.id, "test_id")

        # Verify that the config is None
        self.assertIsNone(system.config)

    def test_init_with_config(self):
        # Create a mock SystemConfig object
        mock_config = object()

        # Create a new System object with a specific config
        system = System(config=mock_config)

        # Verify that the ID is not None
        self.assertIsNotNone(system.id)

        # Verify that the config is set correctly
        self.assertEqual(system.config, mock_config)

    @patch("src.groups.system.SystemConfig")
    def test_set_config(self, mock_config):
        # Create a new System object
        system = System()

        # Call set_config with override_defaults=True and overrides={"test": "value"}
        system.set_config(override_defaults=True, overrides={"test": "value"})

        # Verify that SystemConfig was initialized with the correct arguments
        mock_config.assert_called_once_with(system, override_defaults=True, overrides={"test": "value"})
        
        # Verify that the config is set correctly
        self.assertEqual(system.config, mock_config.return_value)
