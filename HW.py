# # 1
print('Функция принимает аргумент и умножает его на заданное число')


def func_compute(n):
    def inner(x):
        return n * x

    return inner


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))
print()
# # 2
print('Произведение трёх чисел через lambda')
print((lambda x: (lambda y: (lambda z: x * y * z)))(2)(5)(5))
print()
# 3
s = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98},
]
print('Сортировка по "name":')
s1 = sorted(s, key=lambda d: d['name'])
print(s1)
print('Сортировка по "final":')
s2 = sorted(s, key=lambda d: d['final'], reverse=True)
print(s2)
