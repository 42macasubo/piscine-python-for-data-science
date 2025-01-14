class calculator:
    """calculator doc"""
    def __init__(self, vector):
        """calculator init doc"""
        self.vector = vector

    def __add__(self, object) -> None:
        """add doc"""
        self.vector = [i + object for i in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """mul doc"""
        self.vector = [i * object for i in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """sub doc"""
        self.vector = [i - object for i in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """truediv doc"""
        self.vector = [i / object for i in self.vector]
        print(self.vector)


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == '__main__':
    main()
