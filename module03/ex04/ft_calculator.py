class calculator:
    """calculator doc"""
    def __init__(self):
        """calculator init doc"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dot product doc"""
        dot = 0
        for i in range(len(V1)):
            dot = dot + V1[i] * V2[i]
        print('Dot product is:', dot)


    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add_vec doc"""
        print('Add Vector is:', [float(V1[i] + V2[i]) for i in range(len(V1))])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """sous_vec doc"""
        print('Sous Vector is:', [float(V1[i] - V2[i]) for i in range(len(V1))])


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a,b)
    calculator.add_vec(a,b)
    calculator.sous_vec(a,b)


if __name__ == '__main__':
    main()
