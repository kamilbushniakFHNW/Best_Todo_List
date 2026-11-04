# Best_ToDo_List (CLI Version)

A command-line to-do list manager written in Python. You can add tasks with a priority and due date, view them, mark them as done, add subtasks, see overdue tasks and export everything as a PDF. All tasks are saved in `tasks.json`, so nothing is lost when you close the program.

Group project for the module *Programming Foundations* (FHNW, Autumn Semester 2026).

## Team

|   | Team Member         | User Stories                                          |
| - | ------------------- | ----------------------------------------------------- |
| 1 | Thasmini Thayaparan | U1 Main Menu, U11 Export PDF, U12 Add Subtasks        |
| 2 | Andrii Kyrychenko   | U2 Add Task, U3 Priority, U10 Reload Tasks            |
| 3 | Kamil Bušniak       | U4 View Task, U5 Mark Task as Done, U6 Validation     |
| 4 | Naveena Nagarajah   | U7 Delete Task, U8 Exit and Cancel, U9 Overdue Tasks  |

## How to Run

Requires Python 3.10 or newer (the menu uses `match`/`case`).

```
python main.py
```

## Project Structure

```
Best_Todo_List/
├── main.py            # starts the app and shows the main menu
├── tasks.json         # saved tasks
├── validation.py      # shared input checks used by all features
├── add_task/
│   ├── __init__.py
│   └── add_task.py
├── view_task/
│   ├── __init__.py
│   └── ...
└── ...                # one package per feature
```

Each feature lives in its own package (folder with an `__init__.py`). `main.py` imports the features and calls them from the menu.

## Task Data Format

Every task is stored as a dictionary. All tasks together form a list, which is saved to `tasks.json`.

```json
{
    "title": "Finish project report",
    "description": "Chapters 1 to 3",
    "priority": "High",
    "due_date": "15.11.2026",
    "status": "Open",
    "subtasks": [
        {"title": "Write introduction", "status": "Done"},
        {"title": "Add charts", "status": "Open"}
    ]
}
```

| Key           | Allowed values                      |
| ------------- | ----------------------------------- |
| `title`       | any text, not empty                 |
| `description` | any text, can be empty              |
| `priority`    | `Low`, `Medium`, `High`             |
| `due_date`    | date in the format `DD.MM.YYYY`     |
| `status`      | `Open` or `Done`                    |
| `subtasks`    | list of `{"title", "status"}` dicts |

New tasks always start with the status `Open`.

## Coding Conventions

- We follow PEP 8. Functions and variables use `snake_case` (e.g. `print_menu`, `get_user_choice`), constants use `UPPER_CASE` (e.g. `TASKS_FILE`).
- Check your files with `pycodestyle <file>.py` before you push.
- All input checks (menu choice, title, date, priority, task number) live in `validation.py`. Import them instead of writing your own loops.
- Functions return values where possible and leave printing to the code that calls them.
- Work in your own branch and open a pull request. Another team member reviews it before it is merged into `main`.

---

## User Stories

### U1: Main Menu Navigation

> **As a** student,
> **I want to** see a numbered main menu when the app starts,
> **So that** I can easily find and use every function of the app without remembering commands.

**Owner:** Thasmini

#### Acceptance Criteria

- **Start Screen:** When the program starts, the main menu displays the following options:
  - `1.` Add task
  - `2.` View tasks
  - `3.` Mark task as done
  - `4.` Delete task
  - `5.` Show overdue tasks
  - `6.` Add subtask
  - `7.` Export PDF
  - `0.` Exit
- **Selection:** The user selects an option by entering a number (0–7) and pressing Enter.
- **Return to Menu:** Completing an operation automatically returns the user to the main menu.
- **Input Validation:** Any input outside the range 0–7 displays `"Invalid choice. Please enter a number from 0 to 7."` and re-displays the menu.

---

### U2: Add Task

> **As a** student,
> **I want to** add new tasks to my Best_Todo_list,
> **So that** I can organize and keep track of my assignments.

**Owner:** Andrii

#### Acceptance Criteria

- **Menu Option:** The user can select "Add Task" from the main menu.
- **Task Title:** The user must enter a title for the task.
- **Description:** The user can enter an optional description.
- **Due Date:** The user enters a due date in the format `DD.MM.YYYY`.
- **Validation:** The user can't use the dates in past.
- **Canceletion:** The user can cancel the creation of a new task at any time.
- **Status:** A new task is saved with the status `Open`.

---

### U3: Priority

> **As a** student,
> **I want to** assign a priority to my tasks,
> **So that** I know which tasks are most important and should be completed first.

**Owner:** Andrii

#### Acceptance Criteria

- **Priority Option:** The user can choose between `Low`, `Medium` and `High`.
- **Selection:** The user selects a priority by entering a number (`1.` Low, `2.` Medium, `3.` High).
- **Default Priority:** If no priority is selected (the user just presses Enter), the task automatically receives `Medium` priority.
- **Display:** The priority is shown when viewing tasks.

---

### U4: View Task

> **As a** student,
> **I want to** view my tasks and their details,
> **So that** I can see what I have to do and check the information of each task.

**Owner:** Kamil

#### Acceptance Criteria

