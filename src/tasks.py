# This file contains code that manages tasks.

# Initialize a list to store tasks.
todo_list = []


def create_task(task):
    """
    Adds the task (string value) to a todo_list.
    parameters: task
    returns: True
    """
    task = input("Enter a task: ")
    if task == "":
        print("Fields cannot be empty.")
        return False
    if task in todo_list:
        print("Task already exists.")
        return False
    todo_list.append(task)
    print("Task successfully added to list.")
    print(todo_list)
    return True


def delete_task(task):
    """
    Removes the specified task from a todo_list.
    parameters: task
    returns: True
    """
    print(todo_list)
    task = int(input("Enter position of a task to be deleted: "))
    if task <= len(todo_list):
        todo_list.pop(task-1)
        print("Task successfully deleted.")
        print(todo_list)
        return True
    else:
        print("Task does not exist.")
        return False


def mark_as_finished(task):
    """
    Appends the string label '[finished]' at the end of the task,
    if it does not already have the label appended.
    It should remain in the todo_list.
    parameters: task
    returns: True
    """
    print(todo_list)
    task = int(input("Enter position of a task to be finished: "))
    if task <= len(todo_list):
        todo_list[task-1] += " [finished]"
        print(todo_list)
        print("Task successfully completed")
        return True
    else:
        print("Task does not exist")
        return False


def view_all_tasks():
    """
    Returns a complete list of all tasks.
    returns: True
    """
    print(todo_list)
    return True


def delete_all_tasks():
    """
    Empties the todo_list.
    returns: True
    """
    todo_list.clear()
    print(todo_list)
    return True
