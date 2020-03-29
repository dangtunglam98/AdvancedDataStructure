#Refered (But not copied) from Data Structure and Algorithm in Python
#   -On the subject of prime modulo and size of Table 

#ltdang16 - Lam Dang
#Lab 7: Hash Table
#Implementation Hash Table using Bucket List Method as collision handling
#Hierarchy: KeyValuePair -> BucketList -> 

from bucket import BucketList
class HashTable:
    def __init__(self, capacity = 13):
        self._table = [None] * capacity
        self._capacity = capacity
        self._number_entries = 0
        self._empty_slot = 0
        self._million = 200100053  #prime
        self._thousand = 10007

    def compression(self, hash_value):
        mod_million = hash_value % self._million
        mod_thousand = mod_million % self._thousand
        result = mod_thousand % self._capacity
        return result

    
    def hash_function(self, key):
        hash_value = hash(key)
        result = self.compression(hash_value)
        return result
    
    def is_load_balanced(self):
        return (self._number_entries / self._capacity) < 0.6

    def _get_all_value(self):
        all_value = []
        for bucket in self._table:
            if bucket != None:
                all_value += bucket.iter_bucket()
        return all_value

    def __getitem__(self, key):
        index = self.hash_function(key)
        return self._table[index][key]
    
    def __setitem__(self, key, value):
        self._number_entries += 1
        if not self.is_load_balanced():
            self.resize()
        index = self.hash_function(key)
        if self._table[index] == None:
            self._table[index] = BucketList()
        self._table[index][key] = value
    
    def __delitem__(self, key):
        self._number_entries -= 1
        index = self.hash_function(key)
        del self._table[index][key]
        if self._table[index].get_size() == 0:
            self._table[index] = None

    def resize(self):
        self._capacity = self._capacity * 2
        old_entries = self._get_all_value()
        self._table = [None] * self._capacity
        self._number_entries = 0
        for key, value in old_entries:
            self[key] = value

    def shape_of_table(self):
        print(self._capacity)
        current_index = 0
        for bucket in self._table:
            if bucket == None:
                print('Empty Slot index ' + str(current_index))
            else:
                print(bucket.iter_bucket())
            current_index += 1





