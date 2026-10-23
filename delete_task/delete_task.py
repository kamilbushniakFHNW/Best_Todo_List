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