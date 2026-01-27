


class LinkedQueue:

    class _node:
        def ___init__(self,elem: None) -> None:
            self.elem = elem
            self.next = None




    def __init__(self) -> None:
        self.front: LinkedQueue._node | None =  None
        self.rear: LinkedQueue._node | None = None
        self._size: int = 0

    def isEmpty(self) -> bool:
        return len(self)==0

    def __len__(self) -> int:
        return self._size

    def enqueue(self, elem) -> None:
        _node = LinkedQueue._node(elem)
        
        if self.isEmpty():
            self.front = self.rear = _node
        else:
            self.rear.next = _node
            rear = node

        self._size +=1

    def dequeue(self):
        if not self.isEmpty():
            _node = self.front
            if len(self) == 1:
                self.rear = self.front = None
            else:
                self.front = self.front.next
            return _node.elem
        raise Exception("Queue is empty")
    
    def peek(self):
        if not self.isEmpty():
            return self.front.elem
        return None

    def transform(self, func) -> None:
        curr = self.front
        while curr is not None:
            func(curr.elem)
            curr = curr.next


    def __str__(self):
        cont = []
        curr = self.front
        while curr is not None:
            cont.append(curr.elem)
        
        return ' -> '.join(cont)

    
