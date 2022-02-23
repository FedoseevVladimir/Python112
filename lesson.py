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

# frozenset - вид множества которое не может быть изменено
# s = frozenset([1, 2, 3, 4])
# print(s)
# a = frozenset({"Hello world"})
# print(a)
# b = frozenset({i ** 2 % 4 for i in range(10)})
# print(b)


#  dict (Словарь)


# ls = ['один', 'два']
# print(ls[0])
# d = {'one': 'один', 'two': 'два'}
# print(d['one'])


# одно и то же
# d = {}
# d1 = dict()


# два синтаксиса записи
# d = {'one': 'один', 'two': 'два'}
# print(d)
# di = dict(one="один", two="два")
# print(di)


# d3 = dict.fromkeys(['a', 'b'], 100) # {'a': 100, 'b': 100}
# print(d3)


# users = (
#     ('igor@gmail.com', 'Igor'),
#     ('ann@gmail.com', 'Ann'),
#     ('irina@gmail.com', 'Irina')
# )
# print(users)
# d_users = dict(users)
# print(d_users)


# d4 = {i: i ** 2 for i in range(1, 7)}
# print(d4)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# print(d4[5])  # 25
# d4[5] = 50 * 2
# print(d4)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 100, 6: 36}


# в качестве ключа нельзя использовать изменяемые данные, например список нельзя
# d5 = {0: 'text1', 'one': 45, (1, 2, 3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d5[42][1])  # 3
# print(d5[1, 2, 3])  # кортеж
# del d5[1, 2, 3] # удаляет ключ и значение
# print('one' in d5) # проверям есть ли ключ 'one' True
# if 'one' in d5:
#     print('True') # True


# d5 = {0: 'text1', 'one': 45, (1, 2, 3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# key = 'one1'
# # if key in d5: # если такой ключ есть
# #     del d5[key] # то удалить его из словаря
# try:
#     del d5[key]
# except KeyError:
#     print('Элемента с таким ключем нет в словаре')
# print(d5)


# d6 = {'one': 1, 'two': 2, 'three': 3}
# for key in d6:
#     print(key, '->', d6[key])
# выводит:
# one -> 1
# two -> 2
# three -> 3


# перемножаем ключи словаря
# d7 = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# d = 1
# for key in d7:
#     d *= d7[key]
# print(d)

# d = dict()
# d[1] = input('-> ')
# d[2] = input('-> ')
# d[3] = input('-> ')
# d[4] = input('-> ')
# print(d)

# d1 = {i: input('-> ') for i in range(1, 5)}
# print(d1)
# a = int(input('Исключить: '))
# del d1[a]
# print(d1)

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
# for country in countries:
#     if country in capitals:
#         print('Столица страны '+country+': '+capitals[country])
#     else:
#         print('В базе нет страны с названием: '+country)


# меняю количество по ключу
# goods = {'1': ['Core-i3-4330', 9, 4500],
#          '2': ['Core-i5-4670', 3, 8500],
#          '3': ['AMD FX-6300', 6, 3700],
#          '4': ['Pentium G3220', 8, 2100],
#          '5': ['Core-i5-3450', 5, 6400],
#          }
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. ', goods[i][2], 'руб', sep='')
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         q = int(input("Количество: "))
#         goods[n][1] = q
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. ', goods[i][2], 'руб', sep='')


# d = {'A': 1, 'B': 2, 'C': 3}
# x = iter(d)
# print(x)
# print(list(x)) # ['A', 'B', 'C']
# d.clear() # удаляет все элементы из словаря, но не удаляет словарь
# d2 = d.copy() # копирует словарь


# d = {'A': 1, 'B': 2, 'C': 3}
# value = d.get('B') # получить элемент по ключу
# value2 = d.get('E', 'FF') # устанавливаем значение поумолчанию для элемента если его нет
# print(value)
# print(value2)
# new = d.items() # dict_items([('A', 1), ('B', 2), ('C', 3)])
# print(new)
# a = d.keys() # dict_keys(['A', 'B', 'C']), список ключей
# print(a)
# item = d.pop('B', 5) # удаляет по ключу элемент и ключ и сохр его в переменной
# item1 = d.pop('E', 10) # вернет не ошибку а значение указанное вторым
# print(item)
# print(d)
# item = d.popitem() # удаляет из словаря и возвр. случайный элемент
# print(item)
# print(d)
# item = d.setdefault('C') # Возвращает значение ключа
# print(item)
# print(d)
# d.update([('R', 7), ('Q', 9)])  # добавляет новый ключ + значение, или обновляет значение если есть такой ключ
# print(d)


