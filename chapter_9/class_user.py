class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"The name of the user is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}. How are you ding today?")

user_0 = User("John", "Doe")
user_1 = User("Jon", "Doeh")
user_2 = User("Joh", "Doen")

user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()