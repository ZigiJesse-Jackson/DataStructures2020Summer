'''Author: Jesse-Jackson Zigi
   Assignment 1
   GitHub link: https://github.com/ZigiJesse-Jackson/DataStructures2020Summer
'''

import numpy as np

''' Question 1 '''
def DotProduct(N, ListA, ListB):
    if (len(ListA) and len(ListB)) == N:# Check if both lists are of size N
        print("Generating dot product")
        return sum([x * y for x, y in zip(ListA, ListB)])# Return dot product
    else:
        print("Lists are not of size n")
        return None

''' Helper function to generate lists for question 1'''
def ListGenerator(size):
    return np.random.randint(low=1, high=1001, size=size)# Generate uniform random numbers
                                                         # from 1 to 1000
'''
Test case 1
size = 10
list10 = ListGenerator(size)
list20 = ListGenerator(size)
print(DotProduct(size, list10, list20)

Test case 2
size = 100
list100 = ListGenerator(size)
list200 = ListGenerator(size)
print(DotProduct(size, list100, list200))

'''



''' Question 2'''
'''Helper class for rectangle'''
class Point:
    _X = 0
    _Y = 0

    def __init__(self, X, Y):
        self._X = X
        self._Y = Y

    def getX(self):
        return self._X

    def getY(self):
        return self._Y

'''Rectangle Class'''
class Rectangle:
    _topRight = Point(0,0)
    _bottomLeft = Point(0,0)

    #Checks to see if points are valid for a rectangle before instantiating
    def __init__(self,topRight, bottomLeft):
        if (topRight.getX() > bottomLeft.getX()) and (topRight.getY() > bottomLeft.getX()):
            self._topRight = topRight
            self._bottomLeft = bottomLeft

        elif (topRight.getX() < bottomLeft.getX()) and (topRight.getY() < bottomLeft.getX()):
            print("Correcting error: swapping bottomLeft , topRight values")
            self._topRight, self._bottomLeft = bottomLeft, topRight

    def get_topRight(self):
        return self._topRight

    def get_bottomLeft(self):
        return self._bottomLeft

#Method to return area of rectangle
    def getArea(self):
        length = self._topRight.getY() - self._bottomLeft.getY()
        width = self._topRight.getX() - self._bottomLeft.getX()
        return length * width

#Method to return perimeter of rectangle
    def getPerimeter(self):
        length = self._topRight.getY() - self._bottomLeft.getY()
        width = self._topRight.getX() - self._bottomLeft.getX()
        return (2 * length) + (2 * width)

#Method to check if an intersection occurs with Rectangle rectangle
    def intersection(self, rectangle):
        selfTopY = self._topRight.getY()
        selfBottomY = self._bottomLeft.getY()
        selfTopX = self._topRight.getX()
        selfBottomX = self._bottomLeft.getX()

        rectangleTopY = rectangle.get_topRight().getY()
        rectangleBottomY = rectangle.get_bottomLeft().getY()
        rectangleTopX = rectangle.get_topRight().getX()
        rectangleBottomX = rectangle.get_bottomLeft().getX()

        #Check if other rectangle's biggest y-coord is between self's two
        if (selfTopY > rectangleTopY) and (rectangleTopY > selfBottomY):
            if (selfTopX > rectangleTopX or rectangleTopX > selfTopX) and (rectangleTopX > selfBottomX or selfTopX > rectangleBottomX):
                print("Intersection occurs")
                return True

        elif (rectangleTopY > selfTopY) and (selfTopY > rectangleBottomY):
            if (rectangleTopX > selfTopX or rectangleTopX < selfTopX) and (selfTopX > rectangleBottomX or selfTopX < rectangleBottomX):
                print("Intersection occurs")
                return True

        else:
            print("No intersection")
            return False
'''
topR = Point(10,10)
bottomL = Point(1,1)
OtopR = Point(4,9)
ObottomL = Point(2, 3)

rec = Rectangle(topR, bottomL)
otherRec = Rectangle(OtopR, ObottomL)
print('Rectangle Perimeter: ', rec.getPerimeter())
print('Other Rectangle Perimeter: ', otherRec.getPerimeter())
print('Rectangle Area: ', rec.getArea())
print('Other Rectangle Area: ', otherRec.getArea())
rec.intersection(otherRec)
'''

