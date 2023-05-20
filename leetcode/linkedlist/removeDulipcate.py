"""

remove duplicate from a given linked list


We can use set to remove duplicates

"""

from Linkedlist import LinkedList

def removeDuplicate(l1):
    if l1.head is None:
        return l1
    visited = set()
    currentNode = l1.head
    visited.add(currentNode.value)
    while currentNode.next:
        if currentNode.next.value in visited:
            currentNode.next = currentNode.next.next
        else:
            visited.add(currentNode.next.value)
            currentNode = currentNode.next
    return l1

## with out any extra memory

def removeDupicatesWithOutAnyMemory(l1):
    if l1.head is None:
        return
    currentNode = l1.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return l1.head




