from avl import AVLTreeMap
from bst import TreeMap

class RedBlackTreeMap(AVLTreeMap, TreeMap):
    class _Node(TreeMap._Node):
        def __init__(self, element, parent=None, left=None, right=None):
                super().__init__(element, parent=parent, left=left, right=right)
                self._color = "RED"
        
        def get_color(self):
            return self._color
        
        def set_color(self, color):
            self._color = color
    
    #---------------------------------------------------------From AVL Tree -----------------------------------------------
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

    def _left_left_rotation(self,p):
        x = p._node
        y = x._parent
        z = y._parent
        self._left_rotation(p)
        if z == None:
            self._swap_color(x,y)
        else:
            self._swap_color(y,z)
    
    def _right_right_rotation(self,p):
        x = p._node
        y = x._parent
        z = y._parent
        self._right_rotation(p)
        if z == None:
            self._swap_color(x,y)
        else:
            self._swap_color(y,z)

    def _left_right_rotation(self, p):
        self._left_rotation(p)
        self._right_right_rotation(p)

    def _right_left_rotation(self, p):
        self._right_rotation(p)
        self._left_left_rotation(p)

    def _trinode_restructure(self,x):
        y = self.parent(x)
        z = self.parent(y)
        if z == None:
            pass
        else:    
            if self.left(z) == y:
                if self.left(y) == x:  #Right-Right Rotation
                    self._right_rotation(y)
                    return y
                elif self.right(y) == x: #Left-Right Rotation
                    self._left_right_rotation(x)
                    return x
            
            elif self.right(z) == y:
                if self.right(y) == x:  #Left-Left Rotation
                    self._left_rotation(y)
                    return y
                elif self.left(y) == x:  #Right-Left Rotation
                    self._right_left_rotation(x)
                    return x

#-------------------------------------------------------------------------------------------

    def _swap_color(self, p, g):
        p_color = p.get_color()
        g_color = g.get_color()
        p.set_color(g_color)
        g.set_color(p_color)

    def _is_uncle_red(self, p):
        if p == None:  #NULL node are considered Black
            return False
        return p._node.get_color() == "RED"

    def _handle_red_case(self, p):
        p_parent = self.parent(p)
        p_uncle = self.sibling(p_parent)
        p_grandparent = self.parent(p_parent)
        #Color setting
        p_parent._node.set_color("BLACK")
        p_uncle._node.set_color("BLACK")
        p_grandparent._node.set_color("RED")
        self._rebalance(p_grandparent)
            
    def _handle_black_case(self, p):
        middle = self._trinode_restructure(p)
        print(middle)
        middle._node.set_color("BLACK")
        self.left(middle)._node.set_color("RED")
        self.right(middle)._node.set_color("RED")

    def _rebalance(self, p):
        if p == self.root():
            p._node.set_color("BLACK")
        else:
            p_parent = self.parent(p)
            p_uncle = self.sibling(p_parent)
            if p_parent._node.get_color() != "BLACK":
                if self._is_uncle_red(p_uncle):
                    self._handle_red_case(p)
                else:
                    self._handle_black_case(p)

    def _is_node_red(self, p):
        if p is None:
            return False
        return p._node.get_color() == "RED"

    def _swap_elements(self, p , r):
        p._node._element._key = r.get_key()
        p._node._element._value = r.get_value()

    def _get_red_child(self, p):
        for child in [self.left(p), self.right(p)]:
            if self._is_node_red(child):
                return child
        return None

    def _replace_and_delete(self, replaceNode, deleteNode):
        self._swap_elements(deleteNode, replaceNode)
        self._delete(replaceNode)

    def _get_child(self, p):
        for child in [self.left(p), self.right(p)]:
            if child is not None:
                return child
        return None

    def _is_red_leaf(self, p):
        return (self._is_node_red(p)) and (self.num_children(p) == 0)

    def _rebalance_delete(self, p):
        if len(self) == 1:
            self.root()._node.get_color("BLACK")
        elif p is not None:
            num_child = self.num_children(p)
            if num_child == 1:
                child = self._get_child(p)
                if not self._is_red_leaf(child):
                    self._fix_deficit(p, child)
            elif num_child == 2:
                if self._is_red_leaf(self.left(p)):
                    self.left(p)._node.set_color("BLACK")
                else:
                    self.right(p)._node.set_color("BLACK")


    def _fix_deficit(self, parent, child):
        if not self._is_node_red(child):
            red_grandchild = self._get_red_child(child)
            if red_grandchild is not None:
                child._node.set_color("RED")
                if self._is_node_red(parent):
                    parent._node.set_color("BLACK")
                elif not self.root() == parent:
                    self._fix_deficit(self.parent(parent), self.sibling(parent))
            else:
                old_color = parent._node.get_color()
                middle_node = self._trinode_restructure(child)
                middle_node._node.set_color(old_color)
                self.left(middle_node)._node.set_color("BLACK")
                self.right(middle_node)._node.set_color("BLACK")
        else:
            if self.left(parent) == child:
                self._right_rotation(child)
            else:
                self._left_rotation(child)
            child._node.set_color("BLACK")
            parent._node.set_color("RED")

            if parent == self.right(child):
                self._fix_deficit(parent, self.left(parent))
            else:
                self._fix_deficit(parent, self.right(parent))

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        item = self._Item(key, value)
        if self.root() == None:
            self._add_root(item)
        else:
            possibleNode = self._search_recur(self.root(), key)
            if possibleNode.get_key() == key:
                possibleNode.set_value(value)
            else:
                if key < possibleNode.get_key():
                    self._add_left(possibleNode, item)
                    insertedNode = self.left(possibleNode)
                    self._rebalance(insertedNode)
                else: 
                    self._add_right(possibleNode, item)
                    insertedNode = self.right(possibleNode)
                    self._rebalance(insertedNode)

    def __delitem__(self, key):
        if self.root() == None:
            return None
        else:
            deleteNode = self.__getitem__(key)
            if deleteNode == None:
                raise KeyError("Key Not Found")
            else:
                replaceNode = self._subtree_last_node(self.left(deleteNode))
                if replaceNode == None: 
                    self._delete(deleteNode)
                    if self.root() is not None:
                        self.root()._node.set_color("BLACK")
                else:
                    self._replace_and_delete(replaceNode, deleteNode)
                    self._rebalance_delete(deleteNode)

    



        






