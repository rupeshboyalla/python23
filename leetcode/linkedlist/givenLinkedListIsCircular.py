"""



"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def is_circular(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False



list = LinkedList()
print(list.is_circular())