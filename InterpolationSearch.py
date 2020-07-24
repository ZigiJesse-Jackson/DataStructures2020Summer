import time
''' Author: Jesse-Jackson Zigi
    Run SearchAlgoTester.py to test interpolation search'''

def InterpolationSearch(target, list):
    start = time.time()
    low = 0
    mid = 0
    high = len(list) - 1
    found = False

    while found == False and mid < high:

        if low > high:
            if list[low] == target:  # target is found in first position
                found == True
            found == True
            finish = time.time()
            return finish - start

        mid = low + (((high - low)  // (list[high] - list[low])) * (target - list[low]))

        if list[mid] == target:  # target is found in probe position
            found = True

        else:
            if target < list[mid]:  # target is less than item at probe position
                high = mid - 1
            else:  # item is greater than item found at mid position
                low = mid + 1
    finish = time.time()
    return finish - start

