from unittest import result


class Task:
    # empty constructor
    def __init__(self):
        pass

    def case(self, raw_read):
        numbers = raw_read.split(' ')
        result = 0

        if (int(numbers[0]) * int(numbers[1])) == int(numbers[2]):
            result = "YES"
        else:
            result = "NO"

        return result