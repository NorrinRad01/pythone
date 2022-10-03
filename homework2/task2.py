# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input("Введите число: "))
def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


list = []
for i in range(1, num + 1):
    list.append(mult(i))

print(f"Произведения чисел от 1 до {num}:  {list}")