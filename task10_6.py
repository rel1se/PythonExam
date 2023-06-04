class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)


class Mealy():
    def __init__(self):
        self.state = "A"

    def fade(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise MealyError("fade")

    def erase(self):
        if self.state == 'A':
            return 1
        elif self.state == 'B':
            self.state = 'F'
            return 3
        elif self.state == 'D':
            self.state = 'F'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'G':
            self.state = 'C'
            return 9
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("erase")


def main():
    return Mealy()


def test():
    obj = main()
    for ch in "ABCDEFG":
        obj.state = ch
        try:
            obj.fade()
        except MealyError:
            pass

        obj.state = ch
        try:
            obj.erase()
        except MealyError:
            pass

