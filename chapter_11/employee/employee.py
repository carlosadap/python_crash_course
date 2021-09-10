class Employee:
    """Describes an Employee"""

    def __init__(self, first_name, last_name, salary):
        """Store the first name, last name and the salary"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        """Add 5000 to the annual salary by default or any given value"""
        self.salary += salary_raise
