from pair import KeyValuePair

class BucketList:
    def __init__(self):
        self._size = 0
        self._item_list = []

    def __getitem__(self, key):
        for item in self._item_list:
            if item.get_key() == key:
                return item
        return None

    def __setitem__(self, key, value):
        found = 0
        self._size += 1
        for item in self._item_list:
            if item.get_key() == key:
                item.set_value(value)
                found = 1
        if found == 0:
            new_item = KeyValuePair(key, value)
            self._item_list.append(new_item)

    def __delitem__(self, key):
        for item in self._item_list:
            if item.get_key() == key:
                self._item_list.remove(item)
                self._size -= 1
                return
        raise KeyError('Key not existed')

    def get_all(self):
        return self._item_list

    def get_size(self):
        return self._size

    def iter_bucket(self):
        pairs = []
        for item in self._item_list:
            pairs.append((item.get_key(), item.get_value()))
        return pairs
