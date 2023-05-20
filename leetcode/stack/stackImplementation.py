"""
stack have 5 methods
1. push
2. pop
3. is_empty
4. len
5. top

"""
from queue import Empty


class StackImplementation:
    def __int__(self):
        self._data= []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.push(e)
    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data.pop()
    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data[-1]

stack = StackImplementation()
stack.push(10)
len(stack)
stack.push(20)
stack.push(30)
stack.top()