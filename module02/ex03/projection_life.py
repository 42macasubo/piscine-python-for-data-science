import matplotlib as matplot
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
    life_expectancy = load("../life_expectancy_years.csv")
    income = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = life_expectancy[['country', '1900']]
    income = income[['country', '1900']]
    print(life_expectancy)
    print(income)

#    df = income.join(life_expectancy, lsuffix='_income', rsuffix='_life_expectancy')
    df = income.merge(life_expectancy, how='left', on='country', suffixes=('_income', '_life'))
    df = df.dropna(axis='index').sort_values(by='1900_income')
#    print(df)

    with open("out", 'w') as f:
        print(df.to_string(), file=f)

    fig, ax = plt.subplots()
    ax.scatter(df['1900_income'], df['1900_life'])
    ax.set_xscale('log')
    print(ax.get_xticks())
#    ax.get_xaxis().set_major_formatter(matplot.ticker.FuncFormatter(lambda x, p: (x / 1000)))

    ax.set_title("1900")
    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life expectancy")

    print(df['1900_life'].to_list())
    m, b = np.polyfit(df['1900_income'].to_list(), df['1900_life'].to_list(), 1)
    print('m: ', m)
    print('b: ', b)
    life_fit = df['1900_income'].apply(lambda x: m * x + b)
#    print(income_modified)
#    ax.plot(df['1900_income'], life_fit, color='red', label="y = {}x + {}".format(m, b))
    ax.plot(df['1900_income'], life_fit, color='red')
    ax.legend(["data points", "y = {:.3f}x + {:.3f}".format(m, b)], loc='lower right')
    correlation = df['1900_income'].corr(df['1900_life'])
    print('correlation: ', correlation)

#    ax.plot([df['1900_income'].min(), df['1900_income'].max()], [df['1900_life'].min(), df['1900_life'].max()])

    ax.set_xticks([300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()

    """
    row_france = row_france.drop('country').drop(labels = [str(i) for i in range(2051, 2101, 1)])
    row_germany = row_germany.drop('country').drop(labels = [str(i) for i in range(2051, 2101, 1)])

    row_france = row_france.apply(literal_to_decimal).apply(decimal_to_M)
    row_germany = row_germany.apply(literal_to_decimal).apply(decimal_to_M)
   
    unique_values_count = len(set(row_france.tolist() + row_germany.tolist()))
    print(unique_values_count)
 

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


    plt.show()
    """

if __name__ == "__main__":
    main()
