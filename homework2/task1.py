# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = int(input("Введите число: "))

print(f"Сумма цифр = {sumNums(num)}")