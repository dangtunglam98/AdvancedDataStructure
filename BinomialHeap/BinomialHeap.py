from BinomialTree import BinomialTree

class BinomialHeap:
    def __init__(self):
        self.binomial_trees = []

    def get_length(self):
        return len(self.binomial_trees)

    def add_tree(self, tree):
        self.binomial_trees.append(tree)

    def get_trees(self):
        return self.binomial_trees

    def find_minimum(self):
        if len(self.binomial_trees) == 0:
            return None
        smallest_node = self.binomial_trees[0]
        for rootNode in self.binomial_trees:
            if rootNode.get_key() < smallest_node.get_key():
                smallest_node = rootNode
        
        return smallest_node

    def insert(self, key, value):
        newBTree = BinomialTree(key, value)
        newBHeap = BinomialHeap()
        newBHeap.add_tree(newBTree)
        self.merge(newBHeap)
    
    def delete_min(self):
        deleteNode = self.find_minimum()
        if deleteNode == None:
            return None
        self.binomial_trees.remove(deleteNode)
        newBHeap = BinomialHeap()
        newBHeap.binomial_trees = deleteNode.get_children()
        self.merge(newBHeap)


    def connect_heap(self, heap):
        self.binomial_trees.extend(heap.get_trees())
        self.binomial_trees.sort(key= lambda bTree: bTree.get_order())

    def _is_last_tree(self, tree):
        return tree == self.binomial_trees[-1]

    def union(self, index, cur_tree, next_tree):
        if cur_tree.get_key() <= next_tree.get_key():
            cur_tree.add_children(next_tree)
            del self.binomial_trees[index+1]
        else:
            next_tree.add_children(cur_tree)
            del self.binomial_trees[index]

    def merge(self, heap):
        self.connect_heap(heap)
        if self.get_length == 0:
            return
    
        index = 0
        while index < self.get_length() - 1:
            cur_tree = self.binomial_trees[index]
            next_tree = self.binomial_trees[index+1]
            
            while cur_tree.get_order() == next_tree.get_order():
                if not self._is_last_tree(next_tree):
                    later_tree = self.binomial_trees[index+2]
                    if next_tree.get_order() == later_tree.get_order():
                        pass
                    else:
                        self.union(index, cur_tree, next_tree)
                        next_tree = later_tree
                else:
                        self.union(index, cur_tree, next_tree)
            
            index+=1
    
    def find_value(self, value):
        for tree in self.get_trees():
            found = tree.find_value_tree(value)
            if found is not None:
                return found                      
        return None
                
    def decrease_key(self, value, new_key):
        found_node = self.find_value(value)
        if found_node == None:
            raise KeyError("No Node with the value was found")
        else:
            found_node.set_key(new_key)
            found_node.swap_up()


        

