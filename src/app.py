# This file contains the entry point to tasks
# and the logic to manage the tasks.
import time
from accounts import add_account, login
from tasks import (create_task, delete_task, delete_all_tasks,
                   view_all_tasks, mark_as_finished)


def main():
    """
    Allows a person to create account, login and
    manipulate todo tasks.
    """
    while True:
        print("1) Login")
        print("2) Signup")
        time.sleep(2)
        user_options = input("> ")
        if user_options == "1":
            if login("name", "password") is True:
                while True:
                    print("Choose an option to manage your tasks.")
                    print("1) add task")
                    print("2) delete task")
                    print("3) mark task as finished")
                    print("4) view all tasks")
                    print("5) delete all tasks")
                    print("6) exit")
                    task_options = input("> ")
                    if task_options == "1":
                        create_task("task")
                    elif task_options == "2":
                        delete_task("task")
                    elif task_options == "3":
                        mark_as_finished("task")
                    elif task_options == "4":
                        view_all_tasks()
                    elif task_options == "5":
                        delete_all_tasks()
                    elif task_options == "6":
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
