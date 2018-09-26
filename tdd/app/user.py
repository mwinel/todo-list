# Using OOP best practices, write a simple program that
# registers a user (name, username, age, email, password, gender, etc.)


class User:
    """
    This class defines a user in terms of the name, username,
    email, password and age.
    """
    def __init__(self, name, username, email, password, age):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.age = age

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_age(self):
        return self.age

    def set_email(self, new_email):
        self.email = new_email

    def set_password(self, new_password):
        self.password = new_password

    def __str__(self):
        return "User[name=" + self.name + ", username=" + self.username + \
               ", email=" + self.email + ", password=" + self.password + \
               ", age=" + str(self.age) + "]"
