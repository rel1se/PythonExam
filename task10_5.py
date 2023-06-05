class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.state = method_name
        super().__init__(method_name)


class Mealy:
    def __init__(self):
        self.state = "A"

    def model(self):
        if self.state == "A":
            return 2
        elif self.state == "B":
            self.state = "C"
            return 3
        elif self.state == "C":
            self.state = "D"
            return 4
        elif self.state == "F":
            self.state = "G"
            return 8
        else:
            raise MealyError("model")

    def look(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "D":
            self.state = "A"
            return 6
        elif self.state == "E":
            self.state = "F"
            return 7
        else:
            raise MealyError("look")

    def walk(self):
        if self.state == "A":
            self.state = "E"
            return 1
        elif self.state == "D":
            self.state = "E"
            return 5
        elif self.state == "F":
            self.state = "B"
            return 9
        else:
            raise MealyError("walk")

def main():
    return Mealy()

def test():
    obj = main()
    for ch in "ABCDEFG":
        obj.state = ch
        try:
            obj.model()
        except MealyError:
            pass
        try:
            obj.model()
        except MealyError:
            pass
        try:
            obj.model()
        except MealyError:
            pass
