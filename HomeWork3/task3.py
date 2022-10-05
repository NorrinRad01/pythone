# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем

from random import uniform

def num_list(count):
    my_list = list()
    if count < 0:
        return "Error"
    for i in range(count):
        num = round(uniform(1, 10), 2)
        my_list.append(num)
    print(f'Список: ', my_list)
    min = 1
    max = 0
    dif = 0
    for i in range(count):
        if (my_list[i] % 1) < min:
            min = round((my_list[i] % 1), 2)
        if (my_list[i] % 1) > max:
            max = round((my_list[i] % 1), 2)
    dif = round(max - min, 2)
    print(f'Разница между максимальным и минимальным:', dif)

num = int(input('Введите чило: '))
num_list(num)