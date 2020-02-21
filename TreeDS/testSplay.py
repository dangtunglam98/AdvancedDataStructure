import unittest
from splayTree import SplayTree

class testSplay(unittest.TestCase):
    def setUp(self):
        print("Setting up...")
        #Empty Splay Tree
        self.emptyTree = SplayTree()

        #populated Splay Tree
        self.testTree = SplayTree()
        keys = [30, 40, 24, 58, 48, 26, 11, 13]
        for i in keys:
            self.testTree[i] = "success"
    
    def test_check_access(self):
        #Check Empty Splay Tree
        with self.assertRaises(KeyError):
            self.testTree[100]
        
        #Check Access with populated Splay Tree
        #After performing a splay for search, the search Item should be at the root
        searchedItem = self.testTree[58]
        self.assertEqual(searchedItem, self.testTree.root())
        keys = [30, 40, 24, 58, 48, 26, 11, 13]
        for i in keys:
            self.testTree[i] = "success"

    def test_check_insert(self):
        #check Insertion to Empty Tree
        #Insert a list and check everytime we insert, the keys is at the root
        keys = [30, 40, 24, 58, 48, 26, 11, 13]
        for i in keys:
            self.emptyTree[i] = "success"
            self.assertEqual(self.emptyTree.root().get_key(), i)

        #The correct left and right of the splay tree should be like Figure 1.1 Initial in the pdf
        self.assertEqual(self.emptyTree.right(self.emptyTree.root()).get_key(), 24)
        self.assertEqual(self.emptyTree.left(self.emptyTree.root()).get_key(), 11)
        
        #populated BST (Reference to Figure 1.2)
        self.testTree[25] = "success"
        self.assertEqual(self.testTree.root().get_key(), 25)
        self.assertEqual(self.testTree.right(self.testTree.root()).get_key(), 26)
        self.assertEqual(self.testTree.left(self.testTree.root()).get_key(), 13)
    
    def test_check_delete(self):
        #Check Deletion to Empty Tree
        self.assertEqual(self.emptyTree.__delitem__(30), None)

        #Check Deletion for populated tree
        self.testTree.__delitem__(48)
        self.assertEqual(self.testTree.root().get_key(), 40)

        #Check Deletion of non-existence key in populated tree
        self.testTree.__delitem__(100)
        self.assertEqual(self.testTree.root().get_key(), 58)

        

    def tearDown(self):
        print("Tearing down...")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
