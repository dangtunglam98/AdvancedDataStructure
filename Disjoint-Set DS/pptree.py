from node import DJNode

class ParentPointTree:
    def __init__(self, set, node):
        node.set_set_name(set)
        self._node = node
        self._tail = node

    def get_tail(self):
        return self._tail

    def set_tail(self, newTail):
        self._tail = newTail

    def get_root(self):
        return self._node

    def insert_to_tree(self, newNode):
        newNode.set_parent(self._tail)
        self.set_tail(newNode)

    def get_set(self):
        return self._node.get_set_name()

    def merge_trees(self, tree):
        tree.get_root().set_set_name(None)
        tree.get_root().set_parent(self._tail)
        self.set_tail(tree.get_tail())
