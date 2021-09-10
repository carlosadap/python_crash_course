import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """
        Create an employee and with first name, last name and a salary for use in all test methods.
        """
        self.employee1 = Employee('John', 'Doe', 10000)

    def test_give_default_raise(self):
        """Test that the give_raise function gives 5000 by default"""
        self.employee1.give_raise()
        self.assertEqual(self.employee1.salary, 15000)

    def test_give_custom_raise(self):
        """Test that the give_raise function gives any custom value"""
        self.employee1.give_raise(20000)
        self.assertEqual(self.employee1.salary, 30000)

if __name__ == '__main__':
    unittest.main()