import time

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Action:
    """Represents a batched group of editor operations."""
    def __init__(self, action_type):
        self.type = action_type  # to indicate whether it is 'WRITE' or 'DELETE'
        self.data = []           # list of characters affected
        self.timestamp = time.time()

    def can_batch(self, new_type):
        """Check if a new keystroke can be added to this batch."""
        return self.type == new_type and (time.time() - self.timestamp) < 2.0