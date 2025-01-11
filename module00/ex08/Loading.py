def ft_tqdm(lst: range) -> None:
    for i in lst:
        if i % 20 == 0:
            print()
        yield i


from time import sleep
from tqdm import tqdm

#for elem in ft_tqdm(range(100)):
#    print(elem)
#    sleep(0.005)
#print()

for elem in tqdm(range(100), ascii=True):
#    print(elem, end='\r')
    sleep(0.005)
print()
