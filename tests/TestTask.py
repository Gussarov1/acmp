import unittest
from Task import Task


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task()

    def test_subtract1(self):
        numbers = '	5\n-7 5 -1 3 9'
        self.assertEqual(self.task.case(numbers), (17, -15))

    def test_subtract2(self):
        numbers = '8\n3 14 -9 4 -5 1 -12 4'
        self.assertEqual(self.task.case(numbers), (26, 180))

    def test_subtract3(self):
        numbers = '	10\n-5 1 2 3 4 5 6 7 8 -3'
        self.assertEqual(self.task.case(numbers), (36, 5040))

# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
