"""

Linked list is a form of sequential collection, and it doesn't have to be in order
A linked list is made up of independent nodes that may contain any type of data
and each node has a reference to the next in the link

"""



class Node:

    def __int__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# __str__() method returns a human-readable string representation of an object/
    def __str__(self):
        return str(self.data)
class LinkedList:

    def __int__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = []
        

