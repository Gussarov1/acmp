import unittest
from Task import Task


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task()

    def test_subtract1(self):
        numbers = '1 -3 0 0'
        self.assertEqual(self.task.case(numbers), '0 3')

    def test_subtract2(self):
        numbers = '3 -15 18 0'
        self.assertEqual(self.task.case(numbers), '0 2 3')

    def test_subtract3(self):
        numbers = '1 -7 -33 135'
        self.assertEqual(self.task.case(numbers), '-5 3 9')

# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
