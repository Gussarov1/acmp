import unittest
from Task import Task


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task()

    def test_subtract1(self):
        numbers = ['1', '1', '1']
        self.assertEqual(self.task.case(numbers), '1')

    def test_subtract2(self):
        numbers = ['1', '2', '3']
        self.assertEqual(self.task.case(numbers), '3')

    def test_subtract3(self):
        numbers = ['1891231241523461346134563451345285', '21346134683', '4958439238923098134613461346349024']
        self.assertEqual(self.task.case(numbers), '4958439238923098134613461346349024')

    def test_subtract4(self):
        numbers = ['0', '0', '0']
        self.assertEqual(self.task.case(numbers), '0')

    def test_subtract5(self):
        numbers = ['123', '1234', '1234']
        self.assertEqual(self.task.case(numbers), '1234')


    def test_subtract6(self):
        numbers = ['5', '7', '3']
        self.assertEqual(self.task.case(numbers), '7')


    def test_subtract7(self):
        numbers = ['987531', '234', '86364']
        self.assertEqual(self.task.case(numbers), '987531')


    def test_subtract8(self):
        numbers = ['189285', '283', '4958439238923098349024']
        self.assertEqual(self.task.case(numbers), '4958439238923098349024')


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
