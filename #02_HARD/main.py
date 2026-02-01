from HierarchicalTaskProcessor import TaskProcessor

tp = TaskProcessor()


def main():
    print("This is a task processor program")

    while (command := get_command()) != "quit":
        print()
        parse_command(command)


def get_command():
    return (
        input(
            """Please enter a command to proceed: enter <help> for help, <quit> to quit\n>> """
        )
        .strip()
        .lower()
    )


def parse_command(command: str):
    parsed_command: list[str] = command.split(" ")
    match parsed_command[0].upper():
        case "SCHEDULE_TASK":
            schedule_task(parsed_command[1:])
        case "TICK":
            tick()
        case "STATUS":
            status()
        case "HELP":
            help()
        case _:
            raise Exception(f"Unkown command {command}.")


def schedule_task(args: list):
    if len(args) == 3:
        args[1] = int(args[1])
        args[2] = int(args[2])
        tp.schedule_task(*args)
        print()
    else:
        raise Exception("Argument length doesn't match")


def tick():
    tp.tick()
    print()


def status():
    tp.status()
    print()


def help():
    print("""\n
    Enter SCHEDULE_TASK <id> <total_work_needed> <arrival time> to schedule a task
    Enter TICK to advance the system's clock by 1 unit
    Enter STATUS to print the status of all the 3 queues and the pending area
    \n""")


if __name__ == "__main__":
    main()
