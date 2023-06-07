class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def trace(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'G'
            return 3
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'G':
            self.state = 'H'
            return 9
        if self.state == 'H':
            self.state = 'D'
            return 11
        else:
            raise MealyError("trace")

    def crack(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'C'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError("crack")

    def chip(self):
        if self.state == 'G':
            self.state = 'F'
            return 10
        if self.state == 'D':
            self.state = 'E'
            return 6
        else:
            raise MealyError("chip")

    def smash(self):
        if self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("smash")


def main():
    return Mealy()


def test():
    obj = main()
    for ch in "ABCDEFGH":
        obj.state = ch
        try:
            obj.trace()
        except MealyError:
            pass
        obj.state = ch
        try:
            obj.crack()
        except MealyError:
            pass
        obj.state = ch
        try:
            obj.chip()
        except MealyError:
            pass
        obj.state = ch
        try:
            obj.smash()
        except MealyError:
            pass
