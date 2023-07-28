from unittest import result


class Task:
    # empty constructor
    def __init__(self):
        pass

    def case(self, numbers):
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        return str(max(numbers))
