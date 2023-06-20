import json
import unittest

from groups.modules.decentralized_id import DecentralizedId
from groups.modules.nonce import Nonce
from groups.modules.nonce_unit import NonceUnit
from groups.modules.nonce_types import NonceTypes
from groups.modules.owner import Owner
from groups.modules.credentials import Credentials
from groups.modules.generic_data import GenericData
from groups.modules.universal_object import UniversalObject
from groups.modules.default_schema import DefaultSchema


class TestUniversalObject(unittest.TestCase):
    def setUp(self):
        self.nonce_types = NonceTypes()
        self.nonce_unit = NonceUnit(0, self.nonce_types.INTEGER_NONCE[0])
        self.decentralized_id = DecentralizedId("did:example:123")
        self.default_schema = DefaultSchema({"entry": "entry one"}, "schema")

        self.nonce = Nonce([self.nonce_unit])
        self.owner = Owner(self.decentralized_id)
        self.data = GenericData(self.default_schema)
        self.creds = Credentials(["username", "password"])
        self.obj = UniversalObject(self.nonce, self.data, self.owner, self.creds)

    def test_get_name(self):
        self.assertEqual(self.obj.get_name(), "UniversalObject")

    def test_get_description(self):
        self.assertEqual(self.obj.get_description(), "Universal serializable object")

    def test_get_owner(self):
        self.assertEqual(self.obj.get_owner(), self.owner)

    def test_get_nonce(self):
        self.assertEqual(self.obj.get_nonce(), self.nonce)

    def test_get_data(self):
        self.assertEqual(self.obj.get_data(), self.data)

    def test_get_creds(self):
        self.assertEqual(self.obj.get_creds(), self.creds)

    def test_set_name(self):
        self.obj.set_name("NewName")
        self.assertEqual(self.obj.get_name(), "NewName")

    def test_set_description(self):
        self.obj.set_description("NewDescription")
        self.assertEqual(self.obj.get_description(), "NewDescription")

    def test_set_owner(self):
        new_owner = Owner("Jane Doe")
        self.obj.set_owner(new_owner)
        self.assertEqual(self.obj.get_owner(), new_owner)

    def test_set_nonce(self):
        new_nonce = Nonce()
        self.obj.set_nonce(new_nonce)
        self.assertEqual(self.obj.get_nonce(), new_nonce)

    def test_set_data(self):
        new_data = GenericData()
        self.obj.set_data(new_data)
        self.assertEqual(self.obj.get_data(), new_data)

    def test_set_creds(self):
        new_creds = Credentials(["new_username", "new_password"])
        self.obj.set_creds(new_creds)
        self.assertEqual(self.obj.get_creds(), new_creds)

    def test_json(self):
        expected = {
            "name": "UniversalObject",
            "description": "Universal serializable object",
            "owner": self.owner.__str__(),
            "nonce": self.nonce.__str__(),
            "data": self.data.__str__(),
            "creds": self.creds.__str__()
        }
        self.maxDiff = None
        self.assertEqual(self.obj.__json__(), expected)

    def test_str(self):
        expected = json.dumps(self.obj.__json__(), indent=4, sort_keys=True)
        self.assertEqual(str(self.obj), expected)
