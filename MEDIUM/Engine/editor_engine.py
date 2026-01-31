from .models import Node

class TextEditor:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.cursor = self.tail  
        self.undo_stack = []
        self.redo_stack = []