import unittest

from employee_class import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        # create an employee to use in tests
        self.trav = Employee('trav', 'deegan', 65000)

    def test_give_default_raise(self):
        self.trav.give_raise()
        self.assertEqual(self.trav.salary, 70000)

    def test_give_custom_raise(self):
        self.trav.give_raise(20000)
        self.assertEqual(self.trav.salary, 85000)

unittest.main()