# складываем два словаря и обновляем элементы с уже имеющимся ключем
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# c = {'b': 5}
# # z = x.copy()
# # z.update(y)
# z = x | y | c # объединяет словари
# print(z)

# d = {'A': 1, 'B': 2, 'C': 3}
# v = d.values() # dict_values([1, 2, 3]) список значений
# print(list(v)) # [1, 2, 3]

# # 1
# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# b = {'name': 'Kelly', 'salary': 8000}
# for key in list(iter(a)):
#     for keys in b.keys():
#         if key == keys:
#             del a[key]
# print(a)
# print(b)
#
# # 2
# a['location'] = a.pop('city')
# print()
# print(a)


# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# b = dict()
# a['name'] = b.pop('name')
# a['salary'] = b.pop('salary')
# print(a)
# print(b)


# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for i in a:
#     print(i)
#     for j in a[i]:
#         print('\t', j, ': ', a[i][j], sep="")
#
# a = {
#     'John': {
#         'N': '3056',
#         'S': '8463',
#         'E': '8441',
#         'W': '2694'
#     },
#     'Tom': {
#         'N': '4832',
#         'S': '6786',
#         'E': '4737',
#         'W': '3612'
#     },
#     'Anne': {
#         'N': '5239',
#         'S': '4802',
#         'E': '5820',
#         'W': '1859'
#     },
#     'Fiona': {
#         'N': '3904',
#         'S': '3645',
#         'E': '8821',
#         'W': '2451'
#     }
# }
# for i in a:
#     print(i)
#     for j in a[i]:
#         print('\t', j, ': ', a[i][j], sep="")
#
# b = input("Имя: ")
# d = input("Регион:")
# print(a[b][d])
# a[b][d] = input('Нужное значение: ')
# print(a[b])


# a = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# b = {key: key for key in a} # {'один': 'один', 'два': 'два', 'три': 'три', 'четыре': 'четыре'}
# b = {key: value for key, value in a.items()} # {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# b = {value: key for key, value in a.items() if value <= 2} # {1: 'один', 2: 'два'}
# print(b)
# s = [10, 20, 30, 40]
# s = "hello"
# a = {i: i * 5 for i in s} # {'h': 'hhhhh', 'e': 'eeeee', 'l': 'lllll', 'o': 'ooooo'}
# print(a)

# v = int(input('->'))
# s = [10, 20, 30, 40]
# a = {i: v for i in s} # {10: 1, 20: 1, 30: 1, 40: 1}
# print(a)


# s = [10, 20, 30, 40]
# a = {i: int(input('->')) for i in s} # {10: 1, 20: 2, 30: 3, 40: 4}
# print(a)

# figure = {1: 'Rect', 2: 'Tria', 3: 'Circle'}
# print((list(figure))) # [1, 2, 3]
# print(list(figure.values())) # ['Rect', 'Tria', 'Circle']
# print(list(figure.items())) # [(1, 'Rect'), (2, 'Tria'), (3, 'Circle')]

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d) # {'one': [1, 2, 3], 'two': [10, 20], 'three': [15, 36, 60], 'four': [-20]}


# d = zip([1, 2, 3], ['one', 'two', 'three']) # первый список - ключи, второй - вэлью
# print(dict(d)) # {1: 'one', 2: 'two', 3: 'three'}


# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# f = {k: v for k, v in zip(b, a)}
# print(f) # {12: 'Dec', 1: 'Jan', 2: 'Feb'}
# z = zip(a,b)
# print(list(z)) # [('Dec', 12), ('Jan', 1), ('Feb', 2)]


# print(list(zip(range(2, 5), range(100)))) # [(2, 0), (3, 1), (4, 2)]


# a = {'a': 1, 'b': 2, 'c': 3}
# b = {'a': 11, 'b': 22, 'c': 33}
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)
# ВЫВОД:
# a -> 1
# a -> 11
# b -> 2
# b -> 22
# c -> 3
# c -> 33


# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs) # * распаковка кортежа
# print(a) # (1, 2, 3, 4)
# print(b) # ('a', 'b', 'c', 'd')


# a = [1, 2, 3, 4]
# b = ['a', 'b', 'c', 'd']
# data = list(zip(a,b))
# print(data) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# data.sort()
# print(data)


# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# production_cost = [46800.00, 45900.00, 43200.00]
# for sales, cost, m in zip(total_sales, production_cost, month):
#     res = sales - cost
#     print('Общая прибыль в', m, '=', res)
# ВЫВОДИТ:
# Общая прибыль в January = 5200.0
# Общая прибыль в February = 5100.0
# Общая прибыль в March = 4800.0


# one = {'apple': 0.04, 'orange': 0.35}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**two, **one}) # {'pepper': 0.2, 'onion': 0.55, 'apple': 0.04, 'orange': 0.35}
# for k, v in {**two, **one}.items():
#     print(k, '->', v)
# выводит:
# pepper -> 0.2
# onion -> 0.55
# apple -> 0.04
# orange -> 0.35


# colors = ['red', 'green', 'blue']
# ind = 1
# for color in colors:
#     print(str(ind) + ')', color)
#     ind += 1
#
# print()
# for i, color in enumerate(colors, 1):
#     print(str(i) + ')', color)


# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# for i, (j, q) in enumerate(d.items(), 1):
#     print(i, ': ', j, q, sep='')
# # ВЫВОДИТ
# 1: a1
# 2: b2
# 3: c3
# 4: d4


# d = {
#     1: {'a': 1, 'b': 2, 'c': 3, 'd': 4},
#     2: {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# }
#
# for i, k in enumerate(d):
#     print(i, ') key=', k, ', value=', d[k], sep='')
# 0) key=1, value={'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 1) key=2, value={'a': 10, 'b': 20, 'c': 30, 'd': 40}


# num = [1, 2, 3, 4, 5]
# itr = iter(num)
# print(itr)
# print(next(itr)) # 1
# print(next(itr)) # 2
# print(next(itr)) # 3
# print(next(itr)) # 4
# print(next(itr)) # 5
# print(next(itr, 'STOP')) # STOP


# a = [6, 7, 3, 4, 1, 5]
# b = enumerate(a)
# c = next(b)
# c1 = next(b)
# print(c)
# print(c1)


# # 1
# print()
# color = ['red', 'green', 'blue']
# color_num = ['#FF0000', '#008000', '#0000FF']
# c = dict(zip(color, color_num))
# print(c)  # {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
# print()
#
# # 2
# a = {i: i * i * i for i in range(1, 11)}
# print(a)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
# print()
#
# # 3
# d1 = ['color', 'fruit', 'pet']
# d2 = ['blue', 'apple', 'dog']
# d = {x: y for x, y in zip(d1, d2)}
# print(d)  # {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# print()
#
#
# # 4
#
#
# def mi_n(s):
#     return min(s)
#
#
# print(mi_n([10, 9]))  # 9
# print(mi_n([2, 3, 4]))  # 2
# print(mi_n([3, 5, 10, 6]))  # 3
# print()
#
# # 5
# a = [3, 5, 10, 6, 3]
#
#
# def su_m(s):
#     c = a[0]
#     d = len(a) + 1
#     for elem in range(d):
#         print(c, end=' ')
#         c += a[elem + 1]
#
#
# print(su_m(a))

# a = [1, 2, 3]
# b = [*a, 4, 5, 6] # [1, 2, 3, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(1))  # (1,)
# print(func(1, 3, 5, 'abc'))  # (1, 3, 5, 'abc')
# print(func())  # ()


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
# a = summa(1,2,3,4,5,6,7)
# b = summa(1,2,3)
# print(a)
# print(b)


# def func(*a):
#     return {i: i for i in a}
#
#
# print(func(1, 2, 3, 4)) # {1: 1, 2: 2, 3: 3, 4: 4}


# def funct(*a):
#     r = (sum(a) / len(a))
#     d = []
#     for i in a:
#         if i < r:
#             d.append(i)
#     print(d)
#     print(r)
#
#
# print(funct(1, 2, 3, 4, 5, 6, 7, 8, 9))


# def func(a, *args):
#     return a, args
#
#
# print(func(1,2,3, 'abc')) # (1, (2, 3, 'abc'))


