import unittest
import hashlib

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')
from src.groups.merkle_tree import MerkleTree


class TestMerkleTree(unittest.TestCase):
    def test_empty_tree(self):
        tree = MerkleTree()
        self.assertEqual(tree.root(), None)

    def test_tree_with_one_leaf(self):
        leaf = "test_leaf"
        leaf_hashed = hashlib.sha256(leaf.encode()).hexdigest()
        tree = MerkleTree(leaf_hashed)
        self.assertEqual(tree.root(), "a279c6691eb3035528a0fd8b65a607ed73896d0685a9605f2a1eb6484d8c3eca")

    def test_tree_with_two_leaves(self):
        leaf1 = "test_leaf1"
        leaf2 = "test_leaf2"
        leaf1_hashed = hashlib.sha256(leaf1.encode()).hexdigest()
        leaf2_hashed = hashlib.sha256(leaf2.encode()).hexdigest()
        tree = MerkleTree([leaf1_hashed, leaf2_hashed])
        self.assertEqual(tree.root(), "7e885bb1bca891ff63ad681a54105edf12bbc20378ee993efdd3a8c40dccbf6d")

    def test_tree_with_three_leaves(self):
        leaf1 = "test_leaf1"
        leaf2 = "test_leaf2"
        leaf3 = "test_leaf3"
        leaf1_hashed = hashlib.sha256(leaf1.encode()).hexdigest()
        leaf2_hashed = hashlib.sha256(leaf2.encode()).hexdigest()
        leaf3_hashed = hashlib.sha256(leaf3.encode()).hexdigest()
        tree = MerkleTree([leaf1_hashed, leaf2_hashed, leaf3_hashed])
        self.assertEqual(tree.root(), "0e541b96ba6ba48fa3785d4cc4611ad7c9a09ec7a22a1883a35530308363cb01")

    def test_merkle_tree_verify(self):
        leaf1 = "test_leaf1"
        leaf2 = "test_leaf2"
        leaf3 = "test_leaf3"
        leaf1_hashed = hashlib.sha256(leaf1.encode()).hexdigest()
        leaf2_hashed = hashlib.sha256(leaf2.encode()).hexdigest()
        leaf3_hashed = hashlib.sha256(leaf3.encode()).hexdigest()
        tree = MerkleTree([leaf1_hashed, leaf2_hashed, leaf3_hashed])
        self.assertTrue(tree.verify(leaf1_hashed))

    def test_merkle_tree_not_verified_leaf(self):
        leaf1 = "test_leaf1"
        leaf2 = "test_leaf2"
        leaf3 = "test_leaf3"
        leaf1_hashed = hashlib.sha256(leaf1.encode()).hexdigest()
        leaf2_hashed = hashlib.sha256(leaf2.encode()).hexdigest()
        leaf3_hashed = hashlib.sha256(leaf3.encode()).hexdigest()
        tree = MerkleTree([leaf1_hashed, leaf2_hashed, leaf3_hashed])
        self.assertFalse(tree.verify("not_a_leaf"))

