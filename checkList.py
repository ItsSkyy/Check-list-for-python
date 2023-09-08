import os

# Check if "tasks.txt" exists, and create it if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as tasks_file:
        pass

if not os.path.exists("last_task_number.txt"):
    with open("last_task_number.txt", "w") as task_numbers_file:
        pass

def get_user_input(prompt):
    return input(prompt)

def add_task(tasks):
    userTask = get_user_input('Please enter the title of your task: ')
    userTaskDesc = get_user_input('Give a description of the task if you require one: ')
    task_number = len(tasks) + 1
    tasks[task_number] = {'Task Title': userTask, 'Task Description': userTaskDesc}
    print('Your new task is as follows:\n')
    print('Task Number:', task_number)
    print('Task Title:', userTask)
    print('Task Description:', userTaskDesc)

def delete_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Here are the tasks on your list:")
    for task_number, task in tasks.items():
        print(f"{task_number}: {task['Task Title']}")
    userTaskSelection = int(get_user_input("Which task would you like to delete? (Enter the task number): "))
    if userTaskSelection in tasks:
        del tasks[userTaskSelection]
        print(f"Task {userTaskSelection} has been deleted.")
    else:
        print(f"No task with number {userTaskSelection} found.")

def modify_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Here are the tasks on your list:")
    for task_number, task in tasks.items():
        print(f"{task_number}: {task['Task Title']}")

    userTaskSelection = int(get_user_input("Which task would you like to modify? (Enter the task number): "))
    if userTaskSelection in tasks:
        task = tasks[userTaskSelection]
        task['Task Title'] = get_user_input("Enter the new title for the task: ")
        task['Task Description'] = get_user_input("Enter the new description for the task: ")
        print(f"Task {userTaskSelection} has been modified.")
    else:
        print(f"No task with number {userTaskSelection} found.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your current tasks:")
        for task_number, task in tasks.items():
            print(f"{task_number}: {task['Task Title']} - {task['Task Description']}")

def save_tasks_to_file(tasks):
    with open("tasks.txt", "w") as file:
        for task_number, task in tasks.items():
            file.write(f"{task_number},{task['Task Title']},{task['Task Description']}\n")
    print("Tasks saved successfully.")

def load_tasks_from_file():
    tasks = {}
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(',')
                if len(task_data) == 3:
                    task_number, task_title, task_description = task_data
                    tasks[int(task_number)] = {'Task Title': task_title, 'Task Description': task_description}
    except FileNotFoundError:
        pass
    return tasks

def main():
    tasks = load_tasks_from_file()

    while True:
        print('Welcome to your to-do list. What would you like to do?')
        print('1: Add a new task')
        print('2: Delete a task')
        print('3: Modify a task')
        print('4: View current tasks')
        print('5: Close program')

        user_choice = int(get_user_input("Enter your choice (1-5): "))

        if user_choice == 1:
            add_task(tasks)
        elif user_choice == 2:
            delete_task(tasks)
        elif user_choice == 3:
            modify_task(tasks)
        elif user_choice == 4:
            view_tasks(tasks)
        elif user_choice == 5:
            print("Closing program...")
            save_tasks_to_file(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
