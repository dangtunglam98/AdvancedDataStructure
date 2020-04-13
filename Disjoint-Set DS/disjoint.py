from pptree import ParentPointTree

class DisjointSetDS:
    def __init__(self):
        self._roots = []

    def insert_as_new_tree(self,set_name, entity):
        self._roots.append(ParentPointTree(set_name,entity))

    def insert_into_tree(self, entity, existing_root):  #assuming the root definitely exist
        for tree in self._roots:
            if tree.get_root() == existing_root:
                found_tree = tree
        tree.insert_to_tree(entity)

    def merge_trees(self, root1, root2):
        root1_tree_index = None
        root2_tree_index = None
        for index in range(len(self._roots)):
            if self._roots[index].get_root() == root1:
                root1_tree_index = index
            if self._roots[index].get_root() == root2:
                root2_tree_index = index
        tree1 = self._roots[root1_tree_index]
        tree2 = self._roots[root2_tree_index]
        tree1.merge_trees(tree2)
        del self._roots[root2_tree_index]

    def find(self, entity):
        if entity._parent != None:
            entity.set_parent(self.find(entity._parent))
            return self.find(entity._parent)
        return entity

    def iterate(self):
        list_of_sets = []
        for tree in self._roots:
            list_of_sets.append(tree.get_set())

        return list_of_sets
