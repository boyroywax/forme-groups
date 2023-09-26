import unittest
import hashlib

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')
from src.groups.merkle_tree import MerkleTree


class TestMerkleTree(unittest.TestCase):
    def test_empty_tree(self):
        tree = MerkleTree()
        self.assertEqual(tree.root(), None)
