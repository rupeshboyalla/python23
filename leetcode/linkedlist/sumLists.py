"""

you have two numbers represented by a linked list, where each node contains a single digit
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
write a function that adds the two numbers and returns the sum as a linked list


l1 = 7 -> 1 -> 6        617
l2 = 5 -> 9-> 2    ----> 295 -----> 617+295 = 912 ---> sumList = 2 -> 1 -> 9

"""

from Linkedlist import LinkedList
def sumOfLinkedList(l1, l2):
    n1 = l1.head
    n2 = l2.head
    carry = 0
    resultLL = LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        resultLL.add(int(result % 10 ))
        carry = result / 10
    return  resultLL
