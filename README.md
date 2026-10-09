#  Best_ToDo_List (CLI-Version)

|  | Team Members |
| --- | --- |
| 1 | Thasmini Thayaparan |
| 2 | Kamil Bušniak |
| 3 | Naveena Nagarajah |
| 4 | Andrii Kyrychenko |

## User Stories

# User Stories

## 4. View task

**As a** student,
**I want to** view my tasks and their details,
**So that** I can see what I have to do and check the information of each task.

### Acceptance Criteria

- **View All Tasks:** The user can display all tasks grouped by workflow column (To Do, In Progress, Done).
- **View Single Task:** The user can select one task to see its full details.
- **Task Details:** The detail view shows the title, priority, due date, tags, subtasks, and current status.
- **Empty Board:** If there are no tasks, the CLI shows a clear message instead of an empty list.
- **Tasks Unchanged:** Viewing tasks does not modify them.

---

## 5. Mark task as done

**As a** student,
**I want to** mark a task as done,
**So that** I can see what I have completed and focus on the remaining tasks.

### Acceptance Criteria

- **Mark as Done:** The user can mark any task from To Do or In Progress as done.
- **Updated Status:** After marking, the task appears in the Done column.
- **Keep Task Details:** The task keeps its title, priority, due date, tags, and subtasks.
- **Already Done:** If the task is already done, the CLI informs the user and makes no change.
- **Board Update:** The CLI immediately displays the task in the Done column.

---

## 6. Validation and Error handling

**As a** student,
**I want to** get clear messages when I enter something invalid,
**So that** I can correct my mistake without the program crashing or losing my data.

### Acceptance Criteria

- **Empty Title:** A task cannot be created or saved with an empty title.
- **Invalid Due Date:** A due date in the wrong format or a non-existent date is rejected, and the expected format is shown.
- **Invalid Priority:** A priority outside the allowed values is rejected, and the allowed values are shown.
- **Unknown Task:** If the user selects a task that does not exist, the CLI shows an error message.
- **Invalid Menu Choice:** If the user enters an unknown command or menu option, the CLI shows the valid options.
- **Retry Input:** After an invalid input, the user is asked to enter the value again.
- **No Crash:** Invalid input never stops the program or causes an unhandled error.
- **Data Unchanged:** Existing tasks are not changed when an input is rejected.


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
