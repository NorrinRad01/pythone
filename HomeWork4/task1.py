""" Вычислить число c заданной точностью *d* """
num = float(input('Введите число для точности: '))

def accuracy(n):
    list = [0.1]
    for i in range(10):
        list.append(list[i] / 10)
    while True:
        accuracy = float(input('Введите требуемую точность от 0,1 до 0,0000000001: '))
        if accuracy not in list:
            print('Введите правильную точность')
        else:
            break
    count = 0
    while accuracy < 1:
        accuracy *= 10
        count += 1
    return round(n, count)

print(accuracy(num))