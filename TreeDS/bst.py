from trees import LinkedBinaryTree
from maps import MapBase

class TreeMap(LinkedBinaryTree, MapBase):

    class Position(LinkedBinaryTree.Position):
        def get_key(self):
            return self._node._element._key
        
        def get_value(self):
            return self._node._element._value
        
        def set_value(self, value):
            self._node._element._value = value



    def first(self):
        """Return the Position with the smallest key"""
        if self.root() == None:
            return None
        if self.left(self.root()) == None:
            return self.root
        else:
            return self._get_left(self.root())

    def last(self):
        """Return the Position with the largest key"""
        if self.root() == None:
            return None
        
        if self.right(self.root()) == None:
            return self.root()
        else:
            return self._get_right(self.root()) 

    def after(self, p):
        """Return the position containing the least key that is greater than that of position p"""
        if self.right(p) != None:
            least = self.right(p)
            return self._get_left(least)
        else:
            least = p
            parent = self.parent(p)
            while parent != None and least == self.right(parent):
                least = parent
                parent = self.parent(least)
            return parent

    def before(self, p):
        """Return the position containing the greatest key that is less than that of position p"""
        if self.left(p) != None:
            greatest = self.left(p)
            return self._get_right(greatest)
        else:
            greatest = p
            parent = self.parent(p)
            while parent != None and greatest == self.left(parent):
                greatest = parent
                parent = self.parent(least)
            return parent

    def __getitem__(self, k):
        """Return the Position with the specified key, Error if not found"""
        possibleNode = self._search_recur(self.root(), k)
        if possibleNode.get_key() != k:
            raise KeyError("Key Not Found")
        else:
            return possibleNode
    
    def __setitem__(self, key, value):
        """Insert new Position into Tree or Edit existing Position"""
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
                else: 
                    self._add_right(possibleNode, item)
        
    def __delitem__(self, k):
        """Delete a Position in the Tree"""
        if self.root() == None:
            return None
        else:
            deleteNode = self.__getitem__(k)
            if deleteNode == None:
                raise KeyError("Key Not Found")
            else:
                self._delete_node(deleteNode)

    def __iter__(self):
        self._print_inorder(self.root())

#--------------------------------------nonpublic mutators -----------------------------
    def _delete_node(self, p):
        if self.num_children(p) <= 1:
            self._delete(p)
        else:
            r = self.before(p)
            p._node._element._key = r.get_key()
            p._node._element._value = r.get_value()
            self._delete(r)

    def _print_inorder(self, p):
        if p != None:
            self._print_inorder(self.left(p))
            print("key: " + str(p.get_key()) + "- value: " + str(p.get_value()))
            self._print_inorder(self.right(p))

    def _get_left(self, p):
        if self.left(p) == None:
            return p
        else:
            return self._get_left(self.left(p))
 

    def _get_right(self, p):
        if self.right(p) == None:
            return p
        else:
            return self._get_right(self.right(p))  
    
    def _search_recur(self, p, k):
        if k == p.get_key():
            return p
        elif k < p.get_key() and self.left(p) is not None:
            return self._search_recur(self.left(p), k)
        elif k > p.get_key() and self.right(p) is not None:
            return self._search_recur(self.right(p), k)
        return p

