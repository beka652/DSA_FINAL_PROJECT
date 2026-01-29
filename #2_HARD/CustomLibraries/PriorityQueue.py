class PriorityQueue:
    """
    This class is a concrete implementation of the priority queue ADT.
    It uses a heap as the underlying structure to achive the best overall performance accross all operations

    The class can function both as a max and min heap based on the function provided and hence it is up to the
    user to provide the function that computes the priority

    """

    class QueueException(Exception):
        pass

    def __init__(self, priority_function, cont: list = []) -> None:
        self._size = len(cont)
        self._priority = priority_function  # the function used for calculating the priority of each itme
        self._heap = cont  # the array storing the elements
        if self._heap:
            self._heapify()

    def __len__(self) -> int:
        return self._size

    def peek(self):
        # returns a reference of the highest priority object (None if the queue is empty)
        if len(self) > 0:
            return self._heap[0]
        return None

    def isEmpty(self) -> bool:
        return len(self) == 0

    def _heapify(self) -> None:
        # constructs a valid heap
        last_parent_index = (self._size - 2) // 2

        for i in range(last_parent_index, -1, -1):
            self._bubble_down(i)

    def enqueue(self, obj) -> None:
        # adds an object to the queue
        self._heap.append(obj)
        self._size += 1
        self._bubble_up(len(self) - 1)

    def _bubble_up(self, index: int) -> None:
        # positions the object with the given index to its rightful place within the queue/ heap.

        new_item = self._heap[index]

        while index > 0:
            parent_index = (index - 1) // 2
            parent = self._heap[parent_index]

            if self._priority(new_item) > self._priority(parent):
                self._heap[index] = parent
                index = parent_index
            else:
                break

        self._heap[index] = new_item

    def dequeue(self):
        # removes the object with the highest priority from the queue and returns it (else raises an error if the queue is empty)
        if len(self) == 1:
            self._size -= 1
            return self._heap.pop()
        elif len(self) > 1:
            high = self._heap[0]
            self._heap[0] = self._heap.pop()
            self._size -= 1
            self._bubble_down(0)
            return high

        raise self.QueueException("Cannot dequeue from an empty queue")

    def _bubble_down(self, index: int) -> None:
        # positions the object with the given index to its rightful place within the queue/ heap.
        elem = self._heap[index]

        while True:
            high_priority_child_index = self._highest_priority_child_index(index)

            if high_priority_child_index == -1:
                break
            else:
                high_priority_child = self._heap[high_priority_child_index]

                if self._priority(high_priority_child) > self._priority(elem):
                    self._heap[index] = high_priority_child
                    index = high_priority_child_index
                else:
                    break

        self._heap[index] = elem

    def _highest_priority_child_index(self, parent_index: int) -> int:
        # returns the index of the child with the highest priority given the index of the parent (if the parent is a leaf node it returns -1)

        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2
        last_index = len(self) - 1

        if left_child_index > last_index:
            return -1
        elif right_child_index > last_index:
            return left_child_index
        else:
            left_priority = self._priority(self._heap[left_child_index])
            right_priority = self._priority(self._heap[right_child_index])

            return (
                left_child_index
                if left_priority > right_priority
                else right_child_index
            )

    def transform(self, func) -> None:
        for i in self._heap:
            func(i)

    def __str__(self):
        return str(self._heap)
