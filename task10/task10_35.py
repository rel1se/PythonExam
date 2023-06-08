class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def drag(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            return 4
        if self.state == 'F':
            self.state = 'B'
            return 8
        else:
            raise MealyError('drag')

    def model(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 6
        if self.state == 'F':
            return 7
        else:
            raise MealyError('model')


def main():
    return Mealy()


def test():
    obj = main()
    for ch in "ABCDEF":
        obj.state = ch
        try:
            obj.drag()
        except MealyError:
            pass
        try:
            obj.model()
        except MealyError:
            pass

