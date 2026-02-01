# Hierarchical Task Processor

A **multi-level feedback queue** task scheduler implemented in Python. Tasks are scheduled across three tiers (A, B, C) with different time slices and aging to prevent starvation. Built with custom **LinkedQueue** (FIFO) and **PriorityQueue** (heap-based) data structures.

## Overview

The processor simulates a hierarchical scheduling system:

- **Pending area** — Tasks wait here until their arrival time; ordered by earliest arrival (min-priority heap).
- **Queue A** — Highest priority; each task gets **2** time units per turn, then demotes to B.
- **Queue B** — Medium priority; each task gets **4** time units per turn, then demotes to C.
- **Queue C** — Lowest priority; tasks run until completion. Tasks waiting **>15** ticks in C are **aged** back to Queue A to avoid starvation.

The CPU runs one task per **tick**; each tick advances the clock, admits newly arrived tasks, selects the next task (A → B → C), runs it for one unit, and applies aging in C.

## Project Structure

```
#2_HARD/
├── main.py                    # Interactive CLI entry point
├── HierarchicalTaskProcessor.py   # TaskProcessor and scheduling logic
├── CustomLibraries/
│   ├── LinkedQueue.py         # FIFO queue (linked list)
│   └── PriorityQueue.py       # Heap-based priority queue
└── README.md
```

## Data Structures

| Component        | Structure        | Role                                                                 |
|-----------------|------------------|----------------------------------------------------------------------|
| Pending area    | `PriorityQueue`  | Min-heap by arrival time; tasks enter the system when clock ≥ arrival. |
| Queue A, B, C   | `LinkedQueue`    | Three FIFO queues; tasks move A → B → C as they use their time slice. |

- **LinkedQueue**: Singly linked list, O(1) enqueue/dequeue/peek, with a `transform(func)` method used for aging in Queue C.
- **PriorityQueue**: Array-based heap with a configurable priority function; used as min-heap (earliest arrival) for the pending area.

## Requirements

- **Python 3.10+** (uses `match`/`case` for command parsing)

## How to Run

From the project root:

```bash
python main.py
```

Or run the processor module directly (includes a short demo):

```bash
python HierarchicalTaskProcessor.py
```

## Commands

| Command | Description |
|--------|-------------|
| `SCHEDULE_TASK <id> <total_work_needed> <arrival_time>` | Add a task. `id` can be string or number; work and arrival are integers. |
| `TICK` | Advance the system clock by 1 and run one unit of the current task. |
| `STATUS` | Print current time, pending area, Queues A/B/C, and the task currently processing. |
| `HELP` | Show available commands. |
| `QUIT` | Exit the program. |

### Example Session

```
>> SCHEDULE_TASK T1 10 0
>> SCHEDULE_TASK T2 4 2
>> TICK
>> TICK
>> STATUS
Time:  2
Pending:  []
Queue A:  ...
Queue B:  ...
Queue C:  ...
Processing: ...
>> QUIT
```

## Scheduling Algorithm (Summary)

1. **Tick**: Clock += 1.
2. **Admit**: Move all tasks from the pending area whose arrival_time ≤ clock into Queue A.
3. **Select**: If no current task, dequeue from the first non-empty queue (A, then B, then C).
4. **Run**: Execute the current task for 1 unit (remaining_work -= 1, allowed_time_per_tier -= 1).
5. **Demote / Complete**: If remaining_work is 0, task is done. If allowed_time_per_tier is 0, move task to the next queue (A→B or B→C) and clear current task.
6. **Aging**: In Queue C, increment waiting time for all tasks; any task with waiting_time > 15 is moved back to Queue A with waiting_time reset.
