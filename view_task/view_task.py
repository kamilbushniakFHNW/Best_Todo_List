STATUS_OPEN = "Open"
STATUS_DONE = "Done"


def count_done_subtasks(subtasks):
    """Return how many subtasks have the status Done."""
    done_count = 0
    for subtask in subtasks:
        if subtask["status"] == STATUS_DONE:
            done_count += 1
    return done_count


def format_task_line(number, task):
    """Return one short line for the task list."""
    line = f"{number}. {task['title']} | {task['priority']}"
    line += f" | {task['due_date']}"

    subtasks = task["subtasks"]
    if len(subtasks) > 0:
        done_count = count_done_subtasks(subtasks)
        line += f" | {done_count}/{len(subtasks)} subtasks done"

    return line


def format_task_details(task):
    """Return all details of one task as text."""
    description = task["description"]
    if description == "":
        description = "-"

    details = "\n--- Task details ---\n"
    details += f"Title:       {task['title']}\n"
    details += f"Description: {description}\n"
    details += f"Priority:    {task['priority']}\n"
    details += f"Due date:    {task['due_date']}\n"
    details += f"Status:      {task['status']}\n"

    subtasks = task["subtasks"]
    if len(subtasks) == 0:
        details += "Subtasks:    none\n"
    else:
        done_count = count_done_subtasks(subtasks)
        details += f"Subtasks:    {done_count}/{len(subtasks)} done\n"
        for i in range(len(subtasks)):
            subtask = subtasks[i]
            details += f"    {i + 1}. {subtask['title']}"
            details += f" ({subtask['status']})\n"

    return details


def print_task_group(tasks, status):
    """Print all tasks with the given status.

    Each task keeps its number from the full list, so the numbers stay
    the same in View, Mark as done and Delete.
    """
    print(f"\n=== {status} ===")
    found = False

    for i in range(len(tasks)):
        task = tasks[i]
        if task["status"] == status:
            print(format_task_line(i + 1, task))
            found = True

    if not found:
        print("(no tasks)")


def is_valid_task_number(text, task_count):
    """Return True if text is a whole number between 1 and task_count."""
    if not text.isdigit():
        return False
    number = int(text)
    return 1 <= number <= task_count


def ask_task_number(tasks):
    """Ask for a task number.

    Return the list index, or None if the user just presses Enter.
    """
    prompt = "Task number for details (Enter to go back): "
    answer = input(prompt).strip()

    while answer != "" and not is_valid_task_number(answer, len(tasks)):
        print(f"Task not found. Please enter a number from 1 to {len(tasks)}.")
        answer = input(prompt).strip()

    if answer == "":
        return None
    return int(answer) - 1


def print_all_tasks(tasks):
    """Print all tasks grouped by status. Return False if there are none."""
    if len(tasks) == 0:
        print("\nYou have no tasks yet. Add one with option 1.")
        return False

    print_task_group(tasks, STATUS_OPEN)
    print_task_group(tasks, STATUS_DONE)
    return True


def view_tasks(tasks):
    """Show all tasks and let the user open one task to see its details."""
    has_tasks = print_all_tasks(tasks)
    if not has_tasks:
        return

    index = ask_task_number(tasks)
    if index is not None:
        print(format_task_details(tasks[index]))