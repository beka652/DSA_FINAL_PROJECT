from CustomLibraries.LinkedQueue import LinkedQueue
from CustomLibraries.PriorityQueue import PriorityQueue


class TaskProcessor:
    A_tier = 2  # allocated time for tasks in queue A
    B_tier = 4  # allocated time for tasks in queue B
    C_tier = float("inf")

    #  ----------------- Private class to represent each task -------------- #
    class _Task:
        def __init__(self, task_id, total_work_needed, arrival_time):
            self._id: int | str = task_id  # the id of the work
            self._arrival_time = arrival_time  # the arrival time of the task
            self._remaining_work = total_work_needed  # the remaining work left
            self._allowed_time_per_tier = 2  # Amount of remaining work
            self._tier = TaskProcessor.A_tier  # Type of tier
            self._waiting_time = 0

        def key(self) -> int:
            return self._arrival_time

        def arrival_time(self) -> int:
            return self._arrival_time

        def __str__(self):
            return f"{self._id}, (Remaining: {self._remaining_work})"

        def __repr__(self):
            return f"{self._id}, (Remaining: {self._remaining_work})"

    # --------------------------- end of Task class ----------------------------------------------#

    @staticmethod
    def min_priority_function(obj) -> int:
        key = obj.key()
        return -key

    @staticmethod
    def max_priority_function(obj) -> int:
        key = obj.key()
        return key

    def __init__(self):
        self._system_clock = 0

        self._pending_area = PriorityQueue(
            TaskProcessor.min_priority_function
        )  # pending area

        self._list = [
            LinkedQueue() for _ in range(3)
        ]  # QueueA is store at index 0, QueueB at 1, and so on.

        self._current_task = None  # The current task being processed

    def schedule_task(self, task_id: str | int, total_work: int, arrival_time: int):
        # create an object for the task
        task = TaskProcessor._Task(task_id, total_work, arrival_time)

        
        self._add_task_to_pending_area(task)

    def _add_task_to_pending_area(self, task: TaskProcessor._Task):
        self._pending_area.enqueue(task)

    def tick(self):
        

        # check for arriving tasks (Pending -> Queue A)
        self._check_for_arriving_tasks()

        # get the selected task
        self._set_current_task()

        # advance the system clock by 1 unit
        self._advance_sys_clock(1)

        self._run_task()

        self._age_checker()

        

    def _advance_sys_clock(self, unit: int):
        self._system_clock += unit

    def _check_for_arriving_tasks(self):
        # get a reference for the top most task from the pending area
        top = self._pending_area.peek()
        queue_A = self._list[0]

        while top is not None:
            if top.arrival_time() <= self._system_clock:
                # add the task to queue A
                new_task = self._pending_area.dequeue()
                queue_A.enqueue(new_task)

                top = self._pending_area.peek()

            else:
                break

    def _set_current_task(self):
        if self._current_task is None:
            for queue in self._list:
                if queue.peek() is not None:
                    self._current_task = queue.dequeue()
                    break

    def _run_task(self):
        if self._current_task is not None:
            self._current_task._remaining_work -= 1
            self._current_task._allowed_time_per_tier -= 1

            if self._current_task._remaining_work == 0:
                self._current_task = None
            elif self._current_task._allowed_time_per_tier == 0:
                match self._current_task._tier:
                    case TaskProcessor.A_tier:
                        self._current_task._tier = TaskProcessor.B_tier
                        self._current_task._allowed_time_per_tier = 4
                        self._list[1].enqueue(self._current_task)  # Add to Queue B
                    case TaskProcessor.B_tier:
                        self._current_task._tier = TaskProcessor.C_tier
                        self._current_task._allowed_time_per_tier = (
                            self._current_task._remaining_work
                        )
                        self._list[2].enqueue(self._current_task)

                self._current_task = None

    def _age_checker(self):
        queue_c = self._list[2]

        # function for incrementing the waiting time of a task
        def incrememt_wait_time(task):
            task._waiting_time += 1

        # Increment the waiting time of the tasks in queue c
        queue_c.transform(incrememt_wait_time)
        task = queue_c.peek()

        while task is not None:
            if task._waiting_time > 15:
                new_task = queue_c.dequeue()
                new_task._tier = TaskProcessor.A_tier
                task._allowed_time_per_tier = 2
                task._waiting_time = 0
                self._list[0].enqueue(task)
                task = queue_c.peek()
            else:
                break

    def status(self):
        print("Time: ", self._system_clock)
        print("Pending: ", self._pending_area)
        print("Queue A: ", self._list[0])
        print("Queue B: ", self._list[1])
        print("Queue C: ", self._list[2])
        print(
            f"Processing: {self._current_task._id, self._current_task._remaining_work}"
        ) if self._current_task is not None else print("Processing : None")


if __name__ == "__main__":
    tp = TaskProcessor()
    # scheduleTask(id, work , arrival)
    tp.schedule_task("T1", 10, 0)
    tp.schedule_task("T2", 4, 2)
    tp.tick()
    tp.tick()
    tp.tick()
    tp.tick()
    tp.tick()
    tp.status()
