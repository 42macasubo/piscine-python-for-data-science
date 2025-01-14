import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load


def literal_to_decimal(text: str) -> str:
    """"""
    d = {
         'k': 10**3,
         'M': 10**6
    }
    if text[-1] in d:
        num, magnitude = text[:-1], text[-1]
        return "{:.0f}".format(float(num) * d[magnitude])
    return text


def decimal_to_M(text: str) -> str:
    return f"{int(int(text) / 10**6)}M"


def main():
    """"""
    df = load("../population_total.csv")
    row_france = df.iloc[58]
    row_germany = df.iloc[44]

    row_france = row_france.drop('country').drop(labels = [str(i) for i in range(2051, 2101, 1)])
    row_germany = row_germany.drop('country').drop(labels = [str(i) for i in range(2051, 2101, 1)])

    row_france = row_france.apply(literal_to_decimal).apply(decimal_to_M)
    row_germany = row_germany.apply(literal_to_decimal).apply(decimal_to_M)
   
    unique_values_count = len(set(row_france.tolist() + row_germany.tolist()))
    print(unique_values_count)
 
#    with open("out", 'w') as f:
#        print(row_france.to_string(), file=f)

    row_keys = row_france.keys()

#    fig, ax = plt.subplots()
#    plt.plot(row_keys, row_germany, '-.')
#    ax.plot(row_keys, row_france)
#    plt.yticks(ticks=[0, 20, 40, 60, 80, 100])
#    plt.xticks(ticks=[i for i in range(0, 251, 40)], labels=[i for i in range(1800, 2050, 40)])
#    ax.set_ylim(bottom = 0)

    fig, ax = plt.subplots()

    ax.plot(row_keys, row_germany, label='Germany', color='blue')
    ax.plot(row_keys, row_france, label='France', color='green')
    ax.legend(loc='lower right')
    ax.set_xticks([i for i in range(0, 251, 40)])
    ax.set_yticks([i for i in range(12, unique_values_count, 20)])

    ax.set_title("Population Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")

    plt.show()


if __name__ == "__main__":
    main()