- **View All Tasks:** The user can display all tasks grouped by status (`Open`, `Done`).
- **View Single Task:** The user can select one task to see its full details.
- **Task Details:** The detail view shows the title, description, priority, due date, subtasks and current status.
- **Empty List:** If there are no tasks, the CLI shows a clear message instead of an empty list.
- **Tasks Unchanged:** Viewing tasks does not modify them.

---

### U5: Mark Task as Done

> **As a** student,
> **I want to** mark a task as done,
> **So that** I can see what I have completed and focus on the remaining tasks.

**Owner:** Kamil

#### Acceptance Criteria

- **Mark as Done:** The user can mark any `Open` task as done.
- **Updated Status:** After marking, the task's status changes to `Done`.
- **Keep Task Details:** The task keeps its title, description, priority, due date and subtasks.
- **Already Done:** If the task is already done, the CLI informs the user and makes no change.
- **List Update:** The CLI immediately displays the task in the `Done` group.

---

### U6: Validation and Error Handling

> **As a** student,
> **I want to** get clear messages when I enter something invalid,
> **So that** I can correct my mistake without the program crashing or losing my data.

**Owner:** Kamil

#### Acceptance Criteria

- **Empty Title:** A task cannot be created or saved with an empty title.
- **Invalid Due Date:** A due date in the wrong format or a non-existent date is rejected, and the expected format is shown.
- **Invalid Priority:** A priority outside the allowed values is rejected, and the allowed values are shown.
- **Unknown Task:** If the user selects a task that does not exist, the CLI shows an error message.
- **Invalid Menu Choice:** If the user enters an unknown command or menu option, the CLI shows the valid options.
- **Retry Input:** After an invalid input, the user is asked to enter the value again.
- **No Crash:** Invalid input never stops the program or causes an unhandled error.
- **Data Unchanged:** Existing tasks are not changed when an input is rejected.

---

### U7: Delete Task

> **As a** student,
> **I want to** delete tasks that I no longer need,
> **So that** I can keep my task list organized and up to date.

**Owner:** Naveena

#### Acceptance Criteria

- **Select Task:** The user can select a task to delete by its number.
- **Delete Task:** The selected task is removed from the task list.
- **Confirmation:** The system asks the user to confirm before deleting a task.
- **Cancel Deletion:** The user can cancel the deletion without changing the task list.
- **Updated List:** After deletion, the CLI displays the updated task list.

---

### U8: Exit and Cancel

> **As a** student,
> **I want to** exit the program or cancel an action,
> **So that** I can stop an operation or close the application whenever I want.

**Owner:** Naveena

#### Acceptance Criteria

- **Exit Program:** The user can select an option from the main menu to exit the program.
- **Cancel Action:** The user can cancel an ongoing action and return to the main menu.
- **No Changes:** Cancelling an action does not modify existing tasks.

---

### U9: Mark Overdue Tasks

> **As a** student,
> **I want to** have overdue tasks marked automatically by the system,
> **So that** I can easily identify missed deadlines and prioritize unfinished work.

**Owner:** Naveena

#### Acceptance Criteria

- **Check Due Dates:** The program compares task due dates with the current date.
- **Mark Overdue Tasks:** If a task's due date has passed and the task is not done, the due date is highlighted in red and the task is marked as overdue.
- **Automatic Update:** The overdue status is updated whenever the task list is displayed.

---

### U10: Reload Tasks

> **As a** student,
> **I want to** have my tasks saved and reloaded automatically when I restart the app,
> **So that** I can continue where I stopped last time without entering my tasks again.

**Owner:** Andrii

#### Acceptance Criteria

- **Automatic Save:** Every change (add, mark as done, delete, add subtask) is saved immediately to `tasks.json`.
- **Saved Data:** For each task, the file stores the fields described in [Task Data Format](#task-data-format), including all subtasks with their own status.
- **Reload at Start:** When the program starts, all tasks are loaded from `tasks.json` before the main menu appears, displaying `"Tasks loaded."`

---

### U11: Export To-Do List as PDF

> **As a** student,
> **I want to** export my to-do list as a PDF,
> **So that** I can print it, share it with my group or keep an overview of my tasks outside the app.

**Owner:** Thasmini

#### Acceptance Criteria

- **Menu Option:** Accessible via option `7. Export PDF` from the main menu.
- **Report Content:** The generated document contains:
  - Document header: `"To-Do List Report"`
  - Export date formatted as `DD.MM.YYYY`
  - All tasks with title, due date, priority, status and subtasks
- **File Naming:** Defaults to `todo_DD-MM-YYYY.pdf` using the current date.
- **Confirmation:** On success, the CLI shows `"Report saved as <file name>"`.
- **Error Handling:** If the file cannot be saved, the CLI shows `"Export failed: the file could not be saved."`

---

### U12: Add Subtasks

> **As a** student,
> **I want to** add subtasks to a task,
> **So that** I can split a big task into smaller steps and work on it piece by piece.

**Owner:** Thasmini

#### Acceptance Criteria

- **Task Selection:** The user selects the parent task by its number. Invalid or non-numeric input shows `"Task not found."` and asks again.
- **Subtask Creation:** The user is asked for a subtask title. Empty input shows `"Title cannot be empty."` and asks again.
- **Multiple Subtasks:** A task can have several subtasks, numbered 1, 2, 3, ...
- **Status Updates:** Each subtask can be marked as `Done` on its own.
- **Display Format:** Subtasks are shown indented below their parent task, together with a progress count (e.g. `"2/3 subtasks done"`).