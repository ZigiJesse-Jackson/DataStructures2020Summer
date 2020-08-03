
class BinaryNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:

    def __init__(self, data):
        self.root = BinaryNode(data)
        self.leftChild = self.root.left
        self.rightChild = self.root.right

    def push(self, data):
        if self.root.data == None:
            self.root.data = data
            return
        child = self.root
        while True:
            if data > child.data:
                if child.right == None:
                    child.right = BinaryNode(data)
                    return
                child = child.right
            elif data < child.data:
                if child.left == None:
                    child.left = BinaryNode(data)
                    return
                child = child.left
            else:
                return

    def remove(self, data):
        if self.root.data == data:
            self.root.data = None
            return
        child = self.root
        while True:
            if data > child.data and child.right != None:
                if child.right.data == data:
                    child.right = child.right.right
                    return
                child = child.right
            elif data < child.data and child.left != None:
                if child.left == data:
                    child.left = child.left.left
                    return
                child = child.left
            else:
                return



    def print(self, root):
        if root.left is not None:
            self.print(root.left)
        print(root.data)
        if root.right is not None:
            self.print(root.right)



