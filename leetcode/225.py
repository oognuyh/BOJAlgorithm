"""
    225. Implement Stack using Queues
"""
import collections

class MyStack:
    def __init__(self):
        self.deque = collections.deque()

    def push(self, x: int) -> None:
        self.deque.append(x)

    def pop(self) -> int:
        return self.deque.pop() if self.deque else None

    def top(self) -> int:
        return self.deque[-1] if self.deque else None
        
    def empty(self) -> bool:
        return False if self.deque else True

"""
    - 32 ms 14.2 MB 
"""