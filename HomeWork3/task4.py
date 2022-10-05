# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def convert_num(count):
    if count < 0:
        return "Error"
    num = 0
    result = 0
    while count > 0:
            for i in range(count):
                num = (count % 2) * 10**i
                result += num
                count //= 2
    print(f'Двоичное число: ', result)

num = int(input('Введите чило: '))
convert_num(num)