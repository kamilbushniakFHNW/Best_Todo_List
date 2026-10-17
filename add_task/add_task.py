def add_task(tasks):
    title = input("Add your task: ")
    description = input("Add your description: ")

    while True:
        print("Choose priority:")
        print("[1] High")
        print("[2] Medium")
        print("[3] Low")
        choice_priority = input("Add priority: ")

        if choice_priority == "1":
            priority = "High"
            break
        elif choice_priority == "2":
            priority = "Medium"
            break
        elif choice_priority == "3":
            priority = "Low"
            break
        else:
            print("Please enter 1, 2, or 3.")

    tasks.append(f"{title}\n{description}\n{priority}")            
    print(f"Task added:\n{title}\n{description}\n{priority}")        

