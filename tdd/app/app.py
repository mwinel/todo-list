import time
from utils import create_user, show_all_users


def main():
    users = []
    while True:
        print("1) Sign Up")
        print("2) Login")
        option = input("> ")
        if option == "1":
            users.append(create_user())
            while True:
                print("1) Show users")
                print("2) Exit")
                user_option = input("> ")
                if user_option == "1":
                    show_all_users(users)
                elif user_option == "2":
                    print("Exiting...")
                    time.sleep(3)
                    print("See you soon...")
                    time.sleep(2)
                    break
                else:
                    print("Unrecognized input, Try Again!")
        else:
            print("Unrecognized Input, Try Again!")


if __name__ == "__main__":
    main()
