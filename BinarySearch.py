import time
''' Author: Jesse-Jackson Zigi
    Run SearchAlgoTester.py to test binary search'''

def BinarySearch(target, list):
    start = time.time()
    first = 0
    last = len(list)-1
    found = False

    while found == False :
        if first > last:
            if list[first] == target:  # target is found in first position
                found == True
            found == True
            finish = time.time()
            return finish - start

        mid = (first + last) // 2
        if list[mid] == target:  # target found at mid
            found = True

        else:
            if target < list[mid]:  # target is less than item at mid position
                last = mid - 1
            else:
                first = mid + 1  # item is greater than item found at mid position
    finish = time.time()
    return finish-start

