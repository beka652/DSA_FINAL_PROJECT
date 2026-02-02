import time

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Action:
    def __init__(self, action_type):
        self.type = action_type  # 'WRITE' or 'DELETE'
        self.data = []           # List of characters affected
        self.timestamp = time.time()

    def can_batch(self, new_type):
        return self.type == new_type and (time.time() - self.timestamp) < 2.0