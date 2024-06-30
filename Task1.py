# Задача №1. Решение в группах

# Требуется найти N-е число Фибоначчи

# Input: 7
# Output: 21

# Задание необходимо решать через рекурсию

# 0 1 1 2 3 5 8 13 21

a = 7
fibo_p, fibo_n = 0, 1
for i in range(0, a):
    fibo_p, fibo_n = fibo_n, fibo_p + fibo_n
print(f'{a}-е число = {fibo_n}')

# Рекурсия:

def func(a, fibo_p=0, fibo_n=1):
    if a == 0:
        return fibo_n
    return func(a-1, fibo_n, fibo_p + fibo_n) # шаг рекурсии (меняем все значения)
print(func(7))
