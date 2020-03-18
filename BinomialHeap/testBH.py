from BinomialHeap import BinomialHeap
import unittest

class TestBH(unittest.TestCase):
    def setUp(self):
        print("Setting up...")
        self.emptyHeap = BinomialHeap()


        self.testHeap = BinomialHeap()
        keys = [30, 40, 24, 58, 48, 26, 11, 13]
        for item in keys:
            self.testHeap.insert(item, "Success")

    def test_getMin(self):
        #Get Minimum in an empty Heap
        self.assertEqual(self.emptyHeap.find_minimum(), None)

        #Get Minimum in a populated Heap
        self.assertEqual(self.testHeap.find_minimum().get_key(), 11)

    def test_insert(self):
        #Insert into an empty Heap
        self.emptyHeap.insert(100, "Success")
        self.assertEqual(self.emptyHeap.find_minimum().get_key(), 100)

        #Insert into a populated Heap (new Minimum)
        self.testHeap.insert(5, "Success")
        self.assertEqual(self.testHeap.find_minimum().get_key(), 5)

        #Insert into a populated Heap (new Maximum)
        self.testHeap.insert(100, "Success")
        self.assertEqual(self.testHeap.find_minimum().get_key(), 5)
    
    def test_delete(self):
        #Delete a empty Heap
        self.assertEqual(self.emptyHeap.delete_min(), None)

        #Delete a populated Heap
        self.testHeap.delete_min()
        self.assertEqual(self.testHeap.find_minimum().get_key(), 13)

    def test_decrease(self):
        keys = [30, 40, 24, 58, 48, 26, 11, 13,77,66,55,33,44]
        for item in keys:
            self.emptyHeap.insert(item, "Success")
        self.emptyHeap.insert(49, "Failed")
        self.emptyHeap.decrease_key("Failed", 1)
        self.assertEqual(self.emptyHeap.find_minimum().get_key(), 1)


    def tearDown(self):
        print("Tearing down...")
    
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)