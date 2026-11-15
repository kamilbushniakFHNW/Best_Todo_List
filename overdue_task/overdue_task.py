from datetime import datetime
from view_task.view_task import format_task_line

RED = "\033[31m"
RESET = "\033[0m"


def is_overdue(task):
    if task["status"] == "Done":
        return False

    try:
        due_date = datetime.strptime(task["due_date"], "%d.%m.%Y").date()
    except (ValueError, TypeError):
        return False

    today = datetime.today().date()

    return due_date < today


def show_overdue_tasks(tasks):
    print("\n=== Overdue tasks ===")

    found = False

    for i in range(len(tasks)):
        task = tasks[i]

        if is_overdue(task):
            line = format_task_line(i + 1, task)
            due_date = task["due_date"]
            highlighted_date = f"{RED}{due_date} (OVERDUE){RESET}"
            print(line.replace(due_date, highlighted_date))
            found = True

    if not found:
        print("(no overdue tasks)")