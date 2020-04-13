from disjoint import DisjointSetDS
from node import  DJNode
from pptree import  ParentPointTree
import unittest

class testDJ(unittest.TestCase):
    def setUp(self):
        print("Setting up.....")
        dogs = ["Aidi", "Bulldog", "golden", "chihuahua"]
        birds = ["parrot", "sparrow", "hawk", "eagle"]
        cats = ["Persian", "Bengal", "Maine Coon", "British", "Sphynx"]
        bears = ["Asiatic", "Black", "Brown", "Panda", "Polar", "Sloth"]

        self.dogs_entity = [DJNode(name) for name in dogs]
        self.birds_entity = [DJNode(name) for name in birds]
        self.cats_entity = [DJNode(name) for name in cats]
        self.bears_entity = [DJNode(name) for name in bears]

        self.forest = DisjointSetDS()
        #Insert Dog set
        self.forest.insert_as_new_tree("Dog", self.dogs_entity[0])
        for items in self.dogs_entity[1:]:
            self.forest.insert_into_tree(items, self.dogs_entity[0])

        #Insert Birds set
        self.forest.insert_as_new_tree("Bird", self.birds_entity[0])
        for items in self.birds_entity[1:]:
            self.forest.insert_into_tree(items, self.birds_entity[0])

        #Insert Cats set
        self.forest.insert_as_new_tree("Cat", self.cats_entity[0])
        for items in self.cats_entity[1:]:
            self.forest.insert_into_tree(items, self.cats_entity[0])

    def test_iterate(self):
        #Testing the list of sets in the Data Structure
        self.assertEqual(self.forest.iterate(), ["Dog", "Bird", "Cat"])

    def test_newTree(self):
        #Test the insertion of new Set into the Data Structure
        self.forest.insert_as_new_tree("Bear", self.bears_entity[0])
        self.assertEqual(self.forest.iterate(), ["Dog", "Bird", "Cat", "Bear"])
        self.assertEqual(self.bears_entity[0].get_set_name(), "Bear")

    def test_existedTree(self):
        #Test the insertion of existed Tree

        self.forest.insert_as_new_tree("Bear", self.bears_entity[0])
        for items in self.bears_entity[1:]:
            self.forest.insert_into_tree(items, self.bears_entity[0])

        #Test if every item in the same set
        for items in self.bears_entity[1:]:
            self.assertEqual(items.get_set_name(), None)
            self.assertEqual(self.forest.find(items), self.bears_entity[0])

    def test_find(self):
        #Test find root
        for items in self.cats_entity[1:]:
            self.assertEqual(self.forest.find(items), self.cats_entity[0])

        #Test flattening
        for items in self.cats_entity[1:]:
            self.assertEqual(items.get_parent(), self.cats_entity[0])

    def test_merge(self):
        #Test the merging of 2 trees

        self.forest.merge_trees(self.cats_entity[0], self.dogs_entity[0])
        #Test if the old root still have its old set name
        self.assertEqual(self.dogs_entity[0].get_set_name(), None)
        self.assertEqual(len(self.forest.iterate()), 2) #Merge should reduce 3 set to 2
        self.assertEqual(self.forest.iterate(), ["Bird", "Cat"]) #The supposed iteration after merge

        #Test if all element in the old set now belong to the new set or not
        for items in self.dogs_entity:
            self.assertEqual(self.forest.find(items), self.cats_entity[0])

    def tearDown(self):
        print("Tearing down......")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
