from collections import deque



class Stack:
  """Custom class that use python deque for internal implementation that provides a generic interface for deque"""

    def __init__(self) -> None:
        self._stack = deque()

    def push(self, obj) -> None:
        self._stack.append(obj)

    def pop(self):
        try:
            return self._stack.pop()

        except IndexError:
            return None

    def __len__(self):
        return len(self._stack)

    def isEmpty(self) -> bool:
        return len(self._stack) == 0
