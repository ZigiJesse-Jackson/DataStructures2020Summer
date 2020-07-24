'''Author: Jesse-Jackson Zigi
    Assignment 2
    GitHub Link: https://github.com/ZigiJesse-Jackson/DataStructures2020Summer
'''
import array
import random

''' To initialize a Deque instance, pass the size you would like the
    array to be as an argument. 
    To test simulation cases, run main function.
    '''


class Deque:
    _MaxArraySize = 0
    _array = array.array('i', [0])
    _front = 0  # keeps track of position of front item
    _rear = 0  # keeps track of position of last item
    _size = 0  # keeps track of size of array

    # initializes array with a given capacity limit
    def __init__(self, ArraySize):
        self._MaxArraySize = ArraySize
        self._array = array.array('i', [0] * self._MaxArraySize)
        self._front = 0
        self._rear = 0
        self._size = 0

    # len method overwritten for deque
    # returns len of array/max capacity given
    def __len__(self):
        return len(self._array)

    # method to retrieve number of elements in array
    def get_Size(self):
        return self._size

    # method to check if array is empty
    def isEmpty(self):
        return self._front == self._rear

    # method to check if array is full
    def isFull(self):
        return self._size == self._MaxArraySize

    # method to add to front of array
    def add_Front(self, number):

        n = int(number)
        # check if array is full before adding
        if self.isFull() == True:
            print("Array Full")
            return False

        # check if array is empty, in which case
        # front instance variable remains the same
        elif self.isEmpty():
            self._array[self._front] = n
            self._rear += 1
            self._size += 1
            print("Added to front")
            return True

        self._front -= 1 % self._MaxArraySize
        self._array[self._front] = n
        self._size += 1
        print("Added to front")
        return True

    # method to add to back of array
    def add_Back(self, number):

        n = int(number)
        # check if array is full
        if self.isFull() == True:
            print("Array Full")
            return False
        # check if array is empty, in which case
        # add to front
        elif self.isEmpty():
            self.add_Front(n)
            self._size += 1
            return True
        self._array[self._rear] = n
        self._rear += 1 % self._MaxArraySize
        self._size += 1
        print("Added to back")
        return True

    def remove_Front(self):
        # check if array is empty
        if self.isEmpty():
            print("Deque is empty")
            return
        self._array[self._front] = 0
        self._front += 1 % self._MaxArraySize
        self._size -= 1
        print("Successfully removed")
        return

    def remove_Back(self):
        # check if array is empty
        if self.isEmpty():
            print("Deque is empty")
            return
        self._rear -= 1 % self._MaxArraySize
        self._array[self._rear] = 0
        self._size -= 1
        print("Successfully removed")
        return

    def display(self):
        #print content of array
        print(self._array)

# function to test first case of assignment with relevant
# probabilities
def case1(deque):
    checker = False

    while checker == False:
        number = random.random()

        value = random.randrange(1, 101)

        if number <= 0.1:
            if deque.isFull():
                checker = True
            deque.add_Front(value)

        elif 0.1 < number <= 0.3:
            if deque.isEmpty():
                checker = True
            deque.remove_Front()

        elif 0.3 < number <= 0.4:
            if deque.isFull():
                checker = True
            deque.add_Back(value)

        else:
            if deque.isEmpty():
                checker = True
            deque.remove_Back()

# function to test second case of assignment with relevant
# probabilities
def case2(deque):
    checker = False

    while checker == False:
        number = random.random()

        value = random.randrange(1, 101)

        if number <= 0.1:
            if deque.isFull():
                checker = True
            deque.add_Front(value)

        elif 0.1 < number <= 0.3:
            if deque.isEmpty():
                checker = True
            deque.remove_Back()

        elif 0.3 < number <= 0.4:
            if deque.isFull():
                checker = True
            deque.add_Back(value)

        else:
            if deque.isEmpty():
                checker = True
            deque.remove_Front()

def main():
    deque = Deque(20) # Max capacity of array is made 20



    options = "Enter:\n1. For case 1 with:\n\t Add-to-Front: 10%\n\t Remove-From-Front: 20%\n\t Add-to-Rear: 10%\n\t Remove-From-Rear: 60%\n2. For case 2 with: \n\t Add-to-Front: 10%\n\t Remove-From-Front: 60%\n\t Add-to-Rear: 10%\n\t Remove-From-Rear: 20%\n3. Exit"
    answer = 0
    print("Welcome to the deque ADT implementation simulation")

    while answer != 3:
        # initializing array to hold half capacity
        print("...Initializing deque at half capacity for simulation...")
        for i in range(5):
            deque.add_Front(random.randrange(1, 100))
            deque.add_Back(random.randrange(1, 100))

        print(options)

        answer = int(input("Enter option >> "))
        if answer == 1:
            case1(deque)
            print("\n...Simulation case 1 over...\n")

        elif answer == 2:
            case2(deque)
            print("\n...Simulation case 2 over...\n")


    print("\n...Exited...\n\nThank you for testing")

main()