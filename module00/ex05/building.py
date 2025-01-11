from sys import argv


def main():
    """count types of characters in a string"""
    punctuation = "!”#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    try:
        assert len(argv) <= 2, "more than one argument is provided"
        if len(argv) == 1 or argv[1] is None:
            string = input("What is the text to count?\n")
        else:
            string = argv[1]
        print("The text contains", len(string), "characters:")
        print(sum(1 for c in string if c.isupper()), "upper letters")
        print(sum(1 for c in string if c.islower()), "lower letters")
        print(sum(1 for c in string if c in punctuation), "punctuation marks")
        print(sum(1 for c in string if c.isspace()), "spaces")
        print(sum(1 for c in string if c.isdigit()), "digits")
    except (AssertionError, KeyboardInterrupt, EOFError) as error:
        print(error)


if __name__ == "__main__":
    main()
