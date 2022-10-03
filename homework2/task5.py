# Реализуйте алгоритм перемешивания списк

from time import time

lister = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(lister,'список')
def mix_list(old: list) -> list:
    new = []
    while old:
        x = str(time()).split('.')[1]
        x = list(map(int, [x[0], x[-1]]))
        x = x[0] if x[0] <= x[1] else x[1]
        if x > len(old)-1:
            new.append(old.pop(0))
        else:
            new.append(old.pop(x))
    return new

lister = mix_list(lister)
print(lister,'Перемешанный список')

