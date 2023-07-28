import unittest
from Task import Task


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task()

    def test_subtract1(self):
        numbers = '8 54 432'
        self.assertEqual(self.task.case(numbers), 'YES')

    def test_subtract2(self):
        numbers = '16 19 777'
        self.assertEqual(self.task.case(numbers), 'NO')


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
