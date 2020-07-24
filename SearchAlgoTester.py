from InterpolationSearch import InterpolationSearch
from BinarySearch import BinarySearch
import random
''' Author: Jesse-Jackson Zigi
    GitHub Link: https://github.com/ZigiJesse-Jackson/DataStructures2020Summer
    Run script to test both Interpolation and Binary search'''

#Helper function to generate list with random integers
def ListGenerator(size):
    list = []
    for i in range(size):
        list.append(random.randint(1, 32767))
    return list

def main():
    print("Test cases: ")
    print("1. 100 numbers")
    print("2. 1000 numbers")
    print("3. 5000 numbers")
    print("4. Exit")
    answer = int(input("Enter a test case option >> "))
    bsAvg = 0
    isAvg = 0

    while answer != 4:
        if answer == 1:
            list = sorted(ListGenerator(101))
            for i in range(5):
                number = random.randint(1, 32767)
                bsAvg += BinarySearch(number, list)
                isAvg += InterpolationSearch(number, list)
            print("Binary Search average time: ", bsAvg/5)
            print("Interpolation Search average time: ", isAvg / 5)
            print("Test cases: ")
            print("1. 100 numbers")
            print("2. 1000 numbers")
            print("3. 5000 numbers")
            print("4. Exit")
            answer = int(input("Enter a test case option >> "))

        elif answer == 2:
            list = sorted(ListGenerator(1001))
            for i in range(5):
                number = random.randint(1, 32767)
                bsAvg += BinarySearch(number, list)
                isAvg += InterpolationSearch(number, list)
            print("Binary Search average time: ", bsAvg / 5)
            print("Interpolation Search average time: ", isAvg / 5)
            print("Test cases: ")
            print("1. 100 numbers")
            print("2. 1000 numbers")
            print("3. 5000 numbers")
            print("4. Exit")
            answer = int(input("Enter a test case option >> "))

        elif answer == 3:
            list = sorted(ListGenerator(5001))
            for i in range(5):
                number = random.randint(1, 32767)
                bsAvg += BinarySearch(number, list)
                isAvg += InterpolationSearch(number, list)
            print("Binary Search average time: ", bsAvg / 5)
            print("Interpolation Search average time: ", isAvg / 5)
            print("Test cases: ")
            print("1. 100 numbers")
            print("2. 1000 numbers")
            print("3. 5000 numbers")
            print("4. Exit")
            answer = int(input("Enter a test case option >> "))

    print("\n\t.\n\t.\n\t.\n\n...Exiting...")





main()
