from CustomLibraries import PriorityQueue, LinkedQueue


class TaskProcessor:

    A_time = 2 # allocated time for tasks in queue A
    B_time = 4 # allocated time for tasks in queue B
    C_time = float('inf')
    


    class _Task:
    
        def __init__(self, task_id, total_work_needed, arrival_time):
            self._id : int | str = task_id # the id of the work
            self._total_work_needed: int = total_work_needed # The total work needed
            self._arrival_time = arrival_time # the arrival time of the task
            self._remaing_work = total_work_needed # the remaining work left
            self._due_work = 2 # allowed amount of work. depends on the tier the task belongs to
            self._tier = TaskProcessor.A_time # Type of tier
            

        def key(self) -> int:
            return self._arrival_time

        def arrival_time(self) -> int:
            return self.arrival_time

        def __str__(self):
            return f"{self._id} (Remaining: {self._remaing_work})"


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
        self._pending_area: PriorityQueue = PriorityQueue(TaskProcessor.min_priority_function) # pending area
        self._queue_list: list[LinkedQueue] = [LinkedQueue() for _ in range(3)] # QueueA is store at index 0, QueueB at 1, and so on.
        self._current_task: TaskProcessor._Task | None = None # The current task being processed
        self._current_task_tier = None # the tier of the current task being processed

    def schedule_task(self, task_id:str | int, total_work_needed: int, arrival_time: int):
        # create an object for the task
        task = TaskProcessor._Task(task_id, total_work_needed, arrival_time)
        self._add_task_to_pending_area(task)

    def _add_task_to_pending_area(self, task: TaskProcessor._Task):
        self._pending_area.enqueue(task)


    def _tick(self):
        # advance the system clock by 1 unit
        self._advance_sys_clock(1)

        # check for arriving tasks (Pending -> Queue A)
        self.check_for_arriving_tasks()


        # get the selected task
        self.get_selected_task()

        if selected_task is not None:
            self._run_task(1)

    def _advance_sys_clock(self, unit: int):
        self._system_clock += unit

    def status(self):
        # print the contents of all 3 queues, system time and the pending area
        pass

    def check_for_arriving_tasks(self):
        # get a reference for the top most task from the pending area
        top = self._pending_area.peek()
        queue_A = self._queue_list[0]

        while top is not None:
            if top.arrival_time() <= self._system_clock:
                # add the task to queue A
                queue_A.enqueue(self._pending_area.dequeue())
                top = self._pending_area.peek()

            else:
                break

    def get_selected_task(self):
        if self._current_task is None:
            for task in self._queue_list:
                if task.peek() is not None:
                    self._current_task = task.dequeue()
                    break
                
    def _run_task(self, time:int):
        self._current_task._remaing_work -= 1
        self._current_task._due_work -= 1

        if self._current_task._due_work == 0 and self._current_task._remaing_work > 0:
            match self._current_task._tier:
                case TaskProcessor.A_time:
                    self._current_task._tier = TaskProcessor.B_time
                    self._current_task._due_work = (TaskProcessor.B_time if
                                                self._current_task._remaing_work > TaskProcessor.B_time else self._current_task)
                case TaskProcessor.B_time:
                    self._current_task._tier = TaskProcessor.C_time
                    self._current_task._due_work = self._current_task._remaing_work
        elif self._current_task == 0 and self._current_task._remaing_work == 0:
            self._current_task = None



    def status(self):
        print(self._system_clock)
        print("Pending: ", [t.to_str() for t in self._pending_area])
        print("Queue A"), [t.to_str() for t in self._queue_list[0]]
        print("Queue B"), [t.to_str() for t in self._queue_list[1]]
        print("Queue C"), [t.to_str() for t in self._queue_list[2]]
        print(f"Processing {self._current_task._id}")


        