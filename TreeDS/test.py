import unittest
from bst import TreeMap
class TestBST(unittest.TestCase):
    
    def setUp(self):
        print("Setting up...")
        #Empty BST
        self.emptyTree = TreeMap()

        #populated BST
        self.testTree = TreeMap()
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

        #Test with deleted node
        self.testTree.__delitem__(24)
        with self.assertRaises(KeyError):
            self.testTree.__getitem__(24)
        

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
        
    def test_firstItem(self):
        #Test with first item in an empty tree
        self.assertEqual(self.emptyTree.first(),None)
        
        #Test with first item in a populated tree (should return smallest key)
        self.assertEqual(self.testTree.first().get_key(), 11)


    def test_lastItem(self):
        #Test with last item in an empty tree
        self.assertEqual(self.emptyTree.first(),None)
        
        #Test with last item in a populated tree (should return largest key)
        self.assertEqual(self.testTree.last().get_key(), 58)

    def test_before(self):
        #Test with a populated tree (Should return largest key smaller than root (26))
        self.assertEqual(self.testTree.before(self.testTree.root()).get_key(), 26)

    def test_last(self):
        #Test with a populated tree (Should return smallest key larger than root (40))
        self.assertEqual(self.testTree.after(self.testTree.root()).get_key(), 40)

    def tearDown(self):
        print("Tearing down...")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
        

