from datetime import datetime
import json


def cancelation(value):
    if value == "0":
       print("Task cancelled") 
       return True

def add_task(tasks):
    title = input("Write your title\nor enter [0] for cancel:")
    if cancelation(title):
        return
    description = input("Add your description\nor enter [0] for cancel:")
    if cancelation(description):
        return
    priorities ={"1": "Low", "2": "Medium", "3": "High"}
    
    while True:
        choice_priority = input("Choose priority - 1 Low, 2 Medium, 3 High [default: Medium]\nor enter [0] for cancel:")

        if cancelation(choice_priority):
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
     due_date = input("Enter due date (DD.MM.YYYY)\nor enter 0 for cancel: ")

     if due_date == "0":
        print("Task cancelled")
        return

     try:
        parsed_date = datetime.strptime(due_date, "%d.%m.%Y")

        if parsed_date.date() >= datetime.today().date():
            break
        else:
            print("Invalid date! Date cannot be in the past.")
            continue
        

     except ValueError:
         print("Invalid date format! Use DD.MM.YYYY.")
        



    task = {
        "title": title, 
        "description": description, 
        "priority": priority,
        "due_date": due_date,
        "status": "Open",
        "subtasks": [],
    } 
    
    tasks.append(task)
    with open("tasks.json", "a", encoding="utf-8") as file:
        json.dump(tasks, file, indent= 4, ensure_ascii=False)
    print(f"Task added: {title}")
