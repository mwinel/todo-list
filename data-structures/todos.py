# This file contains code that manages todo-lists and
# todo-items.

# Initialize a dictionary to store todos and todo items.
todos = {}


def create_todo_list(title):
    """
    Adds todo list given its title.
    parameters: title.
    returns: True if todo list is created.
    """
    # Initialize todo items as an empty list.
    items = []
    title = input("Add todo list title: ")
    if title == "":
        print("Fields cannot be left empty.")
        return False
    todos[title] = items
    print("Todo list successfully created.")
    print("'{}'".format(title))
    return True


def add_todo_item(title, item):
    """
    Adds a todo item to a todo list given its title.
    parameters: title, item.
    returns: True.
    """
    title = input("Enter todo list title to add todo item to: ")
    if title in todos.keys():
        item = input("Add a todo item to this list: ")
        todos[title].append(item)
        print(todos)
        return True
    else:
        print("Todo list does not exist.")
        return False


def update_todo_item(title, item):
    """
    Updates a todo item given its title.
    parameters: title, item
    returns: True if item updated
    """
    title = input("Enter todo list title where item is found: ")
    if title in todos.keys():
        items = todos[title]
        print(items)
        item = int(input("Enter position of todo item: "))
        if item <= len(items):
            updated_item = input("Edit todo item: ")
            items.remove(items[item-1])
            items.insert(item-1, updated_item)
            print("Todo item successfully updated.")
            print(items)
            return True
        else:
            print("Todo item does not exist.")
            return False
    else:
        print("Todo list does not exist.")
        return False


def find_todo_item(title, item):
    """
    Finds a specific todo item given a todo list title.
    parameters: title, item.
    returns: True if item exists.
    """
    title = input("Enter todo list title to find a todo item: ")
    if title in todos.keys():
        items = todos[title]
        item = int(input("Enter position of todo item: "))
        if item <= len(items):
            print(items[item-1])
            return True
        else:
            print("Todo item does not exist.")
            return False
    else:
        print("Todo list does not exist.")
        return False


def delete_todo_item(title, item):
    """
    Removes the specified todo item from a todo_list.
    parameters: title, item.
    returns: True if deleted.
    """
    title = input("Enter todo list title to delete todo item from: ")
    if title in todos.keys():
        items = todos[title]
        print(items)
        item = int(input("Enter todo item position: "))
        if item <= len(items):
            items.remove(items[item-1])
            print("Successfully deleted todo item.")
            print(items)
            return True
        else:
            print("Todo item does not exist.")
            return False
    else:
        print("Todo list does not exist.")
        return False


def view_todo_lists():
    """
    Returns a dictionary of all todos with the todo title
    as the key and the todo list as the value.
    """
    print(todos)
    return todos


def clear_todo_list(title):
    """
    Empties a todo_list given its title.
    returns: True.
    """
    title = input("Enter todo list title to be cleared: ")
    if title in todos.keys():
        items = todos[title]
        items.clear()
        print("Successfully cleared todo list.")
        return True
    else:
        print("Todo list does not exist.")
        return False
