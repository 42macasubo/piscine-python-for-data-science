def ft_tqdm(lst: range) -> None:
    """print progress bar using yield operator"""
    length_total = 99
    length_start = 6
    length_end = 3
    length_reserved = 26
    range_last = lst[-1] + 1
    step = 20

    for i in lst:
        i = i + 1
        if i % step == 0 or i == range_last:
            percent = int(i * 100 / range_last)
            length_numbers = len(str(i)) + 1 + len(str(range_last))
            length_bar = length_total - length_start - length_end \
                - length_numbers - length_reserved
            length_progress = int(percent * length_bar / 100)
            length_blank = length_bar - length_progress
            print('{: >3.0f}'.format(percent) + "%|["
                  + ''.join('=' for j in range(
                    0 if length_progress == 0 else length_progress - 1))
                  + (">" if length_progress > 0 else "")
                  + ''.join(' ' for k in range(length_blank)) + "]| " +
                  str(i) + '/' + str(range_last),
                  end='\r')
        yield i


"""
from time import sleep
from tqdm import tqdm

for elem in ft_tqdm(range(3333)):
    sleep(0.005)
print()

for elem in tqdm(range(3333)):
    sleep(0.005)
print()
"""
