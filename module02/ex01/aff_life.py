import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """"""
    df = load("../life_expectancy_years.csv")
    print(df)
    row = df.iloc[58].drop('country')
    column_names = row.keys()

    print(row)
    print(column_names)

    plt.plot(column_names, row)
    plt.title("France Life expectancy Projections")
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.xticks(ticks=[i for i in range(0, 301, 40)], labels=[i for i in range(1800, 2100, 40)])
#    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040, 2080, 2100])
    plt.show()


if __name__ == "__main__":
    main()
