# INIT POO

class Point:
    """
    # Define a point
    """

    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def display(self):
        return print(self.__x, self.__y)


# INIT SUPER
class One:
    def __init__(self, param1, param2):
        self.__param1 = param1
        self.__param2 = param2

    def calc(self):
        return self.__param1 * self.__param2


class Two(One):
    def __init__(self, param3):
        super().__init__(param3, 4)


def poo():
    # a = Point(5, 7)
    # a.set_y(4)
    # a.display()

    b = One(2, 4)
    print(b.calc())
    c = Two(3)
    print(c.calc())
