class Node:
    def __int__(self, data ):
        self.data = data
        self.next = None

class Stack:

    def __int__(self):
        self.head = None

    def isEmpty(self):
        if self.head:
            return True
        else:
            return False
    def push(self, data):
        if self.head:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        else:
            popNode = self.head
            self.head = self.head.next
            popNode.next = None
            return popNode.data
    def peek(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        else:
            return self.head.data
    def display(self):

        iternode = self.head
        if self.isEmpty():
            raise Exception("stack is empty")
        while iternode.next is not None:
            print(iternode.data)
            iternode = iternode.next



if __name__ == "__main__":
    myStack = Stack()
    myStack.push(3)
    myStack.push(4)
    myStack.push(5)
