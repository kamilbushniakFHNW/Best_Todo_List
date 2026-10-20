from datetime import datetime


def add_task(tasks):
    title = input("Title: ")
    description = input("Description: ")

    priorities ={"1": "Low", "2": "Medium", "3": "High"}

    while True:
        choice_priority = input("Priority - 1 Low, 2 Medium, 3 High [default: Medium]: ")

        if choice_priority == "":
            priority = "Medium"
            break
        elif choice_priority in priorities:
            priority = priorities[choice_priority]
            break
        else:
            print("Please enter 1, 2, 3 or press Enter for Medium")

    while True:
        due_date = input("Due date (DD.MM.YYYY): ")
        try:
            parsed_date = datetime.strptime(due_date, "%d.%m.%Y")
            if parsed_date.strftime("%d.%m.%Y") == due_date:
                break
        except ValueError:
        

         print("Wrong date")

    task = {
        "title": title, 
        "description": description, 
        "priority": priority,
        "due_date": due_date,
        "status": "Open",
        "subtasks": [],
    } 

    tasks.append(task)
    print(f"Task added: {title}")     

