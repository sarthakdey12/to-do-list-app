import os

# File where tasks will be stored
TASKS_FILE = 'tasks.txt'

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    else:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to add a new task
def add_task(task, tasks):
    tasks.append(task)
    save_tasks(tasks)

# Function to remove a task
def remove_task(task_number, tasks):
    if task_number > 0 and task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)

# Function to display tasks
def display_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks found.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task, tasks)
        elif choice == '3':
            display_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number, tasks)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