# def func(student, *scores):
#     a = 'Student name: ' + student
#     s = []
#     for score in scores:
#         s.append(score)
#     print(a, end=' ')
#     print(*s, sep=', ')
#
#
# func('Igor', 100, 95, 88, 92, 99)
# func('Rick', 69, 96, 20, 33)
# # Воводит
# # Student name: Igor 100, 95, 88, 92, 99
# # Student name: Rick 69, 96, 20, 33
#
# def func(student, *s):
#     print('Student name: ' + student, end=' ')
#     print(*s, sep=', ')
#
#
# func('Igor', 100, 95, 88, 92, 99)
# func('Rick', 69, 96, 20, 33)
# # Воводит
# # Student name: Igor 100, 95, 88, 92, 99
# # Student name: Rick 69, 96, 20, 33

# # перевернуть элемент
# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2 != 0):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}


# def info(**data):
#     for key, value in data.items():
#         print(key, 'is', value)
#     print()
#
#
# info(firstname='Irina', lastname='Saunal', age=22, phone=2334212)
# info(firstname='Irina', lastname='Wood', email='igor12@mail.ru', age=22, phone=2334212, country='Rus')
# ВЫВОД:
# firstname is Irina
# lastname is Saunal
# age is 22
# phone is 2334212
#
# firstname is Irina
# lastname is Wood
# email is igor12@mail.ru
# age is 22
# phone is 2334212
# country is Rus


# функция добавляет в словарь любое количество элементов
# def db(**kwargs):
#     my_dict.update(**kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, width=61, eyes_color='gray')
# print('m = ', my_dict)


# def func(a, *args, b=False, **kwargs):
#     return a, args, b, kwargs
#
#
# print(func(1,2,3,4, b=True, x=11, y=12, z=13))


# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5, 6)
# func2(one=123, two=456)


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, 'one': 1, 'two': 2, **y}
# print(z)


# scope - область видимости функции

# name = 'Tom' # ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ
#
#
# def hi():
#     global name # ДЕЛАЕТ ПЕРЕМЕННУЮ ГЛОБАЛЬНОЙ, ПИШЕТСЯ ВЫШЕ ПЕРЕМЕННОЙ
#     name = 'Sam' # ЛОКАЛЬНАЯ ПЕРЕМЕННАЯ
#     print('Hello', name)
#
#
# def bye():
#     print('Good bye', name)
#
#
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()


# def add_two(a):
#     x = 2
#
#     def add_some():
#         print('x = ' + str(x))
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))

# def outer_func(who):
#     def inner_func():
#         print('Hello,', who)
#
#     inner_func()
#
#
# outer_func('World!')

# def func1():
#     a = 6
#
#     def func2(b):
#         a = 4
#         print('СУмма внутр функции:', a + b)
#
#     print('Значение внешней переменной а:', a)
#
#     func2(4)
#
# func1()

# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#     print('global:', x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print(a)
#
#     inner()
#     print(a)
#     t = a
#
#
# fn()
# z = x + t
# print(z)


# def fn1():
#     x1 = 25
#
#     def fn2():
#         x1 = 33
#
#         def fn3():
#             nonlocal x1
#             x1 = 55
#         fn3()
#         print('fn2.x1 = ', x1)
#     fn2()
#     print('fn1.x1 = ', x1)
#
#
# fn1()



# def func(figure_type='figure', **data):
#     res = 1
#     if figure_type == 'rhombus':
#         res = (data['d1'] * data['d2']) / 2
#         return res
#     elif figure_type == 'square':
#         res = data['a'] * data['a']
#         return res
#     elif figure_type == 'trapezoid':
#         res = 0.5 * ((data['a'] + data['b']) * data['h'])
#         return res
#     elif figure_type == 'circle':
#         res = 3.14 * (data['r'] ** 2)
#         return res
#     else:
#         a = 'invalid data'
#         return a
#
#
# print(func(figure_type='rhombus', d1=10, d2=8))
# print(func(figure_type='square', a=5))
# print(func(figure_type='trapezoid', a=12, b=3, h=6))
# print(func(figure_type='circle', r=18))
# print(func(figure_type='unknown', a=1, b=2, c=3))
#
# # выводит:
# # 40.0
# # 25
# # 45.0
# # 1017.36
# # invalid data