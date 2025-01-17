def square(x: int | float) -> int | float:
    """"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """"""
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0
    y = [x]
    def inner() -> float:
        y.append(function(y[-1]))
        return y[-1]
    return inner


def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())

if __name__ == '__main__':
    main()
