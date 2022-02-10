# print("Hello World, I'am on GitHub")
# sep=""   убирает пробелы
#
#
# def hello(name, word):  # аргументы
#     print("Hello, ", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi")  # параметры
# hello("Ivan", "hello")
#
#
# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")  # если слова то делается конкатенация
# get_sum(2.5, 4.3)
# # get_sum(2.5, "4.5")  # разные типы данных нельзя складывать
#
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")


# ПЕРВЫЙ ВАРИАНТ
# def symbol(num, s1, s2):
#     for ch in range(num):
#         if ch % 2 == 0:
#             print(s1, end='')
#         else:
#             print(s2, end='')
#     print()


# ВТОРОЙ ВАРИАНТ
# def symbol(x,y,z):
#     s=''
#     for i in range(x):
#         if i%2==0:
#             s+=y
#         else:
#             s+=z
#     print(s)


# symbol(9, "+", "-")
# symbol(7, "X", "0")

# ВЫВОДИТ
# +-+-+-+-+-+-+-+-+-
# X0X0X0X0X0X0X0


# def get_sum(a, b):
#     return a + b  # RETURN ВОЗВРАЩАЕТ РЕЗУЛЬТАТ
# #    print('Строка')  #  ЕСЛИ НАПИСАН КОД ПОСЛЕ RETURN ОН НЕ БУДЕТ ОТРАБАТЫВАТЬ
#
#
# n = 2
# m = 5
# res = get_sum(n, m)  # СОХРАНЯЕМ РЕЗУЛЬТАТ ФУНКЦИИ В ПЕРЕМЕННУЮ
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     elif two > one:
#         return two
#     else:
#         return
#
#
# m = maximum(9, 9)
# print(m)


# ЗАПРАШИВАЕТ ДВА ЧИСЛА И ВЫВОДИТ РЕЗУЛЬТАТ В ЗАВИСИМОСТИ ОТ ЗНАЧЕНИЙ
# a = int(input("One: "))
# b = int(input("Two: "))
#
#
# def add(one, two):
#     if one > two:
#         return one - two
#     elif two > one:
#         return one + two
#     else:
#         return
#
#
# m = add(a, b)
# print(m)

# ФУНКЦИЯ ОТРАБАТЫВАЕТ В ЦИКЛЕ
# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# РЯД ФИБОНАЧЧИ (КАЖДОЕ СЛЕД ЧИСЛО = СУММЕ ДВУХ ПРЕДЫДУЩИХ
# 0 1 1 2 3 5 8

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         a, b = b, a + b
#
#
# fib(1000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987


# ВАРИАНТ 2
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#
#
# fib(15)


# меняет первый и последний элементы списка местами
# def change(s):
#     s[0], s[-1] = s[-1], s[0]
#     return s
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))
# ВОЗВРАЩАЕТ:
# [3, 2, 1]
# [105, 12, 33, 54, 9]
# ['н', 'л', 'о', 'с']

# ВАРИАНТ 2
# def change(lst):
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))
# ВОЗВРАЩАЕТ:
# [3, 2, 1]
# [105, 12, 33, 54, 9]
# ['н', 'л', 'о', 'с']


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
# a = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
# s = a
# print('a =', a)
# not_s = []
# for i in a:
#     for j in range(2, i):
#         if i % j == 0:
#             not_s.append(i)
#             break
# else:
#     s.append(i)
#     break
#  если эту часть кода оставлять, то элемент "9" аппендится в список "s" - простые числа
#  я буквально 4 дня думал как сделать, чтобы выдавало только простые числа
#  только такое решение смог сделать
# for i in not_s:
#     for j in s:
#         if j == i:
#             s.remove(j)
#             break
# for i in s:
#     if i == 1:
#         s.remove(i)
# not_s.sort(reverse=True)
# s.sort()
# print("MIN: ", s[0])
# print("MAX: ", not_s[0])
# print('Числа не являющиеся простыми списка: ', not_s)
# print('Простые числа списка: ', s)

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))


#  ФУНКЦИЯ ПРОВЕРКИ ПАРОЛЯ НА СЛОЖНОСТЬ
# def check_pass(passw):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in passw:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(passw) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input('Введите: ')
# if check_pass(p):
#     print('Надежный пароль')
# else:
#     print('Не надежный пароль')


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, d=2))  # 8, c отрабатывает как 0


