
from datetime import datetime, date
from view_task.view_task import print_all_tasks, is_valid_task_number


def edit_task(tasks):
    if not print_all_tasks(tasks):
        return

    while True:
        number = input("Task number to edit (0 to go back): ").strip()

        if number == "0":
            return

        if is_valid_task_number(number, len(tasks)):
            index = int(number) - 1
            task = tasks[index]
            break

        else:
            print("Task not found.")

    while True:
        print("\n===== EDIT TASK =====")
        print(f"Selected task: {task['title']}")
        print("1. Edit Title")
        print("2. Edit Description")
        print("3. Edit Priority")
        print("4. Edit Due Date")
        print("0. Back")

        choice = input("Enter an option: ").strip()

        if choice == "1":
            new_title = input("Enter new title: ").strip()

            if not new_title:
                print("Title cannot be empty.")
                continue

            task["title"] = new_title
            print("Title updated successfully.")

        elif choice == "2":
            new_description = input("Enter new description: ").strip()
            task["description"] = new_description
            print("Description updated successfully.")

        elif choice == "3":
            new_priority = input(
                "Enter new priority (High/Medium/Low): "
            ).strip().capitalize()

            if new_priority not in ("High", "Medium", "Low"):
                print("Invalid priority.")
                continue

            task["priority"] = new_priority
            print("Priority updated successfully.")

        elif choice == "4":
            new_date = input(
                "Enter new due date (DD.MM.YYYY): "
            ).strip()

            try:
                valid_date = datetime.strptime(
                    new_date, "%d.%m.%Y"
                ).date()

            except ValueError:
                print("Invalid date. Use DD.MM.YYYY.")
                continue

            if valid_date < date.today():
                print("Due date cannot be in the past.")
                continue

            task["due_date"] = valid_date.strftime("%d.%m.%Y")
            print("Due date updated successfully.")

        elif choice == "0":
            return

        else:
            print("Invalid option. Please try again.")


def edit_subtask(tasks):
    if not print_all_tasks(tasks):
        return

    while True:
        number = input("Task number (0 to go back): ").strip()

        if number == "0":
            return

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
        number = input(
            "Subtask number to edit (0 to go back): "
        ).strip()

        if number == "0":
            return

        if is_valid_task_number(number, len(subtasks)):
            subtask_index = int(number) - 1
            subtask = subtasks[subtask_index]
            break

        else:
            print("Subtask not found.")

    print(f"Current title: {subtask['title']}")

    while True:
        new_title = input("Enter new subtask title: ").strip()

        if not new_title:
            print("Title cannot be empty.")

        else:
            subtask["title"] = new_title
            print("Subtask updated successfully.")
            return


def edit_menu(tasks):
    while True:
        print("\n===== EDIT MENU =====")
        print("1. Edit Task")
        print("2. Edit Subtask")
        print("0. Back to Main Menu")

        choice = input("Enter an option: ").strip()

        if choice == "1":
            edit_task(tasks)

        elif choice == "2":
            edit_subtask(tasks)

        elif choice == "0":
            return

        else:
            print("Invalid option. Please try again.")
