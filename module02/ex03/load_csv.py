import pandas as pd


def load(path: str) -> pd.DataFrame:
    """"""
    df = pd.read_csv(path)
    print("Loading dataset of dimensions", df.shape)
    return df
