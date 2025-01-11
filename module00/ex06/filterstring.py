from sys import argv
from ft_filter import ft_filter


def main():
    """filter string to keep words longer than a number"""
    try:
        assert len(argv) == 3
        print([i for i in
              ft_filter(lambda w: len(w) > int(argv[2]), argv[1].split(' '))])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
