""" Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. """

def simples(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(n):
    if simples(n) and n > 200:
        print(n)
        return

    lst_of_simples = [2, 3, 5]
    for i in range(8, 10000):
        if simples(i):
            lst_of_simples.append(i)
    result_list = []
    while n > 1:
        for i in range(len(lst_of_simples)):
            if n % lst_of_simples[i] == 0:
                result_list.append(lst_of_simples[i])
                n /= lst_of_simples[i]
                break

    print(result_list)

num = int(input('Введите число: '))
solution(num)