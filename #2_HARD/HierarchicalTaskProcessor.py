from CustomLibraries import PriorityQueue


class TaskProcessor:

    A_time = 2 # allocated time for tasks in queue A
    B_time = 4 # allocated time for tasks in queue B


    class _Task:
    
        def __init__(self, id, total_work_needed, arrival_time):
            self._id : int | str = id
            self._total_work_needed: int = total_work_needed
            self._arrival_time = arrival_time
            self._remaing_work: total_work_needed 

        def key(self) -> int:
            return self._arrival_time

        def arrival_time(self) -> int:
            return self.arrival_time


    @staticmethod
    def min_priority_function(obj) -> int:
        key: int = obj.key()
        return -key

    @staticmethod
    def max_priority_function(obj) -> int:
        key: int = obj.key()
        return key






    def __init__(self):
        self._system_clock :int = 0
        self._pending_area: PriorityQueue = PriorityQueue(TaskProcessor.min_priority_function)
        
        # QueueA is store at index 0, QueueB at 1, and so on.
        self._queue_list: list[PriorityQueue] = [PriorityQueue(TaskProcessor.min_priority_function) for _ in range(3)]
        self.current_task: TaskProcessor._Task | None = None

    def schedule_task(self, id:str | int, total_work_needed: int, arrival_time: int):
        # create an object for the task
        task = TaskProcessor._Task(id, total_work_needed, arrival_time)
        self._add_task_to_pending_area(task)


    def tick(self):
        # advance the system clock by 1 unit
        self._system_clock += 1

        # check for arriving tasks (Pending -> Queue A)
        self.check_for_arriving_tasks()


        # get the selected task
        selected_task = self.get_selected_task()

        if selected_task is not None:
            self.run_task(selected_task)

    def status(self):
        # print the contents of all 3 queues, system time and the pending area
        pass

    def check_for_arriving_tasks(self):
        # get a reference for the top most task from the queue
        top = self._pending_area.peek()

        while top is not None:
            if top.arrival_time() <= self._system_clock:

                # add the task to queue A
                self._queue_list[0].enqueue(self._pending_area.dequeue())
                top = self._pending_area.pee()
            else:
                break




        