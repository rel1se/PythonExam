class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def make(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'B'
            return 7
        else:
            raise MealyError('make')

    def chat(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'E':
            self.state = 'F'
            return 8
        else:
            raise MealyError('chat')

    def roam(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        if self.state == 'C':
            self.state = 'E'
            return 5
        if self.state == 'B':
            self.state = 'F'
            return 3
        else:
            raise MealyError('roam')


def main():
    return Mealy()


def test():
    obj = main()
    for ch in "ABCDEF":
        obj.state = ch
        try:
            obj.make()
        except MealyError:
            pass
        obj.state = ch
        try:
            obj.chat()
        except MealyError:
            pass
        obj.state = ch
        try:
            obj.roam()
        except MealyError:
            pass
