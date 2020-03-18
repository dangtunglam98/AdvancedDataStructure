class BinomialTree:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self.children = []
        self._order = 0
        self._parent = None

    def set_key(self, key):
        self._key = key

    def set_value(self, value):
        self._value = value

    def get_key(self):
        return self._key

    def get_value(self):
        return self._value

    def get_order(self):
        return self._order

    def set_order(self, order):
        self._order = order

    def increase_order(self):
        self._order += 1

    def set_parent(self, parent):
        self._parent = parent

    def add_children(self, tree):
        tree.set_parent(self)
        self.children.append(tree)
        self.increase_order()

    def get_children(self):
        return self.children

    def get_number_children(self):
        return len(self.children)
    
    def find_value_tree(self, value):
        if self._value == value:
            return self
        else:
            for children in self.get_children():
                return children.find_value_tree(value)
        return None


    def swap_up(self):
        if self._parent == None:
            return
        else:
            while self._parent != None and self._key < self._parent._key:
                self._parent._key, self._key = self._key, self._parent._key
                self._parent._value, self._value = self._value, self._parent._value
                self = self._parent

