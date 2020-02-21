from avl import AVLTreeMap
from bst import TreeMap

class SplayTree(AVLTreeMap, TreeMap):
    class _Node(TreeMap._Node):
        def __init__(self, element, parent=None, left=None, right=None):
                super().__init__(element, parent=parent, left=left, right=right)

    def _zig_zig(self, p):
        parent_p = self.parent(p)
        self._right_rotation(parent_p)
        self._right_rotation(p)
    
    def _zig_zag(self, p):
        self._right_rotation(p)
        self._left_rotation(p)
    
    def _zag_zig(self, p):
        self._left_rotation(p)
        self._right_rotation(p)

    def _zag_zag(self, p):
        parent_p = self.parent(p)
        self._left_rotation(parent_p)
        self._left_rotation(p)

    def _has_parent(self,p):
        return self.parent(p) != None
    
    def _has_grandparent(self,p):
        return self.parent(self.parent(p)) != None

    def _is_left_child(self, p):
        parent_of_p = self.parent(p)
        if self.left(parent_of_p) == p:
            return True
        else:
            return False

    def _is_zig_case(self, p):
        parent_p = self.parent(p)
        grandparent_p = self.parent(parent_p)
        return grandparent_p == None and self._is_left_child(p)

    def _is_zag_case(self, p):
        parent_p = self.parent(p)
        grandparent_p = self.parent(parent_p)
        return grandparent_p == None and not self._is_left_child(p)

    def _is_zig_zig_case(self, p):
        parent_p = self.parent(p)
        grandparent_p = self.parent(parent_p)
        return  self._is_left_child(parent_p) and self._is_left_child(p)

    def _is_zag_zag_case(self, p):
        parent_p = self.parent(p)
        grandparent_p = self.parent(parent_p)
        return not self._is_left_child(p) and not self._is_left_child(parent_p)

    def _is_zig_zag_case(self, p):
        parent_p = self.parent(p)
        grandparent_p = self.parent(parent_p)
        return not self._is_left_child(parent_p) and self._is_left_child(p)

    def _is_zag_zig_case(self, p):
        parent_p = self.parent(p)
        grandparent_p = self.parent(parent_p)
        return self._is_left_child(parent_p) and not self._is_left_child(p)

    def _splay(self, p):
        while p != self.root():
            if self._has_parent(p) and not self._has_grandparent(p):
                if self._is_left_child(p):
                    self._right_rotation(p)
                else:
                    self._left_rotation(p)
            elif self._has_grandparent(p):
                if self._is_zig_zag_case(p):
                    self._zig_zag(p)

                elif self._is_zig_zig_case(p):
                    self._zig_zig(p)

                elif self._is_zag_zig_case(p):
                    self._zag_zig(p)

                elif self._is_zag_zag_case(p):
                    self._zag_zag(p)

    
    def __getitem__(self, k):
        if self.root().get_key() == k:
            return self.root()
        else:
            possibleNode = self._search_recur(self.root(), k)
            if possibleNode.get_key() != k:
                self._splay(possibleNode)
                raise KeyError("Key Not Found")
            else:
                self._splay(possibleNode)
                return possibleNode
    
    def __setitem__(self, key, value):
        item = self._Item(key, value)
        if self.root() == None:
            self._add_root(item)
        else:
            possibleNode = self._search_recur(self.root(), key)
            if possibleNode.get_key() == key:
                possibleNode.set_value(value)
                self._splay(possibleNode)
            else:
                if key < possibleNode.get_key():
                    self._add_left(possibleNode, item)
                    self._splay(self.left(possibleNode))
                else: 
                    self._add_right(possibleNode, item)
                    self._splay(self.right(possibleNode))
            
    
    
    def __delitem__(self, k):
        if self.root() == None:
            return None
        splayNode = self._search_recur(self.root(),k)
        if splayNode.get_key() == k:
            parent = self.parent(splayNode)
            self._delete(splayNode)
            self._splay(parent)
        else:
            self._splay(splayNode)