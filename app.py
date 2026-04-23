import os

FILE_NAME = "tasks.txt"

tasks = []

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append("[ ] " + task)
    save_tasks()
    print("Task added!")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks()
            print(f"Deleted: {removed}")
        else:
            print("Invalid number!")
    except:
        print("Enter valid number!")

def mark_done():
    show_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = tasks[num - 1].replace("[ ]", "[✓]")
            save_tasks()
            print("Marked as done!")
        else:
            print("Invalid number!")
    except:
        print("Enter valid number!")

def main():
    load_tasks()

    while True:
        print("\n=== CLI To-Do Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
