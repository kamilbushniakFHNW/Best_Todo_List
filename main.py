import json
from pathlib import Path
import add_task.add_task as add_task_module
TASKS_FILE = Path(__file__).resolve().parent / "tasks.json" #This line I'm not sure how it works
tasks = []

def printMenu():
    print("""
    +==========================================+
    |                                          |
    |        ✓  BEST TO-DO LIST  ✓             |
    |     Your very own task manager           |
    |                                          |
    +==========================================+

    ┌──────────── MENU ────────────┐
    │  [1]  Add task               │
    │  [2]  View tasks             │
    │  [3]  Mark task as done      │
    │  [4]  Delete task            │
    │  [5]  Show overdue tasks     │
    │  [6]  Add subtask            │
    │  [7]  Export PDF             │
    │  [0]  Exit                   │
    └──────────────────────────────┘
    """)

def placeholder(action_name):
    print(f"Feature ´action_name´ is not implemented yet")


def getUserChoice():
    return input("Enter an option: ")

def executeTask(choice):
    match choice:
            case "1":
                add_task_module.add_task(tasks)
            case "2":
                placeholder("View tasks")
            case "3":
                placeholder("Mark task as done")
            case "4":
                placeholder("Delete task")
            case "5":
                placeholder("Show overdue tasks")
            case "6":
                placeholder("Add subtask")
            case "7":
                placeholder("Export PDF")
            case "0":
                print("Goodbye!")
                return False
           # TODO: inavlid user input
    return True

def main():
    while True:
        printMenu()
        choice = getUserChoice()
        should_continue = executeTask(choice)
        if not should_continue:
            break

if __name__ == "__main__":
    main()