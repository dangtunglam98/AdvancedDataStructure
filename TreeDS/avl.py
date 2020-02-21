from bst import TreeMap


class AVLTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        def __init__(self, element, parent=None, left=None, right=None):
                super().__init__(element, parent=parent, left=left, right=right)
                self._height = 0
        
        def get_left_height(self):
            if self._left == None:
                return 0
            return self._left._height
        
        def get_right_height(self):
            if self._right == None:
                return 0
            return self._right._height

#----------------------------------------------------------------Non-public Mutator--------------------------------------
    def _is_node_balanced(self, p):
        if abs(p._node.get_left_height() - p._node.get_right_height()) > 1:
            return False
        return True


    def _calculate_height(self, p):
        p._node._height = 1 + max(p._node.get_left_height(),p._node.get_right_height())


    def _assign_node_height(self,p):
        if p != None:
            self._assign_node_height(self.left(p))
            self._assign_node_height(self.right(p))
            self._calculate_height(p)
    

    def _is_tree_balanced(self, p):
        if p == None:
            return True
        if self._is_node_balanced(p) is True and self._is_tree_balanced(self.left(p)) is True and self._is_tree_balanced(self.right(p)) is True:
            return True

        return False
    

    def _link_parent_child(self, parent, child, toLeft):
        if toLeft:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent
    
    def _child_to_parent(self, grandparent, parent, child):
        if grandparent == None:
            self._root = child
            child._parent = None
        else:
            if parent == grandparent._left:
                self._link_parent_child(grandparent, child, True)
            else:
                self._link_parent_child(grandparent, child, False)
    
    def _parent_to_left_child(self, parent, child):
        self._link_parent_child(parent, child._left, False)
        self._link_parent_child(child, parent, True)
    
    def _parent_to_right_child(self, parent, child):
        self._link_parent_child(parent, child._right, True)
        self._link_parent_child(child, parent, False)

    def _left_rotation(self, p):
        x = p._node
        y = x._parent
        z = y._parent
        self._child_to_parent(z, y, x)
        self._parent_to_left_child(y, x)

    def _right_rotation(self, p):
        x = p._node
        y = x._parent
        z = y._parent
        self._child_to_parent(z, y, x)
        self._parent_to_right_child(y, x)

    def _left_right_rotation(self, p):
        self._left_rotation(p)
        self._right_rotation(p)

    def _right_left_rotation(self, p):
        self._right_rotation(p)
        self._left_rotation(p)

    def _trinode_restructure(self,x):
        y = self.parent(x)
        z = self.parent(y)

        if self.left(z) == y:
            if self.left(y) == x:  #Right-Right Rotation
                self._right_rotation(y)
            elif self.right(y) == x: #Left-Right Rotation
                self._left_right_rotation(x)
        
        elif self.right(z) == y:
            if self.right(y) == x:  #Left-Left Rotation
                self._left_rotation(y)
            elif self.left(y) == x:  #Right-Left Rotation
                self._right_left_rotation(x)

    def _tall_child(self, p):
        if p._node.get_left_height() > p._node.get_right_height():
            return self.left(p)
        elif p._node.get_left_height() < p._node.get_right_height():
            return self.right(p)
        else:
            parent_of_p = self.parent(p)
            if parent_of_p == None:
                return None
            else:
                if parent_of_p._node._left == p:
                    return self.left(p)
                else:
                    return self.right(p)

    def _tall_grandchild(self, p):
        return self._tall_child(self._tall_child(p))

    def _rebalance(self, p):
        notBalanced = True
        while notBalanced:
            old_height = p._node._height
            if self._is_node_balanced(p) == False:
                self._trinode_restructure(self._tall_grandchild(p))
                if self.left(p) != None:
                    self._calculate_height(self.left(p))
                if self.right(p) != None:
                    self._calculate_height(self.right(p))
            self._calculate_height(p)
            if p._node._height == old_height:
                notBalanced = False
            else:
                p = self.parent(p)
                if p is None:
                    break
    
#----------------------------------------------------------Public Mutators---------------------------------------------
    def __getitem__(self, k):
        return super().__getitem__(k)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        p = self.__getitem__(key)
        self._rebalance(p)
        
    def set_item_bst(self,key, value):
        super().__setitem__(key, value)

    def __delitem__(self, k):
        if self.root() == None:
            return None
        p = self.__getitem__(k)
        if p == None:
            raise KeyError("Key Not Found")
        else:
            parent_of_p = self.parent(p)
            super().__delitem__(k)
            self._rebalance(parent_of_p)

    
    def assign_tree_height(self):
        if self.root() == None:
            raise ValueError("Empty Tree")
        else:
            self._assign_node_height(self.root())


    def is_balanced(self):
        if self.root() == None:
            return True
        else:
            return self._is_tree_balanced(self.root())

    def __iter__(self):
        return super().__iter__()