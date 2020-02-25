import unittest
from rbt import RedBlackTreeMap

class TestRBT(unittest.TestCase):
    def setUp(self):
        print("Setting up...")
        #Empty BST
        self.emptyTree = RedBlackTreeMap()

        #populated BST
        self.testTree = RedBlackTreeMap()
        keys = [30, 40, 24, 58, 48, 26, 11, 13]
        for i in keys:
            self.testTree.__setitem__(i, "Success")
    
    def test_searchItem(self):
        #Test with invalid key
        with self.assertRaises(KeyError):
            self.testTree.__getitem__(29)

        
        #Test with valid key, red color
        searchItem = self.testTree.__getitem__(40)
        self.assertEqual(searchItem.get_key(),40)
        self.assertEqual("RED", self.testTree._get_color(searchItem))

        #Test with valid key, black color
        searchItem = self.testTree.__getitem__(48)
        self.assertEqual(searchItem.get_key(),48)
        self.assertEqual("BLACK", self.testTree._get_color(searchItem))
    
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
    
    def test_deleteItem(self):
        #Test with deletion in an empty tree
        self.assertEqual(self.emptyTree.__delitem__(9),None)

        #Test with deletion of a non-existing key
        with self.assertRaises(KeyError):
            self.testTree.__delitem__(2)

        #Test with deletion of an existing key
        self.testTree.__delitem__(11)
        with self.assertRaises(KeyError):
            self.testTree.__getitem__(11)

        
        #Test with deletion of root
        self.testTree.__delitem__(self.testTree.root().get_key())
        self.assertEqual(self.testTree.root().get_key(), 26)
        

    def tearDown(self):
        print("Tearing down...")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)