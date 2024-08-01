from collections import deque

class MyStack:
    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()

    def push(self, x: int) -> None:
        self.que2.append(x)
        while self.que1:
            self.que2.append(self.que1.popleft())
        self.que1, self.que2 = self.que2, self.que1

    def pop(self) -> int:
        return self.que1.popleft()

    def top(self) -> int:
        return self.que1[0]

    def empty(self) -> bool:
        return not self.que1

# Example usage:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
