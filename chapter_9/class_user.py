class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"The name of the user is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}. How are you doing today?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_0 = User("John", "Doe")
user_1 = User("Jon", "Doeh")
user_2 = User("Joh", "Doen")

user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()

user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can ban user", "and so on"]

    def show_privileges(self):
        print("The Admin:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

    # def show_privileges(self):
    #     print("The Admin:")
    #     for privilege in self.privileges:
    #         print(f"- {privilege.title()}")


my_admin = Admin("Foo", "Spam")
# my_admin.show_privileges()
my_admin.privileges.show_privileges()