# def set_param(x=20, y='-'):
#     print(y * x)
#
#
# set_param(10, '+')  # ++++++++++
# set_param()  # --------------------
# set_param(5, '*')  # *****


# def check_password(username, password, min_length=8, check_user=True):
#     if len(password) < min_length:
#         print('Pass is small')
#         return False
#     elif check_user and username in password:
#         print('Pass got is username')
#         return False
#     else:
#         print('Пароль пользователя', username, 'прошел все проверки')
#         return True
#
#
# check_password('igor', '12345')
# check_password('igor', '12345igor')
# check_password('igor', '12345name')


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur = n % 10
#         if even and cur % 2 == 0:
#             s += cur
#         elif not even and cur % 2 != 0:
#             s += cur
#         n //= 10
#     return s
#
#
# print('Сумма четных цифр: ')
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print('Сумма НЕчетных цифр: ')
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print('Name: ', name, '\nAge: ', age, '\n')
#
#
# display_info('Ira', 23)
# display_info(23, 'Ira')
# display_info(age=23, name='Ira')
# display_info('Igor', age=23, name='Ira') # нельзя 2 значения name


# def func(a, ln=[]):
#     ln.append(a)
#     return ln
#
#
# print(func(1))  # [1]
# print(func(2))  # [1, 2]
# print(func(3))  # [1, 2, 3]


# # ТАК ДЕЛАТЬ ПРАВЕЛЬНЕЕ!!!
# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
#
#
# print(func(1))  # [1]
# print(func(2))  # [2]
# print(func(3))  # [3]


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False


# def add_number(n):
#     print('Внутри функции: ', n, '=', id(n))
#     n += [4]
#     print('После присвоения: ', n, '=', id(n))
#
#
# x = [1, 2, 3]
# print(x, '=', id(x))
# add_number(x)
# print(x, '=', id(x))


# Кортеж (tuple)
# lst = [10, 20, 30]
# tp = (10, 20, 30)
# print(lst.__sizeof__()) # 104 bite
# print(tp.__sizeof__()) # 48 bite


# a = (1, 2, 3, 4, 5)
# print(a)
# print(type(a))  # <class 'tuple'>
# b = 1, 2, 3
# print(tuple(b))
# print(type(b))  # <class 'tuple'>
# print(tuple((1, 2, 3)))


# t = (1,)
# print(type(t))

# t = tuple('hello')
# print(t)
# print(type(t))

# a = tuple((1, 2, 3, 4, 5))
# print(a)
#
# print(a[1:3])  # срез картежа

# s1 = tuple(int(input("-> ")) for i in range(1, 3))
# print(s1)

# import random
#
# s1 = tuple((2 ** i for i in range(1, 13)))
# # (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096)
# print(s1)


# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
# print(t3)
# print(len(t3))


# Задание 1, кортеж срезает значением y при разных условиях
# import random
#
#
# def slicer(x, y):
#     if y in x:
#         if x.count(y) > 1:
#             start = x.index(y)
#             stop = x.index(y, start + 1)
#             return x[start:stop + 1]
#         else:
#             return x[x.index(y):]
#     else:
#         return ()
#
#
# t = (1, 8, 3, 4, 8, 8, 9, 2)
# g = (1, 2, 3)
# h = (1, 2, 8, 5, 1, 2, 9)
# print(t)
# print(g)
# print(h)
# b = 8
# print(b)
# print(slicer(g, b))
# print(slicer(t, b))
# print(slicer(h, b))
# print()
# print()
# print()
# print()
# print('Задание 2')
#
#
# #  Задание 2, создает два кортежа, складывает их и показывает кол-во 0
# def cort(x, y):
#     res = tuple(random.randint(x, y) for i in range(10))
#     return res
#
#
# def zero(x):
#     z = x.count(0)
#     return z
#
#
# a = (cort(-5, 0))
# f = (cort(0, 5))
# print(a)
# print(f)
# m = a + f
# print('m =', m)
# print('0 =', zero(m))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# from random import randint

#  выводит кортеж с уникальными элементами
# def func(s):
#     ls = []
#     for i in s:
#         if i not in ls:
#             ls.append(i)
#
#     return tuple(reversed(ls))
#
#
# a = [1, 2, 3, 3, 2]
# print(func(a))

