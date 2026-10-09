#  Best_ToDo_List (CLI-Version)

|  | Team Members |
| --- | --- |
| 1 | Thasmini Thayaparan |
| 2 | Kamil Bušniak |
| 3 | Naveena Nagarajah |
| 4 | Andrii Kyrychenko |

## User Stories

## U7: Delete Task

**User Story**

As a student, I want to delete tasks that I no longer need, so that I can keep my task list organized and up to date.

### Acceptance Criteria

- **Select Task:** The user can select a task to delete by its number.
- **Delete Task:** The selected task is removed from the task list.
- **Confirmation:** The system asks the user to confirm before deleting a task.
- **Cancel Deletion:** The user can cancel the deletion without changing the task list.
- **Updated List:** After deletion, the CLI displays the updated task list.

---

## U8: Exit and Cancel

**User Story**

As a student, I want to exit the program or cancel an action, so that I can stop an operation or close the application whenever I want.

### Acceptance Criteria

- **Exit Program:** The user can select an option from the main menu to exit the program.
- **Cancel Action:** The user can cancel an ongoing action and return to the main menu.
- **No Changes:** Cancelling an action does not modify existing tasks.

---

## U9: Mark Overdue Tasks

**User Story**

As a student, I want the system to automatically mark tasks that are overdue, so that I can easily identify missed deadlines and prioritize unfinished work.

### Acceptance Criteria

- **Check Due Dates:** The program compares task due dates with the current date.
- **Mark Overdue Tasks:** If a task's due date has passed and the task is not completed, the due date is highlighted in red and the task is marked as overdue.
- **Automatic Update:** The overdue status is updated whenever the task list is displayed.

### U10: Main Menu Navigation

> **As a** student,  
**I want to** see a numbered main menu when the app starts,  
**So that** I can easily find and use every function of the app without remembering commands.

#### Acceptance Criteria
* **Start Screen:** When the program starts, the main menu displays the following options:
  * `1.` Add task
  * `2.` View tasks
  * `3.` Mark task as done
  * `4.` Delete task
  * `5.` Show overdue tasks
  * `6.` Add subtask
  * `7.` Export PDF
  * `0.` Exit
* **Selection:** The user selects an option by entering a number (0–7) and pressing Enter.
* **Return to Menu:** Completing an operation automatically returns the user to the main menu.

(**Input Validation:** Any input outside the range 0–7 displays:  `"Invalid choice. Please enter a number from 0 to 7."` and re-displays the menu.)

---

### U11: Export To-Do List as PDF

> **As a** student,  
**I want to** export my to-do list as a PDF,  
**So that** I can print it, share it with my group or keep an overview of my tasks outside the app.

#### Acceptance Criteria
* **Menu Option:** Accessible via option `7. Export PDF` from the main menu.
* **Report Content:** The generated document contains:
  * Document header: `"To-Do List Report"`
  * Export timestamp formatted as `DD.MM.YYYY`
  * Complete task inventory including: 
    * **Title**
    * **Due Date**, 
    * **Priority** (`Low`, `Medium`, `High`)
    * **Status** (`Done`)
    * All associated **Subtasks**.
* **File Naming:** Defaults to `todo_DD-MM-YYYY.pdf` using the current date.
* **Confirmation:** On successful file generation, outputs: `"Report saved as <file name>"`.

(**Error Handling:** `"Export failed: the file could not be saved."`)

---

### U12: Add Subtasks

> **As a** student,  
**I want to** add subtasks to a task,  
**So that** I can split a big task into smaller steps and work on it piece by piece.

#### Acceptance Criteria
* **Task Selection:** The user identifies the target parent task by its index number. 
* **Subtask Creation:** Prompts for a subtask title. 
* **Multiple Subtasks:** Supports multiple sequential subtasks per parent task, indexed as 1, 2, 3, ....
* **Status Updates:** Subtasks can be updated independently as `Done`.
* **Display Format:** Subtasks render indented beneath their parent task, showing item status (`"2/3 subtasks done"`).

(**Task Selection:** Invalid or non-numeric indices trigger the message:  
  `"Task not found."` and re-prompt for input.

**Subtask Creation:** Empty inputs trigger:  
  `"Title cannot be empty."` and re-prompt for input.))

---
