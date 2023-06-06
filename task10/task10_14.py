class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def smash(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        if self.state == 'B':
            self.state = 'F'
            return 3
        if self.state == 'F':
            self.state = 'C'
            return 8
        if self.state == 'D':
            self.state = 'E'
            return 6
        else:
            raise MealyError('smash')

    def spawn(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 4
        else:
            raise MealyError('spawn')

    def cull(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError('cull')


def main():
    return Mealy()


def test():
    obj = main()
    for ch in "ABCDEF":
        obj.state = ch
        try:
            obj.smash()
        except MealyError:
            pass
        obj.state = ch
        try:
            obj.spawn()
        except MealyError:
            pass
        obj.state = ch
        try:
            obj.cull()
        except MealyError:
            pass