# def func(s):
#     ls = []
#     [ls.append(i) for i in reversed(s) if i not in ls]
#     return tuple(ls)
#
#
# a = [1, 2, 3, 3, 2]
# print(func(a))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t # распаковка кортежа
# print(x, y, z)
#
#
# def get_user():
#     name = 'Tom'
#     age = '22'
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)  # ('Tom', '22', False)
# n, a, i = user
# print(n, a, i)  # Tom 22 False
# print(user[0])  # Tom

# t = (1, 2, 3)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5]
# print(type(lst))
# print(lst)
# tp = tuple(lst)
# print(type(tp))
# print(tp)

# countries = (
#     ('Germany', 80.2, (
#         ('Berlin', 3.326),
#         ('Hamburg', 1.718))
#      ),
#     ('France', 66, (('Paris', 2.2), ('Marcel', 1.6)))
# )
#
# for country in countries:
#     country_name, country_population, cities = country
#     print('\n Страна:', country_name, 'Население =', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород: ', city_name, 'Население = ', city_population)


# s = {1, 2, 1, 2, 3, 2, 3, 8}
# print(type(s))
# print(s)
# # МНОЖЕСТВО (set)
# print(len(s))

# c = ['hello', 'hi']
# a = set(c)
# b = {'hello', 'hi'}
# print(b)

# s = {x for x in range(10) if x % 2 == 0}
# print(list(s))

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# print(list(set(numbers)))  # [1, 2, 3, 4, 5, 6]

# def to_set(x):
#     a = set(x)
#     b = len(a)
#     return a, b
#
#
# z = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
# print(to_set(z))

# t = {'red', 'green', 'blue'}
# # print('green' in t)
# for i in t:
#     print(i, end=' ')  # blue red green

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']

# ВАРИАНТЫ НАПИСАНИЯ В ОДНУ СТРОКУ
# # [res for() if]
# # [res if() else for()]
# # [res if() else for() if]


# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)


# a = {0, 1, 2, 3}
# a.add(4)  # добавляет элемент в множество
# a.remove(1)  # удаляет заданный элемент
# num = 2
# if num in a:
#     a.remove(num)
# a.discard(3)  # удаляет элемент если он там есть
# a.pop()  # удаляет элемент с нулевым индексом
# a.clear()  # отчистить множество, но переменная останется set()
# print(a)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)  # объединяет два множества
# c = a | b  # та же запись функции a.union(b)
# a |= b
# c = a & b  # выводит только повторяющиеся элементы
# c = a - b  # только элементы которые есть в а, но нету в b
# c = a.copy()
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s = set(s1 | s2 | s3 | s4 | s5 | s6 | s7)
# print(s)
# print('elem count: ', len(s))
# print('min: ', min(s))
# print('max: ', max(s))
# ВЫВОДИТ
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# elem count:  9
# min:  1
# max:  9


# ВЫВОДИТ ОБЩИЕ БУКВЫ ДВУХ СТРОК
# a = 'Hello'
# b = 'How are you'
# c = set(a) & set(b)
# for i in c:
#     print(i, end=' ')

# print('Задание 1 элементы первой строки которые отсутствуют во второй строке')
# a = 'Python'
# print('Первая строка: ', a)
# b = 'Programming language'
# print('Вторая строка: ', b)
# print('Искомыми буквами являются: ')
# c = set(a) - set(b)
# for i in c:
#     print(i, end=' ')
#
# print('\n\nЗадание 2 выводит количество гласных в строке')
# d = 'Hello world'
# print(d)
#
#
# def vowels(x):
#     count = 0
#     set_d = list(d)
#     vowels_str = ['a', 'e', 'i', 'o', 'u', 'y']
#     for i in x:
#         if i in vowels_str:
#             count += 1
#     return count
#
#
# print('Numbers of vowels: ', vowels(d))
#
# print('\n\nЗадание 3 общие элементы двух строк')
# str1 = 'test'
# print('Первая строка: ', str1)
# str2 = 'string'
# print('Вторая строка: ', str2)
# letter = set(str1) | set(str2)
# print('Искомые буквы: ')
# for i in letter:
#     print(i, end=' ')
#
# print('\n\nЗадание 4 только уникальные элементы двух строк')
# str3 = 'hello'
# print('Первая строка: ', str3)
# str4 = 'world'
# print('Вторая строка: ', str4)
# letter1 = set(str3) | set(str4)
# letter2 = set(str3) & set(str4)
# l = letter1 - letter2
# print('Искомые буквы: ')
# for i in l:
#     print(i, end=' ')
