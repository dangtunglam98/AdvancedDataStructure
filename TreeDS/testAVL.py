import unittest
from avl import AVLTreeMap

class TestAVL(unittest.TestCase):

    def setUp(self):
        print("Setting up...")
        #Empty BST
        self.emptyTree = AVLTreeMap()

        #populated BST
        self.testTree = AVLTreeMap()
        keys = [30, 40, 24, 58, 48, 26, 11, 13]
        for i in keys:
            self.testTree[i] = "success"

    def test_check_insert_balance(self):
        #check Balance of Empty Tree
        self.assertEqual(self.emptyTree.is_balanced(), True)
        
        #Check Balance of Populated Tree
        self.assertEqual(self.testTree.is_balanced(), True)


        #Check Balance of Imbalance Tree
        self.testTree.set_item_bst(7,'Failed')
        self.testTree.set_item_bst(8,'Failed')
        self.testTree.set_item_bst(9,'Failed')
        self.testTree.assign_tree_height()   #Reassign all height for the tree without any rotation
        self.assertEqual(self.testTree.is_balanced(), False)
    
    def test_check_delete_balance(self):
        #Test with deletion in an empty tree
        self.assertEqual(self.emptyTree.__delitem__(9),None)

        #check Balance of Empty Tree
        self.assertEqual(self.emptyTree.is_balanced(), True)

        #Test with deletion of a non-existing key
        with self.assertRaises(KeyError):
            self.testTree.__delitem__(10)
        
        self.testTree.__delitem__(11)
        with self.assertRaises(KeyError):
            self.testTree.__getitem__(11)
        #check Balance of Populated Tree after Deletion
        self.assertEqual(self.emptyTree.is_balanced(), True)
        

    def tearDown(self):
        print("Tearing down...")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
