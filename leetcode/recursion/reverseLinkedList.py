def reverse(self, head):
    # If head is empty or has reached the list end
    if head is None or head.next is None:
        return head

    # Reverse the rest list
    revLinkedList = self.reverse(head.next)

    # Put first element at the end
    head.next.next = head
    head.next = None

    # Fix the header pointer
    return revLinkedList