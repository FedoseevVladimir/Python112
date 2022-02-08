# Задание 1
import random


def slicer(x, y):
    if y in x:
        if x.count(y) > 1:
            start = x.index(y)
            stop = x.index(y, start + 1)
            return x[start:stop + 1]
        else:
            return x[x.index(y):]
    else:
        return ()


t = (1, 8, 3, 4, 8, 8, 9, 2)
g = (1, 2, 3)
h = (1, 2, 8, 5, 1, 2, 9)
print(t)
print(g)
print(h)
b = 8
print(b)
print(slicer(g, b))
print(slicer(t, b))
print(slicer(h, b))
print()
print()
print()
print()
print('Задание 2')


#  Задание 2
def cort(x, y):
    res = tuple(random.randint(x, y) for i in range(10))
    return res


def zero(x):
    z = x.count(0)
    return z


a = (cort(-5, 0))
f = (cort(0, 5))
print(a)
print(f)
m = a + f
print('m =', m)
print('0 =', zero(m))
