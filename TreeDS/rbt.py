from avl import AVLTreeMap
from bst import TreeMap

class RedBlackTreeMap(AVLTreeMap, TreeMap):
    class _Node(TreeMap._Node):
        def __init__(self, element, parent=None, left=None, right=None):
                super().__init__(element, parent=parent, left=left, right=right)
                self._color = "RED"
    
#------------------------------------------utility-------------------------------------------------------
    def _get_color(self, p):
        return p._node._color
        
    def _set_color_red(self, p):
        p._node._color = "RED"

    def _set_color_black(self, p):
        p._node._color = "BLACK"

    def _is_node_red(self, p):
        if p is None:
            return False
        return p._node._color == "RED"
    
    def _is_node_leaf(self,p):
        return self.num_children(p) == 0

    def _swap_elements(self, p , r):
        p._node._element._key = r.get_key()
        p._node._element._value = r.get_value()

    def _replace_and_delete(self, replaceNode, deleteNode):
        self._swap_elements(deleteNode, replaceNode)
        self._delete(replaceNode)

    def _is_red_leaf(self,p):
        return self._is_node_red(p) and self._is_node_leaf(p)

    def _get_child(self, p):
            for child in [self.left(p), self.right(p)]:
                if child is not None:
                    return child
            return None

    def _get_red_child(self, p):
        for child in [self.left(p), self.right(p)]:
            if self._is_node_red(child):
                return child
        return None

    def _change_color(self, p, color):
        if color == "RED":
            self._set_color_red(p)
        else:
            self._set_color_black(p)
#------------------------------------------AVL--------------------------------------------------
    def _trinode_restructure(self,x):
        if x == self.root():
            return
        y = self.parent(x)
        z = self.parent(y)
        if z == None:
            if self.left(y) == x:
                self._right_rotation(x)
            else:
                self._left_rotation(x)
            return x
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

#-----------------------------------------Search------------------------------------------
    def __getitem__(self, key):
        return super().__getitem__(key)
    
#-----------------------------------------Insertion-------------------------------------------
    def _search_recur(self, p, k):
        if k == p.get_key():
            return p
        elif k < p.get_key() and self.left(p) is not None:
            return self._search_recur(self.left(p), k)
        elif k > p.get_key() and self.right(p) is not None:
            return self._search_recur(self.right(p), k)
        return p

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
                    self._rebalance_insert(insertedNode)
                else: 
                    self._add_right(possibleNode, item)
                    insertedNode = self.right(possibleNode)
                    self._rebalance_insert(insertedNode)
    
    def _rebalance_insert(self, p):
        if self.root() == p:
            self._set_color_black(p)
        else:
            parent_p = self.parent(p)
            if self._is_node_red(parent_p):
                uncle_p = self.sibling(parent_p)
                if self._is_node_red(uncle_p):
                    self._handle_red_case(p)
                else:
                    self._handle_black_case(p)
    
    def _handle_red_case(self, p):
        parent = self.parent(p)
        grandparent = self.parent(parent)
        self._set_color_red(grandparent)
        self._set_color_black(self.left(grandparent))
        self._set_color_black(self.right(grandparent))
        self._rebalance_insert(grandparent)

    def _handle_black_case(self, p):
        middle = self._trinode_restructure(p)
        self._set_color_black(middle)
        if self.left(middle) is not None:
            self._set_color_red(self.left(middle))
        if self.right(middle) is not None: 
            self._set_color_red(self.right(middle)) 

#--------------------------------------------Deletion-------------------------------------
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
                        self._set_color_black(self.root())
                else:
                    self._replace_and_delete(replaceNode, deleteNode)
                    self._rebalance_delete(deleteNode)

    def _fix_deficit(self, parent, child):
        if child is None:
            return
        if not self._is_node_red(child):
            red_grandchild = self._get_red_child(child)
            if red_grandchild is None:
                self._set_color_red(child)
                if self._is_node_red(parent):
                    self._set_color_black(parent)
                elif not self.root() == parent:
                    self._fix_deficit(self.parent(parent), self.sibling(parent))
            else:
                old_color = self._get_color(parent)
                middle_node = self._trinode_restructure(child)
                self._change_color(middle_node, old_color)
                self._set_color_black(self.left(middle_node))
                self._set_color_black(self.right(middle_node))
                
        else:
            if self.left(parent) == child:
                self._right_rotation(child)
            else:
                self._left_rotation(child)
            self._set_color_black(child)
            self._set_color_red(parent)
            if parent == self.right(child):
                self._fix_deficit(parent, self.left(parent))
            else:
                self._fix_deficit(parent, self.right(parent))
    
    def _rebalance_delete(self, p):
        if len(self) == 1:
            self._set_color_black(self.root())
        elif p is not None:
            num_child = self.num_children(p)
            if num_child == 1:
                child = self._get_child(p)
                if not self._is_red_leaf(child):
                    self._fix_deficit(p, child)
            elif num_child == 2:
                if self._is_red_leaf(self.left(p)):
                    self._set_color_black(self.left(p))
                else:
                    self._set_color_black(self.right(p))