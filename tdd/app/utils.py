from user import User


def create_user():
    name = input("Enter name: ")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    age = input("Enter age: ")
    if name == "" or password == "":
        print("Fields cannot be left empty.")
        return False
    if len(password) < 5:
        print("Password too short, cannot be less than five characters.")
        return False
    User(name, username, email, password, age)
    return True


def show_all_users(users):
    print("Showing all users...")
    for user in users:
        print(user)
