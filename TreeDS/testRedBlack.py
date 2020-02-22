import unittest
from redBlackTree import RedBlackTree

class TestRBT(unittest.TestCase):
    def setUp(self):
        #Empty BST
        self.emptyTree = RedBlackTree()

        #populated BST
        self.testTree = RedBlackTree()
        keys = [30, 40, 24, 58, 48, 26, 11, 13]
        for i in keys:
            self.testTree.__setitem__(i, "Success")
    
    def test_searchItem(self):
        #Test with invalid key
        with self.assertRaises(KeyError):
            self.testTree.__getitem__(29)

        
        #Test with valid key
        searchItem = self.testTree.__getitem__(30)
        self.assertEqual(searchItem.get_key(),30)
        self.assertEqual(searchItem, self.testTree.root())
    
    def test_insertItem(self):
        #Test with inserting root
        self.emptyTree.__setitem__(1, "Dave")
        searchItem = self.emptyTree.__getitem__(1)
        self.assertEqual(searchItem, self.emptyTree.root())

        #Test with inserting into populated tree
        with self.assertRaises(KeyError):   
            self.testTree.__getitem__(3)
        self.testTree.__setitem__(3, "Good")
        searchItem = self.testTree.__getitem__(3)
        self.assertEqual(searchItem.get_value(), "Good")

        #Test with replacing value for existing key
        self.testTree.__setitem__(3, "Better")
        searchItem = self.testTree.__getitem__(3)
        self.assertEqual(searchItem.get_value(), "Better")
    
    def tearDown(self):
        print("Tearing down...")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)