from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:

        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        if self.q1:
            return self.q1.popleft()

    def top(self) -> int:
        if self.q1:
            return self.q1[0]
        return -1

    def empty(self) -> bool:
        return len(self.q1) == 0

    def size(self):
        return len(self.q1)


if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())

    print("current size: ", s.size())
