from avl import AVLTreeMap
from bst import TreeMap

class RedBlackTree(AVLTreeMap, TreeMap):
    class _Node(TreeMap._Node):
        def __init__(self, element, parent=None, left=None, right=None):
                super().__init__(element, parent=parent, left=left, right=right)
                self._color = "RED"
        
        def get_color(self):
            return self._color
        
        def set_color(self, color):
            self._color = color
    
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
        self._trinode_restructure(p)


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
                    self._right_right_rotation(y)
                elif self.right(y) == x: #Left-Right Rotation
                    self._left_right_rotation(x)
            
            elif self.right(z) == y:
                if self.right(y) == x:  #Left-Left Rotation
                    self._left_left_rotation(y)
                elif self.left(y) == x:  #Right-Left Rotation
                    self._right_left_rotation(x)




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
        pass
