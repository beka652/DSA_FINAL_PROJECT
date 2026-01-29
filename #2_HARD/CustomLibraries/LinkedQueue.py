class LinkedQueue:
    # -------- Internal node --------- #
    class _node:
        def __init__(self, elem) -> None:
            self._elem = elem
            self._next = None

    # --------------------------------------#

    def __init__(self) -> None:
        self._front: LinkedQueue._node | None = None
        self._rear: LinkedQueue._node | None = None
        self._size: int = 0

    def isEmpty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return self._size

    def enqueue(self, elem) -> None:
        node = LinkedQueue._node(elem)
        if self.isEmpty():
            self._front = self._rear = node
        else:
            self._rear._next = node
            self._rear = node

        self._size += 1

    def dequeue(self):
        if not self.isEmpty():
            node = self._front
            self._size -= 1

            if len(self) == 1:
                self._rear = self._front = None
            else:
                self._front = self._front._next
            return node._elem
        raise Exception("Queue is empty")

    def peek(self):
        if not self.isEmpty():
            return self._front._elem
        return None

    def transform(self, func) -> None:
        curr = self._front
        while curr is not None:
            func(curr._elem)
            curr = curr._next

    def __str__(self):
        if len(self) == 0:
            return "[]"
        cont = []
        curr = self._front

        while curr is not None:
            cont.append(str(curr._elem))
            curr = curr._next

        return " -> ".join(cont)
