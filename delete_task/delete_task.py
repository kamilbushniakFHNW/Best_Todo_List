from view_task.view_task import print_all_tasks, is_valid_task_number


def delete_task(tasks, index):
    confirmation = input("Are you sure you want to delete this task? (yes/no): ").strip().lower()

    while confirmation not in ("yes", "no"):
        print("Please enter yes or no.")
        confirmation = input("Are you sure you want to delete this task? (yes/no): ").strip().lower()

    if confirmation == "yes":
        removed_task = tasks.pop(index)
        print(f"Task deleted: {removed_task['title']}")
        return True

    else:
        print("Deletion cancelled.")
        return False


def select_task_to_delete(tasks):
    if not print_all_tasks(tasks):
        return

    while True:
        number = input("Task number to delete: ").strip()


        if is_valid_task_number(number, len(tasks)):
            index = int(number) - 1

            if delete_task(tasks, index):
                print_all_tasks(tasks)

            return

        else:
            print("Task not found.")

 
def delete_subtask(task, index):
    confirmation = input(
        "Are you sure you want to delete this subtask? (yes/no): "
    ).strip().lower()

    while confirmation not in ("yes", "no"):
        print("Please enter yes or no.")
        confirmation = input(
            "Are you sure you want to delete this subtask? (yes/no): "
        ).strip().lower()

    if confirmation == "yes":
        removed_subtask = task["subtasks"].pop(index)
        print(f"Subtask deleted: {removed_subtask['title']}")
        return True

    else:
        print("Deletion cancelled.")
        return False


def select_subtask_to_delete(tasks):
    if not print_all_tasks(tasks):
        return

    while True:
        number = input("Task number: ").strip()

        if is_valid_task_number(number, len(tasks)):
            task_index = int(number) - 1
            task = tasks[task_index]
            break
        else:
            print("Task not found.")

    subtasks = task["subtasks"]

    if not subtasks:
        print("This task has no subtasks.")
        return

    print("\n===== SUBTASKS =====")

    for index, subtask in enumerate(subtasks, start=1):
        print(f"{index}. {subtask['title']}")

    while True:
        number = input("Subtask number to delete: ").strip()

        if is_valid_task_number(number, len(subtasks)):
            subtask_index = int(number) - 1

            if delete_subtask(task, subtask_index):
                print("Subtask list updated.")

            return
        else:
            print("Subtask not found.")


def delete_menu(tasks):
    while True:
        print("\n===== DELETE MENU =====")
        print("1. Delete Task")
        print("2. Delete Subtask")
        print("0. Back to Main Menu")

        choice = input("Enter an option: ").strip()

        if choice == "1":
            select_task_to_delete(tasks)

        elif choice == "2":
            select_subtask_to_delete(tasks)

        elif choice == "0":
            return

        else:
            print("Invalid option. Please try again.")          