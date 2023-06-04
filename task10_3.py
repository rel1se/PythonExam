class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)


class Mealy:
    def __init__(self):
        self.state = "A"

    def join(self):
        if self.state == 'A':
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError("join")

    def melt(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 6
        else:
            raise MealyError("melt")

    def step(self):
        if self.state == 'A':
            self.state = 'F'
            return 2
        if self.state == 'C':
            return 5
        if self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise MealyError("step")


def main():
    return Mealy()

def test():
    obj = main()
    for ch in "ABCDEF":
        obj.state = ch
        try:
            obj.join()
        except MealyError:
            pass

        obj.state = ch
        try:
            obj.melt()
        except MealyError:
            pass

        obj.state = ch
        try:
            obj.step()
        except MealyError:
            pass


# test()

# o = main()
# # print(o.walk()) # 0
# # print(o.walk()) # 1
# # #print(o.punch()) # MealyError
# # print(o.slur()) # 5
# # print(o.walk()) # 0
# # print(o.walk()) # 1
# # print(o.walk()) # 4
# # print(o.walk()) # 6
# # print(o.punch()) # 7
# # print(o.slur()) # 8
# # print(o.walk()) # 10
# # print(o.punch()) # 7
# # #print(o.punch()) # MealyError
# # print(o.slur()) # 8
# # print(o.punch()) # 9
# # print(o.walk()) # 11
