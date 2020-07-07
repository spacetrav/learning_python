class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Located in " + self.location)

    def greet_user(self):
        print("hello " + self.first_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

trav = User("Trav", "Deegan", "spacetrav", "spacetrav99@gmail.com", "brookings")
trav.greet_user()
trav.describe_user()
trav.increment_login_attempts()

