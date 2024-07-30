class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popnode = self.head
        popnode.next = None
        self.head = self.head.next
        return popnode.data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Current stack:")
stack.display()

print("Popped element:", stack.pop())

print("Stack after popping:")
stack.display()

print("Peek on stack:", stack.peek())
