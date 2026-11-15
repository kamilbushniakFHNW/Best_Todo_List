from view_task.view_task import (
    STATUS_DONE,
    count_done_subtasks,
    is_valid_task_number,
    print_all_tasks,
)
from subtask.subtask import ask_yes_no
from datetime import date

def ask_task_to_mark(tasks):
    """Ask which task to mark as done.

    Return the list index, or None if the user just presses Enter.
    """
    prompt = "Task number to mark as done (Enter to go back): "
    answer = input(prompt).strip()

    while answer != "" and not is_valid_task_number(answer, len(tasks)):
        print(f"Task not found. Please enter a number from 1 to {len(tasks)}.")
        answer = input(prompt).strip()

    if answer == "":
        return None
    return int(answer) - 1


def count_open_subtasks(task):
    """Return how many subtasks of the task are not done yet."""
    subtasks = task["subtasks"]
    return len(subtasks) - count_done_subtasks(subtasks)


def mark_all_subtasks_done(task):
    """Set the status of every subtask to Done."""
    for subtask in task["subtasks"]:
        subtask["status"] = STATUS_DONE


def mark_task_done(task):
    """Mark one task as done.

    Return True if the task was changed, False if nothing changed.
    """
    if task["status"] == STATUS_DONE:
        print(f"'{task['title']}' is already done. Nothing changed.")
        return False

    open_count = count_open_subtasks(task)
    if open_count > 0:
        print(f"This task still has {open_count} open subtask(s).")
        if not ask_yes_no("Mark them as done too? (yes/no): "):
            print("Nothing changed.")
            return False
        mark_all_subtasks_done(task)

    task["status"] = STATUS_DONE
    task["done_date"] = date.today().strftime("%d.%m.%Y")
    print(f"Task marked as done: {task['title']}")
    return True


def select_task_to_mark_done(tasks):
    """Show all tasks, ask for one and mark it as done."""
    if not print_all_tasks(tasks):
        return

    index = ask_task_to_mark(tasks)
    if index is None:
        return

    if mark_task_done(tasks[index]):
        print_all_tasks(tasks)