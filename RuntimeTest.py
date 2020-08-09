'''
    Authors: Jesse-Jackson Zigi
             Bright Okrah Jnr

    This file uses DirectChainingHashTable.py and BSTHashtable.py to run.
    It is a tester file to compare the average runtimes of two different
    collision resolution methods for hashtables. As a result, they both
    do not have a get method as it is of no practical use in comparing
    the insertion runtimes.

    GitHub: https://github.com/ZigiJesse-Jackson/DataStructures2020Summer
'''
from DirectChainingHashTable import HashTable as DHashTable
from BSTHashTable import HashTable as BSTHashTable
import random
import time
from matplotlib import pyplot


def main():
    keys = []  # list of keys for insertion testingpy
    values = []  # list of random values for nodes
    counter = 0
    dTable = DHashTable()
    bstTable = BSTHashTable()
    dTime = 0  # sum of insertion times of direct chaining
    bstTime = 0  # sum of insertion times of bst chaining
    dAvgs = []  # holds average insertion time after every 1024th insertion
    bstAvgs = []  # holds average insertion time after every 1024th insertion

    for i in range(8192):
        keys.append(random.randrange(16384, 65536))
        values.append(random.randrange(16384, 65536))

    while counter < 8192:
        if counter % 1024 == 0:
            dAvgs.append(dTime/1024)
            bstAvgs.append(bstTime/1024)
            dTime = 0
            bstTime = 0
        dStart = time.time()
        dTable.add(keys[counter], values[counter])
        dEnd = time.time()
        dTime += dEnd-dStart

        bstStart = time.time()
        bstTable.add(keys[counter], values[counter])
        bstEnd = time.time()
        bstTime += bstEnd - bstStart
        counter += 1


    x = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192]
    #x = [1, 2, 3, 4, 5, 6, 7, 8]
    y1 = dAvgs
    y2 = bstAvgs
    pyplot.plot(x, y1, 'r-', label='Direct Chaining Average time')
    pyplot.plot(x, y2, 'b-', label='BST average time')
    pyplot.xlabel("Number of insertions")
    pyplot.ylabel("Runtimes in seconds")
    pyplot.title("Average runtime after every 1024 insertions insertions")
    pyplot.legend()
    pyplot.show()

main()




