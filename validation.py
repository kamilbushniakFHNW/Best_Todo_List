"""Shared input checks used by all features of the to-do list."""

CANCEL_KEY = "0"


def is_cancel(text):
    """Return True if the user typed the cancel key."""
    return text.strip() == CANCEL_KEY


def is_valid_title(text):
    """Return True if the title is not empty."""
    return text.strip() != ""


def is_valid_task_number(text, task_count):
    """Return True if text is a whole number between 1 and task_count."""
    if not text.isdigit():
        return False
    number = int(text)
    return 1 <= number <= task_count


def ask_task_index(tasks, action):
    """Ask for a task number, e.g. action = "mark as done".

    Return the list index, or None if the user types the cancel key.
    """
    prompt = f"Task number to {action} ({CANCEL_KEY} to go back): "
    answer = input(prompt).strip()

    while not is_cancel(answer) and not is_valid_task_number(answer,
                                                             len(tasks)):
        print(f"Task not found. Enter a number from 1 to {len(tasks)}, "
              f"or {CANCEL_KEY} to go back.")
        answer = input(prompt).strip()

    if is_cancel(answer):
        return None
    return int(answer) - 1