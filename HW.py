# ЗАДАНИЕ 1
# import math
#
# q = int(input("Площадь чего будем находить: 1 - прямоугольник, 2 - треугольник, 3 - круг: "))
#
#
# def rect(x, y):
#     s = a * b
#     return s
#
#
# def tria(x, y):
#     s = 0.5 * a * h
#     return s
#
#
# def circle(x):
#     s = math.pi * r
#     s = round(s, 2)
#     return s
#
#
# if q == 1:
#     print("Найдем площадь прямоугольника через длину и ширину ")
#     a = int(input("Длина: "))
#     b = int(input("Ширина: "))
#     print("S = ", rect(a, b))
# elif q == 2:
#     print("Найдем площадь треугольника через основание и высоту ")
#     a = int(input("Основание: "))
#     h = int(input("Высота: "))
#     print("S = ", tria(a, h))
# elif q == 3:
#     print("Найдем площадь круга через радиус ")
#     r = int(input("Радиус: "))
#     print("S = ", circle(r), " (округлено до 2х знаков после запятой)")


# ЗАДАНИЕ 2
a = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
s = a
print('a =', a)
not_s = []
for i in a:
    for j in range(2, i):
        if i % j == 0:
            not_s.append(i)
            break
        # else:
        #     s.append(i)
        #     break
        #  если эту часть кода оставлять, то элемент "9" аппендится в список "s" - простые числа
        #  я буквально 4 дня думал как сделать, чтобы выдавало только простые числа
        #  только такое решение смог сделать
for i in not_s:
    for j in s:
        if j == i:
            s.remove(j)
            break
for i in s:
    if i == 1:
        s.remove(i)
not_s.sort(reverse=True)
s.sort()
print("MIN: ", s[0])
print("MAX: ", not_s[0])
print('Числа не являющиеся простыми списка: ', not_s)
print('Простые числа списка: ', s)


