# задание:
# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

""" lambda """
# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# print(res)
# res = where(lambda x: not x % 2, res)
# print(res)
# res = select(lambda x: (x, x**2), res)

# print(res)
""" работа с файлом """
# f = open('file.txt', 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []

# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))

# print(out)

""" функция "map" """
# li = [i for i in range(1, 10)]
# print(li)

# li = list(map(lambda i:i+10, li))
# print(li)

""" функция "filter" """
# data = [x for x in range(10)]
# print(data)
# res = list(filter(lambda x: x % 2 == 0, data))

# print(res)

""" использование вместе все 3 функции(map, lambda, filter) """

# data = '1 2 3 5 8 15 23 38'.split()

# res = list(map(int, data))
# print(res)

# res = list(filter(lambda x: not x % 2, res))
# print(res)

# res = list(map(lambda x: (x, x**2), res))
# print(res)


""" функция "zip" """

# users = 'user1', 'user2', 'user3', 'user4', 'user5', 'user6'
# ids = [1, 2, 3, 4, 5, 6]

# data = list(zip(users, ids))
# print(data)

""" функция "enumarate"(пронумерование) """
# print()
# users = 'user1', 'user2', 'user3', 'user4', 'user5', 'user6'
# data = list(enumerate(users))
# print(data)
# print('__________')
# ids = [1123323, 12345, 234, 334, 2345, 333]
# data = list(enumerate(ids))
# print(data)