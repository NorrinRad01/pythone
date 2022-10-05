# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции

from random import sample
def list(count):
    if count < 0:
        return "Error"
    my_list = sample(range(1, count * 2), count)
    print(my_list)
    summ = 0
    for i in range(count):
        if i % 2 == 0:
            summ += my_list[i]
    print(f'Сумма элементов на нечетных позициях: ', summ)

num = int(input('Задайте количество элементов списка: '))
list(num)

