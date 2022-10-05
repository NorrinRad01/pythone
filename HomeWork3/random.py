# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

def myrandint(start, end, seed=999999999):
    a = 32310901  
    b = 1729
    rOld = seed
    m = end-start
    while True: 
        rNew = (a*rOld+b)%m
        yield rNew
        rOld=rNew
        
for i in range(4):
    r = myrandint(1,100,  i)
    print()
    print(f'({i})','Рандомные числа:')
    for j in range(10):
        print( next(r),end=',' )
    print(      )
 
