from CustomLibraries import PriorityQueue, LinkedQueue


class TaskProcessor:

    A_tier = 2 # allocated time for tasks in queue A
    B_tier = 4 # allocated time for tasks in queue B
    C_tier = float('inf')
    


    class _Task:
    
        def __init__(self, task_id, total_work_needed, arrival_time):
            self._id : int | str = task_id # the id of the work
            self._arrival_time = arrival_time # the arrival time of the task
            self._remaing_work = total_work_needed # the remaining work left
            self._due_work = 2 # allowed amount of work. depends on the tier the task belongs to
            self._tier = TaskProcessor.A_tier # Type of tier
            self._waiting_time: int= 0
            

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
        self._list: list[LinkedQueue] = [LinkedQueue() for _ in range(3)] # QueueA is store at index 0, QueueB at 1, and so on.
        self._current_task: TaskProcessor._Task | None = None # The current task being processed
    

    def schedule_task(self, task_id:str | int, total_work_needed: int, arrival_time: int):
        # create an object for the task
        task = TaskProcessor._Task(task_id, total_work_needed, arrival_time)
        self._add_task_to_pending_area(task)

    def _add_task_to_pending_area(self, task: TaskProcessor._Task):
        self._pending_area.enqueue(task)


    def tick(self):
        # advance the system clock by 1 unit
        self._advance_sys_clock(1)

        # check for arriving tasks (Pending -> Queue A)
        self.check_for_arriving_tasks()


        # get the selected task
        self.set_current_task()

        if self._current_task is not None:
            self._run_task()

        self._age_checker()

    def _advance_sys_clock(self, unit: int):
        self._system_clock += unit

    def status(self):
        # print the contents of all 3 queues, system time and the pending area
        pass

    def check_for_arriving_tasks(self):
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

    def set_current_task(self):
        if self._current_task is None:
            for queue in self._list:
                if queue.peek() is not None:
                    self._current_task = queue.dequeue()
                    break
                
    def _run_task(self):
        self._current_task._remaing_work -= 1
        self._current_task._due_work -= 1

        if self._current_task._remaing_work == 0:
            self._current_task = None
        elif self._current_task._due_work == 0:
            match self._current_task._tier:
                case TaskProcessor.A_tier:
                    self._current_task._tier  = TaskProcessor.B_tier
                    self._current_task._due_work = 4
                    _list[1].enqueue(self._current_task)
                case TaskProcessor.B_tier:
                    self._current_task._tier = TaskProcessor.C_tier
                    self._current_task._due_work = self._current_task._remaing_work
                    self._list[2].enqueue(self._current_task)

            self._current_task = None


    def _age_checker(self):
        def incrememt_wait_time(task):
            task._waiting_time += 1
        self._list[2].transform(incrememt_wait_time)

        queue_c = self._list[2]
        front = queue_c.peek()

        while peek is not None:
            if peek._waiting_time > 15:
                task = queue_c.pop()
                task._tier = TaskProcessor.A_tier
                task._due_work = 2
                task._waiting_time = 0
                self._list[0].enqueue(task)
                front = queue_c.peek()
            else:
                break



    def status(self):
        print(self._system_clock)
        print("Pending: ", [t.__str__() for t in self._pending_area])
        print("Queue A"), [t.__str__() for t in self._list[0]]
        print("Queue B"), [t.__str__() for t in self._list[1]]
        print("Queue C"), [t.__str__() for t in self._list[2]]
        print(f"Processing {self._current_task._id}")


        