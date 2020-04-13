class DJNode:
    def __init__(self, value):
        self._set_name = None
        self._value = value
        self._parent = None

    def set_set_name(self, set_name):
        self._set_name = set_name

    def get_set_name(self):
        return self._set_name

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent
