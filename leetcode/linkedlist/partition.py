"""
write a code to partition a linked list around value x, such that all nodes
less than x come before all nodes greater than or equal to x

"""


def partition(l1, x):
    currentNode = l1.head
    l1.tail = l1.head

    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.value < x:
            currentNode.next = l1.head
            l1.head = currentNode
        else:
            l1.tail.next = currentNode
            l1.tail = currentNode
        currentNode = nextNode
    if l1.tail.next is not None:
        l1.tail.next = None
