'''
    Authors: Jesse-Jackson Zigi
             Bright Okrah
'''
import random



class HashTable():
    _capacity = 509
    _table = _capacity * [None]
    _num = 0

    def __init__(self):
        self._capacity = 509
        self._table = self._capacity * [None]
        self.num = 0

    def __hash(self, key):
        key *= key # square key
        skey = str(key) # turn key to string to slice
        hashk = int(skey[(len(skey)//2)-1:(len(skey)//2)+1]) # retrieve middle values
        return hashk % self._capacity # hash key and return slot position for key

    def add(self, key, val):
        index = self.__hash(key)
        if self._table[index] == None:
            self._table[index] = val
            self.num += 1
            # self._num = self._num + 1
        else:
            return

    def get(self, key):
        index = self.__hash(key)
        if self._table[index] != None:
            return self._table[index]
        else:
            return

    def __len__(self):
        return self.num







