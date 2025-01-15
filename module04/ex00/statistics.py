def ft_statistics(*args: any, **kwargs: any) -> None:
    """statistics doc"""

    args_list = [a for a in args]
    args_list.sort()
    args_len = len(args_list)

    for key, val in kwargs.items():
        if val == 'mean':
            print('mean:', sum(args_list) / len(args_list))
        elif val == 'median':
            if args_len % 2 == 0:
                index_left = int(args_len / 2) - 1
                index_right = index_left + 1
                print('median:', (args_list[index_left] + args_list[index_right]) / 2)
            else:
                print('median:', args_list[int(args_len / 2)])
        elif val == 'quartile':
            if args_len % 2 == 0:
                index_left = int(args_len / 4) - 1
                index_right = index_left + 1
                res = [(args_list[index_left] + args_list[index_right]) / 2]
            


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
