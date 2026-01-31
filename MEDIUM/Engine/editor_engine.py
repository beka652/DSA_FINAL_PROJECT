from .models import Node, Action
import time

class TextEditor:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.cursor = self.tail  
        self.undo_stack = []
        self.redo_stack = []
    """below this are internal helper """     
    def _insert_node(self, char, position_node):
            new_node = Node(char)
            prev_node = position_node.prev
            
            new_node.next = position_node
            new_node.prev = prev_node
            prev_node.next = new_node
            position_node.prev = new_node
            return new_node
        
    def _remove_node(self, node):
            """Internal helper to remove a specific node."""
            if node.value is None: return None
            p, n = node.prev, node.next
            p.next = n
            n.prev = p
            return node.value

    def _handle_batching(self, action_type, char):
            if self.undo_stack and self.undo_stack[-1].can_batch(action_type):
                self.undo_stack[-1].data.append(char)
                self.undo_stack[-1].timestamp = time.time()
            else:
                new_action = Action(action_type)
                self.undo_stack.append(new_action)