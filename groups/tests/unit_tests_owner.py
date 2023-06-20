import unittest

from groups.modules.owner import Owner
from groups.modules.decentralized_id import DecentralizedId


class TestOwner(unittest.TestCase):
    def test_get_did(self):
        did = DecentralizedId("did:example:123")
        owner = Owner(did)
        self.assertEqual(owner.get_did(), did)

    def test_set_did(self):
        did = DecentralizedId("did:example:123")
        owner = Owner(did)
        new_did = DecentralizedId("did:example:456")
        owner.set_did(new_did)
        self.assertEqual(owner.get_did(), new_did)

    def test_json(self):
        did = DecentralizedId("did:example:123")
        owner = Owner(did)
        self.assertEqual(owner.__json__(), {"did": "did:example:123"})

    def test_str(self):
        did = DecentralizedId("did:example:123")
        owner = Owner(did)
        self.assertEqual(owner.__str__(), '{"did": "did:example:123"}')
