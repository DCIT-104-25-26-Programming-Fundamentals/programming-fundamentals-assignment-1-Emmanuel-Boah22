# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Global list to store tasks
tasks = []

# Feature 1 — Add a Task


def add_task():
    """Prompts the user for a task description and adds it to the list."""
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


# Feature 2 — View All Tasks

def view_tasks():
    """Displays all tasks numbered from 1. Shows a message if the list is empty."""
    if len(tasks) == 0:
        print("Your task list is empty. Add some tasks!")
    else:
        print("Your Tasks:")
        for i in range(len(tasks)):
            print(f"  {i + 1}. {tasks[i]}")


# Feature 3 — Delete a Task

def delete_task():
    """Shows tasks with numbers, asks which to delete, and removes it."""
    if len(tasks) == 0:
        print("Your task list is empty. Nothing to delete.")
        return

    print("Your Tasks:")
    for i in range(len(tasks)):
        print(f"  {i + 1}. {tasks[i]}")

    choice_str = input("Enter task number to delete: ")
    choice = int(choice_str)

    if choice < 1 or choice > len(tasks):
        print(
            f"Error: Invalid task number. Please enter a number between 1 and {len(tasks)}.")
        return

    removed = tasks.pop(choice - 1)
    print(f'Task "{removed}" has been removed.')


# Feature 4 — Quit

def quit_program():
    """Ends the program with a farewell message."""
    print("Goodbye!")


# Main Menu

def main():
    """Runs the interactive menu loop."""
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            quit_program()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
# Global list to store tasks
tasks = []


def add_task():
    """Prompts the user for a task description and adds it to the list."""
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks():
    """Displays all tasks numbered from 1. Shows a message if the list is empty."""
    if not tasks:
        print("Your task list is empty. Add some tasks!")
        return
    print("Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")


def delete_task():
    """Shows tasks with numbers, asks which to delete, and removes it."""
    if not tasks:
        print("Your task list is empty. Nothing to delete.")
        return

    view_tasks()
    choice = int(input("Enter task number to delete: "))

    if choice < 1 or choice > len(tasks):
        print(
            f"Error: Invalid task number. Please enter a number between 1 and {len(tasks)}.")
        return

    removed = tasks.pop(choice - 1)
    print(f'Task "{removed}" has been removed.')


def quit_program():
    """Ends the program with a farewell message."""
    print("Goodbye!")


def main():
    """Runs the interactive menu loop."""
    menu = "1. Add task\n2. View tasks\n3. Delete task\n4. Quit"
    actions = {"1": add_task, "2": view_tasks, "3": delete_task}

    while True:
        print(menu)
        choice = input("Enter your choice (1-4): ")

        if choice == "4":
            quit_program()
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
