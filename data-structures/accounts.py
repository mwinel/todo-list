# This file contains the code for managing the user account.

# Initialize a dictionary to store user accounts.
# The key is name and value is password.
accounts = {}


def add_account(name, password):
    """
    Adds a key, value pair to the accounts dictionary.
    parameters: name, password
    returns: True if account is created
    """
    name = input("Enter username: ")
    password = input("Enter password: ")
    if name == "" or password == "":
        print("Fields cannot be left empty.")
        return False
    if len(password) < 5:
        print("Password too short, cannot be less than five characters.")
        return False
    if name in accounts.keys():
        print("User with username '{}' already exists.".format(name))
        print("Signup with a different username.")
        return False
    accounts[name] = password
    print("Account successfully created, login to add tasks.")
    return True


def login(name, password):
    """
    Checks if the supplied name and password exist in
    the accounts dictionary.
    parameters: name, password
    returns: True and false if not
    """
    name = input("Enter username: ")
    password = input("Enter password: ")
    if name in accounts and accounts[name] == password:
        print("Successfully logged in as '{}'.".format(name))
        return True
    else:
        print("User with username '{}' not found. Please Signup.".format(name))
        return False
