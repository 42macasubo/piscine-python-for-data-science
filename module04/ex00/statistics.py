def compute_mean(args_list: list[int | float], args_len: int) -> float:
    """compute_mean doc"""
    return (sum(args_list) / args_len)


def compute_median(args_list: list, args_len: int) -> float:
    """compute_median doc"""
    #if args_len < 2 throw ValueError
    if args_len % 2 == 0:
        index_left = int(args_len / 2) - 1
        index_right = index_left + 1
        return ((args_list[index_left] + args_list[index_right]) / 2.0)
    else:
        return (args_list[int(args_len / 2.0)])


def compute_quartile(args_list: list, args_len: int) -> list[float]:
    """"""
    #if args_len < 4 throw ValueError
    if args_len % 4 == 0:
        index_left = int(args_len / 4) - 1
        index_right = index_left + 1
        res = [(args_list[index_left] + args_list[index_right]) / 2]
        index_left = int(args_len / 4) * 3 - 1
        index_right = index_left + 1
        res = res + [(args_list[index_left] + args_list[index_right]) / 2]
    else:
        res = [float(args_list[int(args_len / 4)]),
                float(args_list[int(args_len / 4 * 3)])]
    return res


def compute_variance(args_list: list, args_len: int) -> float:
    """"""
    mean = compute_mean(args_list, args_len)
    squared_diff = [(x - mean) ** 2 for x in args_list]
    new_mean = compute_mean(squared_diff, args_len)
    return new_mean

def compute_standard_deviation(args_list: list, args_len: int) -> float:
    """"""
    return (compute_variance(args_list, args_len) ** (1/2))


def ft_statistics(*args: any, **kwargs: any) -> None:
    """statistics doc"""

    args_list = [a for a in args]
    args_list.sort()
    args_len = len(args_list)

    for key, val in kwargs.items():
        if val == 'mean':
            print('mean:', compute_mean(args_list, args_len))
        elif val == 'median':
            print('median:', int(compute_median(args_list, args_len)))
        elif val == 'quartile':
            print('quartile:', compute_quartile(args_list, args_len))
        elif val == 'std':
            print('std:', compute_standard_deviation(args_list, args_len))
        elif val == 'var':
            print('var:', compute_variance(args_list, args_len))


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")

if __name__ == '__main__':
    main()
