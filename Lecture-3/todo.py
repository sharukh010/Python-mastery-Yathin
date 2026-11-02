from tabulate import tabulate 
def get_todo(tid): 
    for todo in todos: 
        if todo["id"] == tid: 
            return todo 
    return None 

print("Todo App:")
options = """options: 
1. Add a todo 
2. Display all the todos 
3. Mark a todo as completed 
4. Update a todo 
5. Delete a todo 
6. exit """
todos = [
    {
        "id":1,
        "title":"Do Homework",
        "description":"Complete Python lecture-3 homework",
        "status": "pending",
    },
    {
        "id":2,
        "title":"Do Math Homework",
        "description": "Solve Algebra questions",
        "status":"completed"
    }
] # its a list of dictionaries 
tid = 2
while True: 
    print(options)
    choice = int(input("Enter your choice (1-6): "))
    match choice: 
        case 1: 
            print("Adding a Todo: ")
            title = input("Title: ")
            description = input("Description: ")
            status = "pending"
            todo = {
                "id": tid+1,
                "title": title,
                "description": description,
                "status": status
            }
            tid += 1 
            todos.append(todo)
            print(f"Succesfully added todo.")
        case 2: 
            print("Displaing Todos: ")
            table = tabulate(todos,headers="keys",tablefmt="grid")
            print(table)
        case 3: 
            print("Marking Todo as Completed: ")
            target = int(input("Todo ID: "))
            todo = get_todo(target)
            if todo is None: 
                print("Todo Not Found")
            else: 
                todo["status"] = "completed"
                print("Todo marked as completed..")
        case 4: 
            print("Updating a Todo: ")
            target = int(input("Todo ID: "))
            todo = get_todo(target)
            if todo is None: 
                print("Todo Not Found")
            else: 
                key = input("Key: ")
                value = input("Value: ")
                todo[key]=value
                print("Updated Successfully") 
        case 5: 
            print("Deleting a Todo: ")
            target = int(input("Todo ID: "))
            todo = get_todo(target)
            index = todos.index(todo)
            todos.pop(index)
            print("Todo Deleted Successfully")
        case 6: 
            print("Exiting..")
            break 
        case _: 
            print("Invalid option. Try again")
    print("="*25)