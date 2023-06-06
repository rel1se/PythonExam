class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def walk(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'G':
            self.state = 'E'
            return 10
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'H':
            self.state = 'F'
            return 11
        else:
            raise MealyError("walk")

    def punch(self):
        if self.state == 'B':
            self.state = 'H'
            return 2
        if self.state == 'E':
            self.state = 'F'
            return 7
        if self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise MealyError("punch")

    def slur(self):
        if self.state == 'C':
            self.state = 'A'
            return 5
        if self.state == 'B':
            self.state = 'G'
            return 3
        if self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("slur")


def main():
    return Mealy()


def test():
    obj = main()
    for ch in "ABCDEFGH":
        obj.state = ch
        try:
            obj.walk()
        except MealyError:
            pass
        obj.state = ch
        try:
            obj.punch()
        except MealyError:
            pass
        obj.state = ch
        try:
            obj.slur()
        except MealyError:
            pass
