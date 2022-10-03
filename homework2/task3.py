# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def SummNum(num):
    l = []
    i=0
    summ = 0
    while i < num:
        l.append((1+(1/(i+1))) ** (i+1))
        l[i] = round(l[i])
        summ = summ + l[i]
        i = i + 1
    print(f'Лист: ', end='')    
    print(l)
    print(f'Сумма чисел последовательности (1+1/n)^n = ', summ)

num = int(input('Введите число: '))
SummNum(num)