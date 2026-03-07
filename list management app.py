import json
file_name = "todo_list.json"
# load tasks from file
def load_tasks():
    try:
        with open(file_name, "r") as f:
            tasks = json.load(f)
    except:
        tasks = {"tasks": []}
    return tasks
# save tasks to file
def save_tasks(tasks):
    try:
        with open(file_name, "w") as f:
            json.dump(tasks, f)
    except:
        print("Error saving tasks")
# show all tasks
def view_tasks(tasks):
    task_list = tasks["tasks"]
    if not task_list:
        print("No tasks found")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(task_list, start=1):
        status = "Completed" if task["complete"] else "Pending"
        print(f"{i}. {task['description']} - {status}")
# add new task
def add_task(tasks):
    desc = input("Enter task: ").strip()
    if desc == "":
        print("Task cannot be empty")
        return
    tasks["tasks"].append({
        "description": desc,
        "complete": False
    })
    save_tasks(tasks)
    print("Task added successfully")
# mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to complete: "))
        if 1 <= num <= len(tasks["tasks"]):
            tasks["tasks"][num - 1]["complete"] = True
            save_tasks(tasks)
            print("Task completed")
        else:
            print("Invalid task number")
    except:
        print("Enter a valid number")
# main program
def main():
    tasks = load_tasks()
    while True:
        print("\n---- TO DO LIST ----")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("Bye")
            break
        else:
            print("Invalid choice")                                                                                      
main()