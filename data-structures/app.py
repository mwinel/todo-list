# This file contains the entry point to manipulate
# todo lists and todo items.
import time
from accounts import add_account, login
from todos import (create_todo_list, add_todo_item, update_todo_item,
                   find_todo_item, delete_todo_item, view_todo_lists,
                   clear_todo_list)


def choose_options():
    """
    Provides a list of manipulation options for a
    user to choose from.
    """
    print("Choose todo list options")
    print("1) add todo list")
    print("2) add todo item")
    print("3) update todo item")
    print("4) find a specific todo")
    print("5) delete todo item")
    print("6) view all todo lists")
    print("7) clear all todos from a list")
    print("8) exit")


def main():
    """
    Allows a person to create an account, login, and
    manipulate todo lists and manipulate todo items.
    """
    while True:
        print("1) Login")
        print("2) Signup")
        time.sleep(2)
        user_options = input("> ")
        if user_options == "1":
            if login("name", "password") is True:
                while True:
                    print("Todo Items")
                    choose_options()
                    todo_options = input("> ")
                    if todo_options == "1":
                        create_todo_list("title")
                    elif todo_options == "2":
                        add_todo_item("title", "item")
                    elif todo_options == "3":
                        update_todo_item("title", "item")
                    elif todo_options == "4":
                        find_todo_item("title", "item")
                    elif todo_options == "5":
                        delete_todo_item("title", "item")
                    elif todo_options == "6":
                        view_todo_lists()
                    elif todo_options == "7":
                        clear_todo_list("title")
                    elif todo_options == "8":
                        print("Exiting...")
                        time.sleep(3)
                        print("See you soon...")
                        time.sleep(2)
                        break
                    else:
                        print("Unrecognized input, Try Again!")
                else:
                    return False
        elif user_options == "2":
            add_account("name", "password")
        else:
            print("Unrecognized input, Try Again!")


if __name__ == "__main__":
    main()
