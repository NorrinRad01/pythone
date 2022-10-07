""" Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
исходной последовательности. """


uniq = str(input('Введите числа без пробелов: '))

def unique(n):
    list = []
    for i in range(len(uniq)):
        list.append(uniq[i])
    list.sort()
    print(f'ssss',list)
    for i in range(len(list)):
        try:
            if list[i] != list[i + 1] and list[i] != list[i - 1]:
                print(list[i], end=' ')
        except:
            if list[i] != list[i - 1]:
                print(list[i])
     
unique(uniq)