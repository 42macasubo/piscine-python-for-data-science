def ft_filter(func, it) -> iter:
    """filter elements from an iterable based on a function"""
    return (val for val in it if func(val))


"""
def is_even(x):
    return x % 2 == 0


def is_tuple_equal_42(t):
    return sum(x for x in t) == 42


def main():
    print("\ntest is_even")
    a = [42, 21, -4, 84, -42, -42, -21, 0, 8, -600, 5, 7, 3]
    print(type(a), a)
    print("filter:", list(filter(is_even, a)))
    print("ft_filter:", list(ft_filter(is_even, a)))

    print("\ntest tuple 42")
    b = [(1, 2, 3), (0, 0, 42), (21, 22, -1),
        (-42, 0, 0), (42, 42, 42), (-21, -21, 84)]
    print("filter:", list(filter(is_tuple_equal_42, b)))
    print("ft_filter:", list(ft_filter(is_tuple_equal_42, b)))


if __name__ == "__main__":
    main()
"""
