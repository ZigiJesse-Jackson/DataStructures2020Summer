
class LinkNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:

    def __init__(self, data):
        self.head = LinkNode(data)

    def push(self, data):
        if self.head.data == None or self.head.data == -1:
            self.head.data = data
            return

        node = self.head
        while node.next != None:
            node = node.next
        node.next = LinkNode(data)
        return

    # Removes first occurence of data item
    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        node = self.head
        while node.next.data != data:
            node = node.next
        node.next = node.next.next
        return

    def print(self):
        node = self.head
        while node.next != None:
            print(node.data, end=" ")
            node = node.next
        print(node.data)
        return






