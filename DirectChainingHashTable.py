'''
    Authors: Jesse-Jackson Zigi
             Bright Okrah
'''
import random
from LinkedList import LinkList



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
        if len(skey) >= 3:
            hashk = int(skey[(len(skey)//2)-1:(len(skey)//2)+1]) # retrieve middle values
            return hashk % self._capacity # hash key and return slot position for key
        # If len of key is less than 3, just take numbers and hash
        hashk = int(skey)  # retrieve middle values
        return hashk % self._capacity



    def add(self, key, val):
        index = self.__hash(key)
        if self._table[index] == None:
            self._table[index] = LinkList(val)
            return
        self._table[index].push(val)

    def __len__(self):
        return self.num

    def printIndex(self, key):
        index = self.__hash(key)
        if self._table[index] == None:
            print("None")
            return
        self._table[index].print()

    def printHash(self, key):
        print(self.__hash(key))


table = HashTable()

table.add(65, 34)
table.add(35, 34)
table.add(5, 36)
table.add(4, 38)
table.add(36, 34)
table.add(5, 34)

table.printIndex(4)




