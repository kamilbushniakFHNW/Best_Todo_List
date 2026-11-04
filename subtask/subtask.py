from view_task.view_task import (
    STATUS_OPEN,
    STATUS_DONE,
    count_done_subtasks,
    format_task_line,
    is_valid_task_number,
)


def print_tasks_with_subtasks(tasks):
    if len(tasks) == 0:
        print("\nYou have no tasks yet. Add one with option 1.")
        return False

    for status in (STATUS_OPEN, STATUS_DONE):
        print(f"\n=== {status} ===")
        found = False

        for i in range(len(tasks)):
            task = tasks[i]
            if task["status"] == status:
                print(format_task_line(i + 1, task))
                for j in range(len(task["subtasks"])):
                    subtask = task["subtasks"][j]
                    print(f"    {j + 1}. {subtask['title']} ({subtask['status']})")
                found = True

        if not found:
            print("(no tasks)")

    return True


def ask_task_index(tasks, prompt):
    while True:
        number = input(prompt).strip()
        if is_valid_task_number(number, len(tasks)):
            return int(number) - 1
        print("Task not found.")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == "yes":
            return True
        if answer == "no":
            return False
        print("Please enter yes or no.")


def ask_subtask_title():
    while True:
        title = input("Subtask title: ").strip()
        if title != "":
            return title
        print("Title cannot be empty.")


def create_subtask(task, title):
    subtask = {"title": title, "status": STATUS_OPEN}
    task["subtasks"].append(subtask)
    return subtask


def mark_subtask_done(task, index):
    subtask = task["subtasks"][index]
    if subtask["status"] == STATUS_DONE:
        return False
    subtask["status"] = STATUS_DONE
    return True


def print_subtasks(task):
    """Print the subtasks of a task, indented, with a progress count."""
    subtasks = task["subtasks"]
    done_count = count_done_subtasks(subtasks)
    print(f"\n{task['title']} - {done_count}/{len(subtasks)} subtasks done")
    for i in range(len(subtasks)):
        subtask = subtasks[i]
        print(f"    {i + 1}. {subtask['title']} ({subtask['status']})")


def add_subtask(tasks):
    if not print_tasks_with_subtasks(tasks):
        return

    task = tasks[ask_task_index(tasks, "Task number for the subtask: ")]

    while True:
        title = ask_subtask_title()
        create_subtask(task, title)
        print(f"Subtask added: {title}")
        print_subtasks(task)

        if not ask_yes_no("Add another subtask? (yes/no): "):
            return


def select_subtask_to_complete(tasks):
    if not print_tasks_with_subtasks(tasks):
        return

    task = tasks[ask_task_index(tasks, "Task number of the subtask: ")]

    if len(task["subtasks"]) == 0:
        print("This task has no subtasks yet.")
        return

    print_subtasks(task)

    while True:
        while True:
            number = input("Subtask number to mark as done: ").strip()
            if is_valid_task_number(number, len(task["subtasks"])):
                break
            print("Subtask not found.")

        if mark_subtask_done(task, int(number) - 1):
            print("Subtask marked as done.")
        else:
            print("Subtask is already done.")
        print_subtasks(task)

        if count_done_subtasks(task["subtasks"]) == len(task["subtasks"]):
            print("All subtasks of this task are done.")
            return

        if not ask_yes_no("Mark another subtask as done? (yes/no): "):
            return


def subtask_menu(tasks):
    print("\n[1] Add subtask")
    print("[2] Mark subtask as done")
    print("[3] Back to main menu")

    while True:
        choice = input("Enter an option: ").strip()
        if choice == "1":
            add_subtask(tasks)
            return True
        if choice == "2":
            select_subtask_to_complete(tasks)
            return True
        if choice == "3":
            return False
        print("Invalid choice. Please enter 1, 2 or 3.")
