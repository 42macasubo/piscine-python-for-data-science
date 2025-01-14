import pandas as pd


def load(path: str) -> pd.DataFrame:
    """"""
    df = pd.read_csv(path)
    print("Loading dataset of dimensions", df.shape)
    return df


def main():
    print(load("../life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
