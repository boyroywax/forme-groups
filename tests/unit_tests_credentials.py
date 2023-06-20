import unittest
from groups.modules.credentials import Credentials

class TestCredentials(unittest.TestCase):
    def test_get_verified_credentials(self):
        creds = Credentials(["username", "password"])
        self.assertEqual(creds.get_verified_credentials(), ["username", "password"])

    def test_set_verified_credentials(self):
        creds = Credentials(["username", "password"])
        creds.set_verified_credentials(["new_username", "new_password"])
        self.assertEqual(creds.get_verified_credentials(), ["new_username", "new_password"])

    def test_add_verified_credential(self):
        creds = Credentials(["username", "password"])
        creds.add_verified_credential("new_credential")
        self.assertEqual(creds.get_verified_credentials(), ["username", "password", "new_credential"])

    def test_remove_verified_credential(self):
        creds = Credentials(["username", "password", "new_credential"])
        creds.remove_verified_credential(1)
        self.assertEqual(creds.get_verified_credentials(), ["username", "new_credential"])

    def test_get_verified_credential(self):
        creds = Credentials(["username", "password", "new_credential"])
        self.assertEqual(creds.get_verified_credential(1), "password")

    def test_get_verified_credential_length(self):
        creds = Credentials(["username", "password", "new_credential"])
        self.assertEqual(creds.get_verified_credential_length(), 3)
