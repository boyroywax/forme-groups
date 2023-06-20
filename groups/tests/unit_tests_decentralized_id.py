import unittest
from groups.modules.decentralized_id import DecentralizedId


class TestDecentralizedId(unittest.TestCase):
    def setUp(self):
        self.did = DecentralizedId("did:example:123")
        
    def fail_initiation(self):
        with self.assertRaises(TypeError):
            self.did = DecentralizedId()

    def test_get_did(self):
        self.assertEqual(self.did.get_did(), "did:example:123")

    def test_set_did(self):
        self.did.set_did("did:example:1234")
        self.assertEqual(self.did.get_did(), "did:example:1234")

    def test_str(self):
        self.did.set_did("did:example:1234")
        self.assertEqual(str(self.did), "did:example:1234")
