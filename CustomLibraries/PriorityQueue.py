class PriorityQueue:
    """
    This class is a concrete implementation of the priority queue ADT.
    It uses a heap as the underlying structure to achive the best overall performance accross all operations

    Objects enqueue to this queue must have a method called get_key that returns the objects priority and all
    methods are based on the assumption all elements of the queue implement this method.

    The queue functions as a max heap by default by can be change to to behave as a min heap during initialization by passing 
    in a different function that computes the priority

    """

    class QueueException(Exception):
        pass

    def __init__(self, priority_function, iter: list = []) -> None:

        self._size = len(iter)
        self._priority = priority_function
        self._heap = iter
        if self._heap:
            self._heapify()
            



    def _heapify(self) -> None:
  
        last_parent_index = (self._size - 2) // 2

        for i in range(last_parent_index,-1,-1):
            self._bubble_down(i)


    def enqueue(self, obj) -> None:
        self._heap.append(obj)
        self._size +=1
        self._bubble_up(self._size -1)


    def _bubble_up(self, index: int) -> None:

        new = self._heap[index]

        while index > 0:
            parent_index = (index -1) // 2
            parent = self._heap[parent_index]

            if self._priority(new) > self._priority(parent):
                self._heap[index] = parent
                index = parent_index
            else:
                break

        self._heap[index] = new


    def dequeue(self):
        if self._heap:
            high = self._heap[0]
            self._heap[0] = self._heap.pop()
            self._size -= 1
            self._bubble_down(0)
            return high

        raise self.QueueException("Cannot dequeue from an empty queue")

    
    def _bubble_down(self, index: int) -> None:
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
        left_child_index = 2 * parent_index + 1
        right_child_index = 2* parent_index + 2
        last_index = self._size -1

        if left_child_index > last_index:
            return -1
        elif right_child_index > last_index:
            return left_child_index
        else:
            left_priority = self._priority(self._heap[left_child_index])
            right_priority = self._priority(self._heap[right_child_index])

            return left_child_index if left_priority > right_priority else right_child_index



    def print(self):
        print(self._heap)



if __name__ == '__main__':

    pq = PriorityQueue(priority_function=lambda x: -x)

    import random


    for x in range(7):
        pq.enqueue(random.randint(-100, 100))


    pq.print()

    pq.dequeue()

    pq.print()


    



    