from datetime import datetime



def add_task(tasks):
    title = input("Write your title\nor enter [0] for cancel:")
    if title is "0":
        print("Task cancelled")
        return
    description = input("Add your description\nor enter [0] for cancel:")
    if description is "0":
        print("Task cancelled")
        return
    priorities ={"1": "Low", "2": "Medium", "3": "High"}
    
    while True:
        choice_priority = cancelation("Choose priority - 1 Low, 2 Medium, 3 High [default: Medium]\nor enter [0] for cancel:")

        if choice_priority is "0":
            print("Task cancelled")
            return
        if choice_priority == "":
            priority = "Medium"
            break
        elif choice_priority in priorities:
            priority = priorities[choice_priority]
            break
        else:
            print("Please enter 1, 2, 3 or press Enter for Medium\nor enter [0] for cancel:")

    while True:
        due_date = cancelation("Enter due date (DD.MM.YYYY)\nor enter 0 for cancel:")
        parsed_date = datetime.strptime(due_date, "%d.%m.%Y")
        if due_date is "0":
           print("Task cancelled")
           return
        if parsed_date.date() > datetime.today().date():
           break
        else:
            print("Invalid date")


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

