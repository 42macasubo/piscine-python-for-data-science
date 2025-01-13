import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """calculate bmi"""
    return list(np.divide(np.array(weight), np.square(height)))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """create list of boolean after applying a limit condition on bmi values"""
    return list(np.where(np.array(bmi) > limit, True, False))


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
