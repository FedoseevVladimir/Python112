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

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# локальная переменная
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + (rect_square(a, c) + (rect_square(c, b))))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# глобальная переменная
# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#     global s
#     s = 2 * (rect_square(a, b) + (rect_square(a, c) + (rect_square(c, b))))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(s)
# print(rect_paral_square(5, 8, 2))
# print(s)
# print(rect_paral_square(1, 6, 8))
# print(s)

# нелокальная переменная
# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i*j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(c, b)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# Замыкания
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner


# add5 = outer(5)
# print(add5(10)) # 15
# add6 = outer(6)
# print(add6(10)) # 16
# print(outer(5)(10)) # 15 - обычно такой синтаксис не используют
#
#
# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     i = 0
#
#     def city_name():
#         nonlocal i
#         i += 1
#         print(city, i)
#
#     return city_name
#
#
# res = func("Москва")
# res()
# res()
# res2 = func("Сочи")
# res2()
# res2()
# res()


# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'David': 85,
#     'Chris': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for (k, v) in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# a = outer(80, 100)
# b = outer(70, 80)
# c = outer(50, 70)
# d = outer(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))
# ВЫВОДИТ
# {'Alice': 98, 'David': 85}
# {'Chris': 75}
# {'Bob': 67, 'Ella': 54, 'Grace': 69}
# {'Fiona': 35}


# def func(x1, y1):
#     return x1 + y1
#
#
# print(func(1,2))
# print()
# print((lambda x, y: x + y)(1,2))
#
# func1 = lambda x, y: x + y
# print(func1(1,2))
# print(func1('a', 'b'))
# print((lambda x, y: (x * x) + (y * y))(2, 5))
# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ())
# print(summ(10))  # попадет в первое значение
# print(summ(b=10))
# print(summ(10, 20))


# func = lambda *args: args
#
# print(func(1,2,3,4))


# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
#
# for i in c:
#     print(i('abc,'))
# abc,abc,
# abc,abc,abc,
# abc,abc,abc,abc,

# def inc1(n):
#     return lambda x: x + n
#
#
# f = inc1(42)
# print(inc1(2))
# print((lambda n: (lambda x:x+n))(42)(2))

# print((lambda x: (lambda y: (lambda z: x + y + z)))(2)(4)(6)) # сумма чисел 12

# d = {'r':10, 'b': 15, 'c': 4}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[0]) # 0 сортировка по ключам, 1 - по значениям
# print(list_d)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[1](12, 6)  # a[index элемента](значение x, y)
# print(b)
# print(type((lambda x, y: x + y)))

# # 1
# print('Функция принимает аргумент и умножает его на заданное число')
#
#
# def func_compute(n):
#     def inner(x):
#         return n * x
#
#     return inner
#
#
# res = func_compute(2)
# print(res(15))
# print(res(20))
# res = func_compute(3)
# print(res(15))
# print(res(20))
# print()
# # # 2
# print('Произведение трёх чисел через lambda')
# print((lambda x: (lambda y: (lambda z: x * y * z)))(2)(5)(5))
# print()
# # 3
# s = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
# print('Сортировка по "name":')
# s1 = sorted(s, key=lambda d: d['name'])
# print(s1)
# print('Сортировка по "final":')
# s2 = sorted(s, key=lambda d: d['final'], reverse=True)
# print(s2)

# players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}]
#
# s1 = sorted(players, key=lambda d: d['rating'], reverse=True)
# print(s1)
#
# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {'circle': lambda x: print(3.14 * x * x),
#      'rectangle': lambda x, y: print(x * y),
#      'trapezoid': lambda a, b, h: print((a + b) * h / 2)}
# d['circle'](12)
# d['rectangle'](2, 5)
# d['trapezoid'](4, 7, 10)


# находит максимальное значение
# print((lambda a, b: a if a > b else b)(13, 12))
# print((lambda a, b, c: a if (a <= b) and (b <= c) else (b if (b <= a) and (b <= c) else c))(100, 13, 17))


# map(func, iterable)
# def mul(t):
#     return t * 2
#
#
# s = [2, 8, 12, -5, -8]
# s2 = 'hello'
# ls = list(map(mul, s)) # [4, 16, 24, -10, -16]
# ls2 = list(map(mul, s2))
# print(ls)
# print(ls2)

# тоже самое только короче через мэп и лямбду
# s = [2, 8, 12, -5, -8]
# print(list(map(lambda t: t * 2, s)))  # [4, 16, 24, -10, -16]
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -8])))  # [4, 16, 24, -10, -16]

# s = ['1', '2', '3', '4', '5']
# print(list(map(int, s)))

# areas = [3.554747, 5.5734536, 4.004564, 56.243464, 9.01355, 32.000245]
# res = list(map(round, areas, range(1, 7)))
# print(res)  # [3.6, 5.57, 4.005, 56.2435, 9.01355, 32.000245]

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2))) #  [5, 7, 9]

# filter(func, iterable)
# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# print(tuple(filter(lambda s: len(s) == 3, t)))  # ('abc', 'def', 'ghi')
# print(tuple(map(lambda s: len(s) == 3, t))) # (False, True, False, True, True)


# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# import random
#
# c = list(random.randint(1, 40) for i in range(10))
# res = list(filter(lambda i: 10 <= i <= 20, c))
# print(c)
# print(res)

# s = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda i: i % 15 == 0, s))
# print(res)

# s = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda i: not i % 15, s))
# print(res)

# квадраты нечетных чисел
# print(list(map(lambda x:x**2, filter(lambda x:x %2 != 0, range(10))))) # [1, 9, 25, 49, 81]
# print([x**2 for x in range(10) if x %2 !=0]) # [1, 9, 25, 49, 81]

# s = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
# print(list(filter(lambda i: i == i[::-1], s)))

# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#      return 'Hello, I am func "hello"'
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
# def func_test():
#     print('Hello i"m func')
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func): # это декоратор, декорирующая функция
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
# @my_decorator
# def func_test(): # декорируемая функция
#     print('Hello i"m func')
#
# func_test()
#
# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'
#
#
# print(hello()) # <b><i>text</i></b>


# def cnt(func):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         func()
#         print('Вызов функции:', count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()
# Hello
# Вызов функции: 1
# Hello
# Вызов функции: 2
# Hello
# Вызов функции: 3

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print('Данные:', arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
# @args_decorator
# def print_full_name(first, last):
#     print('Меня зовут', first, last)
#
#
# print_full_name('Ирина', 'Лаврова')


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args:', args)
#         print('kwargs:', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# print_full_name('БОрис', 'Елизавета', 'Светлана', study='JavaScript')
# print_full_name('Владимир', 'Екатерина', 'Виктор')
# # args: ('БОрис', 'Елизавета', 'Светлана')
# # kwargs: {'study': 'JavaScript'}
# # БОрис Елизавета Светлана изучают JavaScript
# #
# # args: ('Владимир', 'Екатерина', 'Виктор')
# # kwargs: {}
# # Владимир Екатерина Виктор изучают Python

# # 1
# a = [3, 6, 8, 9, 1, 2]
# print(list(map(lambda x: x * a.index(x) ** 3, a)))  # [0, 6, 64, 243, 64, 250]
# print()
# # 2
# b = [3, -4, -6, 7, -8, 3, -12, 4, 7]
# s = list(filter(lambda x: x < 0, b))
# print(s)
# print(abs(sum(s)))
# print()
# # 3
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
# print(list(map(lambda x: x ** 2, nums)))
# print(list(map(lambda x: x ** 3, nums)))
# print()
#
#
# # 4
# def func_compute(n):
#     def inner(x):
#         return n * x
#
#     return inner
#
#
# res = func_compute(2)
# print(res(15))
# print(res(20))
# res = func_compute(3)
# print(res(15))
# print(res(20))
# print()


# def args_dec(arg1, arg2):
#     print('Аргументы: ', arg1, arg2)
#
#     def wrapper(func1):
#
#         def wrap(func_arg1, func_arg2):
#             print('Аргументы функции: ', func_arg1, func_arg2)
#             func1(func_arg1, func_arg2)
#             func1(arg1, arg2)
#
#         return wrap
#
#     return wrapper
#
#
# @args_dec('Игорь', 'Нефедов') # Игорь Нефедов
# def func(first, last):
#     print('Меня зовут: ', first, last)
#
#
# func('Ирина', 'Лаврова')
# Аргументы:  Игорь Нефедов
# Аргументы функции:  Ирина Лаврова
# Меня зовут:  Ирина Лаврова
# Меня зовут:  Ирина Лаврова

# def args_dec(decorator_text):
#     def wrapper(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#
#         return wrap
#
#     return wrapper
#
#
# @args_dec(decorator_text='Hello, ')
# def hello_world(text):
#     print(text)
#
#
# @args_dec(decorator_text='Hi, ')
# def hello(text, t2):
#     print(text, t2)
#
#
# hello_world("world!")
# hello('Igor!', 'Irina!')

# def multiply(a):
#     def wrapper(func):
#         def wrap(b):
#             return a * func(b)
#
#         return wrap
#
#     return wrapper
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError('Некорректный тип данных')
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError('Некорректный тип данных')
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z='hello '):
#     return (x + y) * z
#
#
# print(typed_fn(3, 2, 5))
# # print(typed_fn(3, 2, 'Hello '))
# print(typed_fn2('Hello, ', 'world', '!'))
# print(typed_fn3('Hello, ', 'world ', z=2))
# # print(typed_fn3('Hello, ', 'world', z='2'))


# def decor(tx=None, dec_text=''):
#     def wrapper(func):
#         def wrap(*args):
#             print(dec_text, end='')
#             func(*args)
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
# @decor
# def hello_world2(text):
#     print(text)
#
# hello_world2('World!')
#
#
# @decor(dec_text = 'hello, ')
# def hello_world(text):
#     print(text)
#
# hello_world('World!')
#########################################################################
# ПОСМОТРЕТЬ
# https://www.youtube.com/playlist?list=PLKhF725nEal1za5jO8xSxbm9HyonmEGo-4
# https://github.com/Helen-prog/Python112/blob/master/112.py
#########################################################################

# print(bin(18)) # 0b10010
# print(oct(18)) # 0o22
# print(hex(18)) # 0x12
#
# print(0b10010) # 18
# print(0o22) # 18
# print(0x12) # 18

# q = 'Pyt'
# w = 'hon'
# print((q+w)*-3)
# s = 'hello'
# print(s[::-1])
# print(s[slice(2)]) # he
# print(s[slice(2, 5)]) # llo

# s = 'python'
# s = s[:3] + 't' + s[4:]
# print(s)

# def change_char_to_str(s, old, new):
#     s2 = ''
#     i= 0
#     while i < len(s):
#         if s[i] == old:
#             s2 = s2 + new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#     return s2
#
#
# str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный'
# str2 = change_char_to_str(str1, 'N', 'P')
# print('str1 = ', str1)
# print('str2 = ', str2)
# str1 =  Я изучаю Nython. Мне нравится Nython. Nython очень интересный
# str2 =  Я изучаю Python. Мне нравится Python. Python очень интересный

# # 1
# def decorator_sr(func):
#     def wrapper(*args):
#         val1 = func(*args)
#         val = val1 / len(args)
#         print('Cумма чисел ', *args, '=', val1)
#         print('Ср.арифм: ', *args, '=', val)
#
#     return wrapper
#
#
# @decorator_sr
# def summa(*args):
#     c = 0
#     for k in args:
#         c += k
#     return c
#
#
# summa(2, 3, 3, 4)
# # Cумма чисел  2 3 3 4 = 12
# # Ср.арифм:  2 3 3 4 = 3.0
# print()
#
#
# # 2
# def change_char_to_str(w, old, new):
#     s2 = ''
#     g = 0
#     while g < len(w):
#         if w[g] == old and g % 2 == 0:
#             s2 = s2 + new
#         else:
#             s2 = s2 + w[g]
#         g += 1
#     return s2
#
#
# str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный'
# str2 = change_char_to_str(str1, 'N', 'P')
# print('str1 = ', str1)
# print('str2 = ', str2)
# # str1 =  Я изучаю Nython. Мне нравится Nython. Nython очень интересный
# # str2 =  Я изучаю Nython. Мне нравится Python. Python очень интересный
# print()
#
#
# # 3
# def del_letter(x, arr):
#     for j in arr:
#         if x == arr.index(j):
#             pass
#         else:
#             print(j, end='')
#
#
# s = '0123456789'
# print('s = ', end='')
# for i in s:
#     print(i, end='')
# print()
# print('s2 = ', end='')
# del_letter(5, s)
# # s = 0123456789
# # s2 = 012346789
# print()
# print()
#
#
# # 4
# def func1(x, arr):
#     x = str(x)
#     for j in arr:
#         if x != j:
#             print(j, end='')
#
#
# s = '132333435363738393'
# print('s = ', end='')
# for i in s:
#     print(i, end='')
# print()
# print('s2 = ', end='')
# func1(3, s)
# # s = 132333435363738393
# # s2 = 12456789


# print('I\'m learning \nPython')
# print('C:\\file.txt')
# print(r'C:\file.txt') # - сырые строки(подавляют экранирование \)
# print(r'C:\file\\'[:-1]) # C:\file\
# print(r'C:\file' + '\\') # C:\file\
# print('C:\\file\\') # C:\file\

# name = 'Дмитрий'
# age = 25
# print('Меня зовут ', name, '. Мне ', age, ' лет.', sep='')
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет.')
# print(f'Меня зовут {name}. Мне {age} лет.')

# import math as m
#
# print(f'Значение числа pi: {m.pi:.2f}')  # Значение числа pi: 3.14
# print(f'13 / 3 = {round(13 / 3, 2)}')  # 13 / 3 = 4.33
# x = 13
# y = 3
# print(f'{x} / {y} = {round(x / y, 2)}')  # 13 / 3 = 4.33

# a = [1, 2, 3, 4, 5, 6]
# print(f'Третий элемент списка {a[3] * 2}')

# name = 'друг'
# prof = 'программист'
# lang = 'Python'
#
# message = (
#     f'Привет {name}. '
#     f'Ты {prof}. '
#     f'На языке {lang}.'
# )
# print(message)
# a = 74
# print(f'{{{a}}}')
# d = 'my_doc'
# f = 'data.txt'
# print(fr'home\{d}\{f}')
# print(fr'home\{d}\{f}')

# '''<div>
#     <a href='#'>content<a/>
# </div>
# '''
# s = 'Hello'
# print(s)

# def square(n):
#     """Принимает число n и возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота циландра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a')) # 97 по кодировки ASCII

# цикл для просмотра кодировки ASCII по введенному символу
# while True:
#     n = input('->')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# my_str = 'Test string for met'
# arr = [ord(x) for x in my_str]
# print('ASCII коды: ', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print('Среднее арифметическое: ', arr)
# arr += [x for x in [ord(x) for x in (input('-> ')[:3])] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(1995))
# a = 12210
# b = 138
#
# if a > b:
#     for x in range(b, a + 1):
#         print(chr(x), end=' ')
# else:
#     for x in range(a, b + 1):
#         print(chr(x), end=' ')

# print('apple' == 'Apple')
# print('apple' > 'Apple') # 97 > 65
# ===================================================================================
# ГЕНЕРАТОР ПАРОЛЕЙ
# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 125
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res = res + random_char
#     return res
#
#
# print(random_password())
# print(random_password())
# print(random_password())
# print(random_password())
# ====================================================================
# ====================================================================
# s = 'hello, WORLD! I am learning Python.'
# print(s.capitalize()) # Hello, world! i am learning python.
# print(s.lower()) # hello, world! i am learning python.
# print(s.upper()) # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase()) # HELLO, world! i AM LEARNING pYTHON.
# print(s.title()) # Hello, World! I Am Learning Python.

# print(s.count('h', 0, -4)) # считает сколько элементов + период в каком проверять
# print(s.find('Python')) # 28, первый индекс искомого слова/элемента, возвращает -1 если не найден элемент
# a = input('Введите два слова через пробел: ')
# s2 = a[a.find(' ') + 1:] + ' ' + a[:a.find(' ')]
# print(s2) # два один

# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if 48 < ord(i) < 58:
#         digits += i
# print(digits)

# ==================================================================================
# находит символ '0123456789'.find(i) в строке
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if '0123456789'.find(i) != -1:
#         digits.append(int(i))
#
# print(digits)
#
# s = 'Дана ст(рока символов, среди которых есть одна открыв)ающася'

# # 1
# s = 'Дана ст(рока символов, среди которых есть одна открыв)ающася'
# a = s.find('(')
# b = s.find(')')
# # print(s[a+1:b]) # рока символов, среди которых есть одна открыв
# print()
# # 2 не работает, не понимаю как сделать по-другому..
# # в интернете делают через replace(), мы такого не проходили
# str1 = input('Строка: ')
# str2 = []
# z = input('ЕЕ заменяемая подстрока: ')
# x = input('Новая подстрока: ')
# for i in str1:
#     if z.find(i) != -1:
#         str2.append(i)
#     else:
#         str2.append(z)
# print(str1)
# # 3
# # это задание исходя из моих знаний я не могу сделать:(

# s = 'hello, WORLD! I am learning Python.'
# print(s.rfind('l')) # индекс последнего вхождения 19
# print(s.rfind('al')) # -1 if False
# print(s.rfind('l', 0, 19)) # 3
# print(s.rindex('l')) # 19

# s = 'Send unlimeted free texts and make WiFi calls from a free phone number. Download the free app or sign up online to pick your free phone number'
# if s.count('f') >= 2:
#     print(s.find('f'), s.rfind('f'))
# elif s.count('f') < 2:
#     print(s.find('f'))

# c = 'I am learning Python. hello, World!'
# c = c[:c.find('h')] + c[c.rfind('h') + 1:]
# print(c)

# s = 'I am learning Python. hello, World!'
# print(s.endswith('d!'))
# print(s.startswith('I am'))

# print('abc123'.isalnum()) # строка состоит из букв и цифр True
# print('abc#123'.isalnum()) # False
# print('ABCabc'.isalpha()) # True только из букв
# print('123'.isdigit()) # True только цифры
# print('abc'.isidentifier()) # True валидный идентификатор
# print('1afdf'.isidentifier()) # False, такие переменные нельзя называть
# print('abc'.islower()) # True если всё в нижнем регистре + любые символы
# print(' \t \n'.isspace()) #
# print('The Apple'.istitle()) # True если каждое слово в верхнем регистре
# print('ABC'.isupper()) # TRUE если все в верхнем регистре + любые символы

# print('py'.center(10, '-'))
# print('py'.center(9, '-'))

# print('       py             '.lstrip()) # удаляет пробелы именно с ЛЕВОЙ стороны
# print('       py             '.rstrip()) # удаляет пробелы именно с ПРАВОЙ стороны
# print('https://www.python.org'.lstrip('/:phts'))
# print('https://www.python.org'.lstrip('/:phts').rstrip('.org')) # www.python
# print('        py       '.strip()) # удаляет заданные элементы со всех сторон
# ================================================================================================
# s = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный'
# print(s.replace('Nython', 'Python')) # заменяет подстроку на значение
# =====================================================================
# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq)) # a-b-c
# print('..'.join(['1', '2'])) # 1..2
# print(':'.join('Hello')) # H:e:l:l:o
# ==========================================================================
# print('Строка разделенная пробелами'.split()) # ['Строка', 'разделенная', 'пробелами']
# print('www.python.org'.split('.')) # ['www', 'python', 'org']
# print('www.python.org'.split('.', 1)) # ['www', 'python.org']

# a = input('-> ').split()
# print(a[0], a[1][:1]+'.', a[2][:1]+'.')

# s = '*'.join((input('Введите строку: ').split()))
# print(s)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
# import re


# s = 'Я ищу совпадения в 2021 году. И я их обязательно найду. 4546'
# reg = 'я'
# print(re.findall(reg, s)) # ['я', 'я', 'я']
# print(re.search(reg, s)) # возвращает первое найденое совпадение и останавливает поиск
# print(re.search(reg, s).span()) # (15, 16)
# print(re.search(reg, s).start()) # 15
# print(re.search(reg, s).end()) # 16
# print(re.search(reg, s).group()) # я
#
# print(re.match(reg, s)) # None
# rec = r'\.'
# print(re.split(reg, s)) # ['Я ищу совпадени', ' в 2021 году. И ', ' их об', 'зательно найду. 4546']
# print(re.split(rec, s)) # ['Я ищу совпадения в 2021 году', ' И я их обязательно найду', ' 4546']
# print(re.sub(rec, '!', s)) # Я ищу совпадения в 2021 году! И я их обязательно найду! 4546
# import re
#
# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. 4546. Найду в два счёта'
# reg = '2021'
# rec = '[2021]'
# rew = '[0-9]'
# rey = '[12][0-9][0-9][0-9]'
# rez = '[А-Яа-яё]'
# print(re.findall(reg, s)) # ['2021']
# print(re.findall(rec, s)) # ['2', '0', '2', '1']
# print(re.findall(rew, s)) # ['2', '0', '2', '1', '4', '5', '4', '6']
# print(re.findall(rey, s)) # ['2021', '1987']
# print(re.findall(rez, s))

# import re

# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. 4546. Найду в два счёта'
# reg = r'[А-Яа-яё.]'
# print(re.findall(reg, s))

# s = 'Еда, беду, победа'
# reg = '[Ее]д[ау]'
# print(re.findall(reg, s)) # ['Еда', 'еду', 'еда']

# s = 'Ели[-ели].'
# reg = r'[А-Яа-яё.\[\]-]'
# print(re.findall(reg, s)) # ['Еда', 'еду', 'еда']
# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. 4546.'
# reg = r'[^0-9]'
# print(re.findall(reg, s)) # все что угодно кроме 0-9

# s = 'Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09'
# reg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))

# ==================================================================
# \d - любая цифра
# \w - любая цифра, буква, символ _
# \s - символ пробела
# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. 4546.'
# reg = r'[\d]'
# print(re.findall(reg, s))
# ================================================================================
# ================================================================================
# 1 перевернуть подстроку между первым и последним вхождением 'h'
# s = 'I am learning Python. hello, WORLD!'
# print(s)
# print(s[0:s.find('h') + 1] + s[s.rfind('h') - 1:s.find('h'): -1] + s[s.rfind('h'):])
# I am learning Pyth .nohello, WORLD!
# print()
# 2 заменить 'о' на 'О', кроме первого вхождения и последнего
# a = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения.'
# print(a)
# print(a.replace('о', 'О', a.count('о') - 1).replace('О', 'о', 1))
# Замените в этой стрОке все пОявления буквы "О" на букву "О", крОме первОгО и пОследнегО вхождения.
#
# import re

#
# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. 4546.'
# # повторения
# # + - от 1 до бесконечности
# # * - от 0 до бесконечностиэ
# # ? - от 0 до 1
# reg = r'20*'
# print(s)
# print(re.findall(reg, s))
#
# d = 'Цифры: 7, +17, -42, 0013, 0.3'
# print(re.findall(r'[+-]?[\d.]+', d)) # ['7', '+17', '-42', '0013', '0.3']
#
# s = '05-03-1987 # Дата рождения'
#
# print('Дата рождения: ', re.sub(r'#.*', '', s))
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s)))

# s = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))

# s1 = 'МИ Д - Министерство иностранных дел, ГЭС - гидроэлектро станция, ФСБ - Федеральная служба безопасности'
# reg1 = r'[А-ЯЁ]{2,}\s*[А-ЯЁ]*'
# print(re.findall(reg1, s1))

# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# reg = '\+?7[0-9]{10}'
# print(re.findall(reg, s))

# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду.'
# # reg = r'^\w+\s\w+'
# reg = r'\w+\.$'
# print(s)
# print(re.findall(reg, s))

# print(re.findall(r'\w+', '12 + й')) # ['12', 'й']
# print(re.findall(r'\w+', '12 + й', flags=re.A)) # ['12'] только символы АСКИИ цифры и англ буквы

# s = 'hello world'
# print(re.findall(r'\w+', s, flags=re.DEBUG))

# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду.'
# reg = r'я'
# print(s)
# print(re.findall(reg, s, re.I)) # IGNORECASE

# text = '''
# one
# two
# '''
# print(re.findall(r'one.\w+', text)) # []
# print(re.findall(r'one.\w+', text, re.DOTALL)) # ['one\ntwo']
# print(re.findall(r'one$', text)) # []
# print(re.findall(r'one$', text, re.MULTILINE)) # ['one']

# text = '''
# {
# "one": 1,
# "two": 2,
# "three": 3
# }
# '''
# print(re.findall(r'^["\w]+', text)) # []
# print(re.findall(r'^["\w]+', text, re.MULTILINE)) # ['"one"', '"two"', '"three"']

# print(re.findall('''
# [a-z.-]+ # part 1
# @
# [a-z.-]+ # part 2
# ''', 'test@mail.ru', re.VERBOSE))

# text = '''Python,
# python
# PYTHON'''
# reg = '(?mi)^python'
# print(re.findall(reg, text))

# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.I)
#
#
# print(validate_name('Python_master'))
# print(validate_name('Py'))
# print(validate_name('@Python_master#@#%@^%'))

# s = '13425@i, 1224@i.ru, 123_2342@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# reg = r'[\w.-]+@[\w.-]+[\w]{2,3}'
# print(re.findall(reg, s)) # ['1224@i.ru', '123_2342@ru.name.ru', 'login@i.ru', 'логин-1@i.ru', 'login.3@i.ru', 'login.3-67@i.ru', '1login@ru.name.ru']
# text = '<body>Пример жадного соответствия регулярного выражения</body>'
# print(re.findall('<.*?>', text))
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
# text = '<body>Пример жадного соответствия регулярного выражения</body>'
# print(re.search('<.*?>', text).group())

# s = '<p>Изображение <img src = "bg.jpg"> - фон страницы</p>'
# reg = r'<img\s+[^>]*?src\s*=\s[^>]+>'
# print(re.findall(reg, s))

# text = 'высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[25][26], ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[27]. Язык является полностью объектно-ориентированным в том плане, что всё является объектами[25]. Необычной особенностью языка является выделение блоков кода пробельными отступами[28].'
# print(re.findall(r'\[.*?]', text)) ########### если нужно найти чтото в []

# s = 'Петр, Ольга и Виталий отлично учатся!'
# reg = r'Петр|Ольга|Виталий'
# print(re.findall(reg, s))

# s = 'int = 4, float = 4.0, double = 8.0f'
# # reg = r'int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*'
# reg = r'(?:int|float)\s*=\s*\d[.\w+]*'
# print(re.findall(reg, s))
# (?:) - группирующая скобка является не сохраняющей


# import re

# s = 'Word2016, PS6 AI5'
# reg = r'([a-z]+)(\d*)'
# print(re.findall(reg, s, re.I))
# 192.168.255.255 или 192.168.2.1
# s = '123.0.0.1'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s))

# s = '5 + 7*2 - 4'
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# a = '01-12-2021'
# p = r'([0][1-9]|[12][0-9]|[3][01])-([0][1-9]|[1][0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(p, a))

# s = 'Я ищу совпадения в 2021 году. И я их обязательно найду.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())  # 2021 году. И я их обязательно найду.
# m = re.search(reg, s)
# print('Найдена строка: ', m[0])  # Найдена строка:  2021 году. И я их обязательно найду.
# print('Найдены цифры: ', m[1])  # Найдены цифры:  2021
# print('Найдены буквы: ', m[2])  # Найдены буквы:  году. И я их обязательно найду.
# print(re.findall(reg, s))  # [('2021', 'году. И я их обязательно найду.')]

# text = '''
# Самара
# Москва
# Тверь
# Уфа
# Казань
# '''
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))

# s = '<p>Изображение <img src="bg.jpg"> - фон страницы</p>'
# reg = r'img\s+[^>]*src=[\'"](.+)[\'"]>'
# print(re.findall(reg, s))  # ['bg.jpg'] находит то что в ковычка внутри строки

# s = '<p>Изображение <img src="bg.jpg"> - фон страницы</p>'
# # reg = r'img\s+[^>]*src=([\'"])(.+)\1>'
# reg = r'img\s+[^>]*src=(?P<q>[\'"])(.+)(?P=q)>'
# print(re.findall(reg, s))  # [('"', 'bg.jpg')]

# s = 'Самолет прилетает 10/23/2021. Будем рады вас видеть после 10/24/2021'
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s)) # Самолет прилетает 23.10.2021. Будем рады вас видеть после 24.10.2021

# s = 'google.com and google.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s)) # http://google.com and http://google.ru

# РЕКУРСИЯ
# def elevator(n):
#     if n == 0:
#         print('Вы в подвале')
#         return
#     print('=>', n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input('На каком Вы этаже: '))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))

#
# def sum_list1(lst):
#     if len(lst) == 1:
#         print(lst, 'lst[0]: ', lst[0])
#         return lst[0]
#     else:
#         print(lst, 'lst[0]: ', lst[0])
#         return lst[0] + sum_list1(lst[1:])
#
#
# print(sum_list1([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(255, 10)) # 255
# print(to_str(255, 16)) # FF
# print(to_str(255, 2)) # 11111111

# names = ['adam', ['bob', ['Chet', 'cat'], 'bard', 'bert'], 'alex', ['bea', 'bill'], 'ann']
#
# print(names[0])
# print(type(names[1]) == list)
# print(isinstance(names[0], list)) # сравнивает с типом данных
# print(names[1])

# names = ['adam', ['bob', ['Chet', 'cat'], 'bard', 'bert'], 'alex', ['bea', 'bill'], 'ann']
#
#
# def count_items(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# =========================================================================
# import re
#
# reg = r'.*7.*[0-9]+.*[0-9]+.*[0-9]+.*[0-9]+.*'
# print(re.findall(reg, '+7 499 456-45-78'))
# print(re.findall(reg, '+74994564578'))
# print(re.findall(reg, '+7 (499) 456 45 78'))
# print(re.findall(reg, '+7 (499) 456-45-78'))
# ['+7 499 456-45-78']
# ['+74994564578']
# ['+7 (499) 456 45 78']
# ['+7 (499) 456-45-78']

# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos = pos + 1
#     return found


# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))

# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))
# import random
# def binary_search(s, item):
#     sorted(lst)
#     print(lst)
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#     if found:
#         print('Число', item,' присутствует в списке')
#     else:
#         print('Число', item, 'отсутствует в списке')
#
#
# lst = [random.randint(0, 99) for i in range(10)]
# a = int(input('Введите число: '))
# binary_search(lst, a)
# import random as r
# import time as t
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#         #         print(a)
#         # print('-' * 40)
#
#
# a = [r.randint(1, 99) for i in range(10000)]
#
# print(a)
# start = t.monotonic()
# bubble(a)
# print(a)
# res = t.monotonic() - start
# print(round(res, 3), 'sec')

# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return array
#
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
#
# array = [8, 2, 6, 4, 5]
# print(array)
# array = merge_sort(array)
# print(array)

# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#         print(gap, 'list: ', s)
#     return s
#
#
# a = [10, 44, 26, 14, 67, 21, 9, 87]
# print(a)
# shell_sort(a)
# print(a)

# f = open('text.txt', 'r')
# print(*f) # hello!
# print(f) # <_io.TextIOWrapper name='text.txt' mode='r' encoding='cp1251'>
# print(f.closed) # открыт или закрыт файл (тру фолс)
# print(f.mode) # r
# print(f.name) # text.txt
# print(f.encoding) # cp1251
# f = open('text.txt', 'r')
# print(f.read()) # hello!
# print(f.read(3)) # hel
# print(f.read()) # lo!. дочитает файл с остановленной позиции
#
# f.close() # после открытия обязательно указываем чтобы закрыть!!!
# f = open('text.txt', 'r')
# try:
#     print(f.read())
# finally:
#     f.close()

# f = open('test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
#
# f.close()

# f = open('test.txt', 'r')
# print(f.readlines(16))
# f.close()

# f = open('test.txt', 'r')
# for line in f:
#     count = len(f.readlines())
#     print(count)
# f.close()

# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld')
# f.close()

# f = open('xyz.txt', 'a')
# lines = ['This is lane 1', 'This is lane 2']
# f.writelines(lines)
# f.close()

# f = open('test2.txt', 'w')
# f.writelines("Первая строка\nстрока которую надо заменить\nтретья строка")
# f.close()
#
# f = open('test2.txt', 'r')
# rd = f.readlines()
# print(rd)
# for i in range(len(rd)):
#     if rd[i] == 'строка которую надо заменить\n':
#         rd[i] = 'hello world!\n'
# print(rd)
# f.close()
#
# f = open('test2.txt', 'w')
# f.writelines(rd)
# f.close()
#
# f = open('test2.txt', 'r')
# print(f.read())
# f.close()


# f = open('test2.txt', 'w')
# f.writelines("Первая строка\nстрока которую надо заменить\nтретья строка")
# f.close()
#
# f = open('test2.txt', 'r')
# rd = f.readlines()
# print(rd)
# st = int(input('pos = '))
# rd.pop(st)
# print(rd)
# f.close()
#
# f = open('test2.txt', 'w')
# f.writelines(rd)
# f.close()
#
# f = open('test2.txt', 'r')
# print(f.read())
# f.close()

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell()) # в какой позиции стоит курсор
# print(f.seek(1)) # перемещает курсор в заданную позицию
# print(f.read())

# f = open('text.txt', 'r+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# f.close()

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))

# with open('text.txt', 'r') as f:
#     for i in f:
#         print(i[:6])

file_name = 'res_1.txt'


# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return '  '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print('Done!')

# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# lst = nums.split('  ')
# print(lst)

# def longest_word(file):
#     with open(file, 'r') as text:
#         w = text.read().split()
#         print(w)
#
# print(longest_word('test.txt'))

# with open('text.txt', 'r') as text:
#     lst = list(map(str, text.read().split()))
#     m = max(len(word) for word in lst)
#     print([i for i in lst if len(i) == m])
# text = 'Строка #1\nСтрока #2\nСтрока #3\nСтрока #4\nСтрока #5\nСтрока #6\nСтрока #7'
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
# # БЕРЕМ ДАННЫЕ ИЗ ОДНОГО ФАЙЛА И ЗАПИСЫВАЕМ В ДРУГОЙ
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)

import os

# print('Текущая директория: ', os.getcwd())
# print(os.listdir('.idea'))
# os.mkdir('folder') # создает директорию по указанному пути
# os.makedirs('nested1/nested2/nesdted3') # создает вложенные папки
# os.remove('xyz.txt') # удаляет файл
# os.rename('nested1', 'test')  # переименовывает папку
# os.rename('test.txt', 'test/test1.txt') # переименовать и переместить в папку
# os.renames('text.txt', 'text/text1.txt') # переименовывает и создает новую в папку в которую помещает файл
# os.rmdir('folder') # удаляет указанную папку


# for root, dirs, files in os.walk('test'):
#     print('Root:', root)
#     print('Dirs:', dirs)
#     print('Files:', files)
#     print()

# УДАЛЯЕТ В ПАПКЕ ВЛОЖЕННЫЕ ПУСТЫЕ ПУПКИ
# for root, dirs, files in os.walk('Work'):
#     if not os.listdir(root):
#         os.rmdir(root)
#         print(f'Директория {root} удалена')

# Директория Work\F2\F5 удалена
# Директория Work\F3 удалена
# Директория Work\F4 удалена

import os.path

#
# print(os.path.split(r'D:\Python\Work\1.txt')) # ('D:\Python\Work\', '1.txt')
# print(os.path.split(r'D:\Python\Work\F5')[1]) # F5
# print(os.path.dirname(r'D:\Python\Work\1.txt')) # выведет путь директории к файлу
# print(os.path.basename(r'D:\Python\Work\1.txt')) # выведет название файла в директории
# print(os.path.join(r'D:\Python', 'Work', '1.txt')) # D:\Python\Work\1.txt

# =========================================================================
# ПРОГРАММА СОЗДАЕТ ДЕРЕВО ПАПОК И ФАЙЛОВ
# dirs = ['Work/F1', 'Work/F2/F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     'Work\\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work\\F2\\F21': ['f211.txt', 'f212.txt']
# }
# for d, fl in files.items():
#     for file in fl:
#         file_path = os.path.join(d, file)
#         open(file_path, 'w').close()
# =======================================================================
# file_with_text = ['Work\\w.txt', 'Work//F1//f12.txt', 'Work\\F2\\F21\\f211.txt', 'Work\\F2\\F21\\f212.txt']
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some sample text for {file} file')
# def print_tree(root, t):
#     print(f"Обход {root} {'сверху вниз' if t else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=t):
#         print(root)
#         print(dirs)
#         print(files)
#     print('*' * 40)
#
#
# print_tree('Work', False)
# print_tree('Work', True)

# print(os.path.exists(r'D:\\')) # проверка есть ли документ по данному пути

# print(os.path.getsize('one.txt')) # возвращает размер файла в байтах
# print(os.path.getatime('one.txt')) # время последнего доступа к файлу (секунды)
# print(os.path.getmtime('one.txt')) # время последнего изменения файла
# print(os.path.getctime('one.txt')) # создания документа

# import time
# path = r'C:\Users\Пупса\Desktop\ДЗ ПО ПРОГРАММИРОВАНИЮ\дз питон\PYTON\pythonProject\test2.txt'
# size = os.path.getsize(path)
# ksize = size // 1024
# print(f'Размер {ksize} КВ')
#
# c = os.path.getctime(path)
# b = time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(c))
# print(b)

# ==========================================================================
# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()  # экземпляр класса Point
# p2 = Point()
# p1.x = 100
# p1.y = 321
# p1.set_coords(5, 10)
# print(p1.__dict__)
# p1.set_coords('admin') # вызов метода
# p2.set_coords('Igor')

# Point.set_coords(p1, 'Elena')
# print(type(p1))
# print(isinstance(p1, Point)) # является ли экземпляр p1 экземпляром класса Point
# print(p1.x, p1.y) # 1 2
# print(p2.x, p2.y) # 100 2
# print(p2.__dict__) # {'x': 100}
# print(getattr(p1, 'x')) # 1
# print(hasattr(p1, 'z')) # проверяет на наличие атрибута 'z'
# print(setattr(p1, 'z', 7)) # создает атрибут
# print(p1.__dict__)
# delattr(p1, 'z')
# print(p1.__dict__)
# print(Point.__doc__) # документация класса
# print(Point.__name__) # имя класса
# print(dir(Point))
# =============================================================================
# https://disk.yandex.ru/d/MoyZqh5AIGaZ3g ===================================

#====================================================================
#===================================================================
#==================================================================
#=====================================================================
# ООП КЛАССЫ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print('='*40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '11-22-33', 'Россия', 'Москва', 'Чистопрудный бульвар, 1A')
# h1.set_name('Егор')
# h1.print_info()
# print(h1.get_name())

# class Auto:
#     name = ''
#     year = ''
#     work = ''
#     horse_power = ''
#     color = ''
#     price = ''
#
#     def car_info(self):
#         print(' Автомобиль '.center(40, '*'))
#         print(f'Название модели: {self.name}\n'
#               f'Год выпуска: {self.year}\n'
#               f'Производитель: {self.work}\n'
#               f'Мощность: {self.horse_power}\n'
#               f'Цвет: {self.color}\n'
#               f'Цена: {self.price}')
#
#     def info_car(self, name, year, work, horse_power, color, price):
#         self.name = name
#         self.year = year
#         self.work = work
#         self.horse_power = horse_power
#         self.color = color
#         self.price = price
#
#     def power(self, power):
#         self.power = power
#
#     def hpower(self):
#         print(self.power)
#
#
# a1 = Auto()
# a1.info_car('BMW', '2022', 'Германия', '450', 'Черный', '8млн')
# a1.car_info()
# a1.power('1000')
# a1.hpower()

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self, ):
#         print(f'Данные сотрудника: {self.name} {self.surname}')
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f'Квалификация сотрудника: {self.name}', self.skill, '\n')
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
# p2 = Person('Anna', 'Dolgih')
# p1.print_info()
# p1.add_skill(2)

# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print('Construktor')
#     #     return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print('Initializator')
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print('Удаление экземпляра: '+ self.__class__.__name__)
#
#     def set_cooords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)

# class Point:
#     count = 0  # статическое свойство
#
#     def __init__(self, x, y):
#         print('Initializator')
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
#
# p2 = Point(10, 20)
#
# print(Point.count)
# print(p1.count)
# print(p2.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Инициализация робота {self.name}')
#         print(f'Приветствую. Меня зовут: {self.name}')
#         Robot.k += 1
#
#     def __del__(self):
#         print(f'{self.name} выключается')
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, 'последний')
#         else:
#             print(f'Работающих роботов осталось {Robot.k}')
#
#
# droid1 = Robot('R2-D2')
# print('Численность роботов', Robot.k)
# droid2 = Robot('C-3PO')
# print('Численность роботов', Robot.k)
# droid3 = Robot('QQ-23')
# print('Численность роботов', Robot.k)
# droid4 = Robot('R-214gG')
# print('Численность роботов', Robot.k)
# print()
# print('RRRRRRRRRRRRRRRRRRR')
# print()
# del droid1
# del droid2
# del droid3
# del droid4
# print('Численность роботов', Robot.k)
# ============================================================
#==============================================================
#=================================================================
#================================================================

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__chek_value(x) and Point.__chek_value(y):
#             self.__x = x
#             self.__y = y
#
#     # def set_x(self, x):  # установить
#     #     self.__x = x
#     #
#     # def get_x(self):  # получить
#     #     return self.__x
#     def __chek_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__chek_value(x) and Point.__chek_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#
# p1 = Point(5, 10)
# # p1.set_x(100)
# # print(p1.get_x())
# p1.set_coords(50.2, 70.2)
# # print(p1.x, p1.y)
# # p1.x = 100
# # p1.y = 'abc'
# # print(p1.x, p1.y)
# print(p1.get_coords())
# print(p1.__dict__)
# import math
#
#
# class Rectangle:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Rectangle.__check_value(x) and Rectangle.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, (int, float)):
#             return True
#         return False
#
#     def set_x(self, x):
#         if Rectangle.__check_value(x):
#             self.__x = x
#
#     def set_y(self, y):
#         if Rectangle.__check_value(y):
#             self.__y = y
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def get_area(self):
#         return self.__x * self.__y
#
#     def get_perim(self):
#         return 2 * (self.__x + self.__y)
#
#     def get_gipp(self):
#         return math.sqrt((self.__x ** 2) + (self.__y ** 2))
#
#     def print_area(self):
#         # for i in range(self.__x):
#         #     print('*' * self.__y)
#         print(('*' * self.__y + '\n') * self.__x)
#
#
# r1 = Rectangle(3, 4)
# r1.set_x(6)
# r1.set_y(29)
# print(r1.get_x(), r1.get_y())
# print(r1.get_area())
# print(r1.get_perim())
# print(round(r1.get_gipp(), 2))
# r1.print_area()
#
# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, n):
#         self.__old = n
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# p1.old = 30
# print(p1.__dict__)
# print(p1.name)
# print(p1.old)
# del p1.name
# del p1.old
# print(p1.__dict__)

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod # сделать статический метод, который не требует обязательного аргумента
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 4)
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p1.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# class Point:
#
#     @staticmethod
#     def max(a, b, c, d):
#         if a > b > c > d:
#             return a
#         elif b > a > c > d:
#             return b
#         elif c > a > b > d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a < b < c < d:
#             return a
#         elif b < a < c < d:
#             return b
#         elif c < a < b < d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def average(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def fact(x):
#         c = 1
#         for i in range(1, x + 1):
#             c *= i
#         return c
#
#
# print(Point.max(6, 14, 3, 2))
# print(Point.min(6, 14, 3, 2))
# print(Point.average(6, 14, 3, 2))
# print(Point.fact(9))
#
# class Temperatur:
#     count = 0
#
#     @staticmethod
#     def farg(x):
#         Temperatur.count += 1
#         return x * 1.8 + 32
#
#     @staticmethod
#     def cel(x):
#         Temperatur.count += 1
#         return f'Температура в цельсиях: {(x - 32) / 1.8}'
#
#
# print(Temperatur.farg(15))
# print(Temperatur.farg(30))
# print(Temperatur.cel(59))
# print(Temperatur.count)

# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_validate(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 2999
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '01.01.2020',
#     '12.31.2020'
# ]
# for string_date in dates:
#     if Date.is_date_validate(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print('Неправильная дата или формат')
# # date = Date.from_string('31.10.2021')
# # print(date.string_to_db())

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value  # баланс
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был открыт')
#         print('*' * 43)
#
#     def __del__(self):
#         print('*' * 43)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты были успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}.')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} было успешно снято')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.__value} {Account.suffix}')
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()
#         print(f'Проценты: {self.__percent:.0%}')
#         print('-' * 20)
#
#
# acc = Account('12345', 'Dolgih', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner('Dyma')
# acc.print_info()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
#
# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#         self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError('Неверный формат фио')
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО используйте только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом от 15 до 99 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строковым значением")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат данных")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер могут быть только числом")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
#
#
#
#
# p1 = UserDate('Волков Игорь Николаевич', 26, '1234 567890', 80.8)
# p1.fio = 'Соболев Игорь Николаевич'
# print(p1.fio)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         print('Инициализатор базового класса Prop')
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
# class Rectangle(Figure):
#     def __init__(self, w, h, color):
#         super().__init__(color)
#         self.__width = w
#         self.__height = h
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError
#
#     def area(self):
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.width)
# print(rect.height)
# print(rect.color)
# print(rect.area())
#
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._ep = ep
#             self._sp = sp
#         else:
#             print('Координаты должны быть числами')
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._ep = ep
#             self._sp = sp
#         else:
#             print('Координаты должны быть целочисленными')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(7, 8), Point(100, 200))
# line.draw_line()

# class Rect:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, w, h, bg):
#         self.fon = bg
#         super().__init__(w, h)
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Фон: {self.fon}')
#
#
# class RectBorder(Rect):
#     def __init__(self, w, h, border):
#         super().__init__(w, h)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Рамка: {self.border}')
#
#
# shape1 = RectFon(400, 200, 'yellow')
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, '1px solid red')
# shape2.show_rect()

# class Vector(list):
#     def __str__(self):
#         return '+'.join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._ep = ep
#             self._sp = sp
#         else:
#             print('Координаты должны быть числами')
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print('Координаты должны быть целочисленными')
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._ep = ep
#                 self._sp = sp
#             else:
#                 print('Координаты должны быть целочисленными')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(7, 8), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(), Point(-10, -20))
# line.draw_line()

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._ep = ep
#             self._sp = sp
#         else:
#             print('Координаты должны быть числами')
#
#     def draw(self):
#         raise NotImplementedError('В дочернем классе должен быть определен метод draw')
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование Линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование Прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование Элипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()
# import math
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError('В дочернем классе должен быть определен метод calc_area()')
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(math.pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t3 = RoundTable(radius=20)
# print(t3.__dict__)
# print(t3.calc_area())
# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print('Нарисовал шахматную фигуру')
#
#     @abstractmethod
#     def move(self):
#         print('Метод move() в базовом классе')
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print('Ферзь перемещен')
#
#
# q = Queen()
# q.draw()
# q.move()
#
# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
#
# d2 = [Euro(5), Euro(10), Euro(50), Euro(100)]
# for elem in d2:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('class Child')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('class displayChild')
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()
#
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print('Метод внешнего класса')
#
#     def outer_obj_method(self):
#         print('Метод для связи')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Метод внутреннего класса', MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('Внешний')
# inner = out.MyInner('Внутренний класс', out)
# inner.inner_method()
# print(inner.inner_name)
#
# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.Lightgreen()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Lightgreen:
#         def __init__(self):
#             self.name = 'Light green'
#             self.code = '024AVC'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Code:', self.code)
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()

# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Employee list')
#         print(self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '657'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Id:', self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#             self.id = '007'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Degree:', self.id)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.intern
# d2 = outer.head
# print()
# d1.display()
# print()
# d2.display()
#
# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('class outer')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('Class INNER')
#
#         class InnerClass:
#             def show(self):
#                 print('Class InnerClass')
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# # inner2 = outer.inner.inner_inner
# inner2 = inner1.inner_inner
# inner2.show()
#
# class Computer:
#     def __init__(self):
#         self.name = 'Pc001'
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core i7'
#
#
# comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.OS()
# my_cpu = Computer.CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())
#
# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('Class Base')
#
#     class Inner:
#
#         def display1(self):
#             print('Inner of Base Class')
#
#
# class SubClass(Base):
#     def __init__(self):
#         print('In Subclass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner of Subclass')
#
# a = SubClass()
# a.display()
#
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end='')
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.model = 'HP'
#             self.cpu = 'i7'
#             self.memory = '16'
#
#         def show(self):
#             print('==>', self.cpu, self.model, self.memory)
#
#
# s1 = Student('Roman')
# s1.show()

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking')
#
# d = Dog('Buddy')
# d.sleep()
# d.play()
# d.bark()

# class A:
#     # def __init__(self):
#     #     print('Инициализатор класса А')
#     def hi(self):
#         print('A')
#
# class AA:
#     def hi(self):
#         print('AA')
#
#
# class B(A):
#     # def __init__(self):
#     #     print('Инициализатор класса B')
#     def hi(self):
#         print('B')
#
# class C(AA):
#     # def __init__(self):
#     #     print('Инициализатор класса C')
#     def hi(self):
#         print('C')
#
# class D(B, C):
#     # def __init__(self):
#     #     super().__init__()
#     #     B.__init__(self)
#     #     C.__init__(self)
#     #     print('Инициализатор класса D')
#     pass
#
#
# d = D()
# d.hi()
# print(D.mro())


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclass = MySubClass()
# subclass.display('Это строка будет отображаться и записываться в файл')

# class Clock:
#     __DAY = 86400  # 24*60*60 число секунд в одном дне
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError('Секунды должны быть числом')
#
#         self.__sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.__sec % 60  # секунды
#         m = (self.__sec // 60) % 60  # минуты
#         h = (self.__sec // 3600) % 24  # часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def get_seconds(self):
#         return self.__sec
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типо данных Clock')
#         return Clock(self.__sec + other.get_seconds())
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# c4 = Clock(300)
# c3 = c1 + c2 + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c4.get_format_time())
# print(c3.get_format_time())
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             # print('Неверный индекс')
#             raise IndexError('Неверный индекс')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('Индекс должен быть целым и положительным числом')
#         # if key >= len(self.marks):
#         #     raise TypeError('Такого индекса не существует')
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError('Индекс должен быть целым числом')
#         del self.marks[key]
#
#
# s1 = Student('Сергей', [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# print(s1[2])
# del s1[2]
# print(s1.marks)
#
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1,2,3)
# t2 = Triangle(4,5,6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())
#
# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text('Python')
#
# print(t1.total(35))
# print(t2.total(35))

# class Cat:
#     def __init__(self, animal, name, age):
#         self.animal = animal
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я {self.animal}. Меня зовут {self.name}. Мой возраст {self.age}."
#
#     def sound(self):
#         return f"{self.name} мяукает."
#
#
# class Dog:
#     def __init__(self, animal, name, age):
#         self.animal = animal
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я {self.animal}. Меня зовут {self.name}. Мой возраст {self.age}."
#
#     def sound(self):
#         return f"{self.name} гавкает."
#
#
# k1 = Cat("кот", "Пушок", 2.5)
# d1 = Dog("собака", "Мухтар", 4)
# lst = [k1, d1]
# for i in lst:
#     print(i.info())
#     print(i.sound())

# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#
#     def info(self):
#         print(f"{self.first} {self.last} {self.age}")
#
#
# class Student(Human):
#     def __init__(self, spec, group, reit, first, last, age):
#         super().__init__(first, last, age)
#         self.spec = spec
#         self.group = group
#         self.reit = reit
#
#     def info(self):
#         print(f"{self.spec} {self.group} {self.reit}", end=" ")
#         super().info()
#
#
# class Teacher(Human):
#     def __init__(self, spec, exp, first, last, age):
#         super().__init__(first, last, age)
#         self.spec = spec
#         self.exp = exp
#
#     def info(self):
#         print(f"{self.spec} {self.exp}", end=" ")
#         super().info()
#
#
# class Graduate(Student):
#     def __init__(self, topic, first, last, age, spec, group, reit):
#         super().__init__(first, last, age, spec, group, reit)
#         self.topic = topic
#
#     def info(self):
#         print(f"{self.topic}", end=" ")
#         super().info()
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f'{self.name}'
#
# cat = Cat('Пушок')
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#
# p = Point(1, 5, 7)
# print(len(p))
#
# import math
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x*x+y*y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(2, 8)
# print(p1.length)
#
# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
#
# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Аргумент должен быть строкой')
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars('?:!.: ')
# print(s1(' Hello World! '))

# def strip_chars(char):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError('Аргумент должен быть строкой')
#         return string.strip(char)
#
#     return wrap
#
#
# s1 = strip_chars('?:!.: ')
# print(s1(' Hello World! '))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# СОРТИРОВКА СПИСКА КЛАССОМ
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class Person:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     @property
#     def data(self):
#         return self.surname, self.name, self.age
#
#
# class SortKey:
#     def __init__(self, *args):
#         self.__method = args
#
#     def __call__(self, lst):
#         lst.sort(key=lambda i: [i.__dict__[key] for key in self.__method])
#
#
# p = [Person('Иванов', 'Игорь', 28),
#      Person('Петров', 'Степан', 21),
#      Person('Сидоров', 'Антон', 25),
#      Person('Петров', 'Анатолий', 11),
#      Person('Иванов', 'Иван', 28)
#      ]
#
# for i in p:
#     print(i.data)
# print()
# s1 = SortKey('surname')
# s1(p)
# for i in p:
#     print(i.data)
# print()
# s2 = SortKey('surname', 'name')
# s2(p)
# for i in p:
#     print(i.data)

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('перед вызовом функции')
#         self.func()
#         print('после вызова функции')
#
#
# @MyDecorator
# def func1():
#     print('func')
#
#
# func1()

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         print('перед вызовом функции')
#         res = self.func(a, b)
#         print('после вызова функции')
#         return res
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 5))

# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = self.func(a, b) ** 2
#         return res
#
#
# @Power
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 3))

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('перед вызовом функции')
#         res = self.func(*args, **kwargs)
#         print('после вызова функции')
#         return res
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
# print(func1(2, 5))
# print(func2(2, 5, 3))

# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             print('перед вызовом функции')
#             print(self.name)
#             func(*args, **kwargs)
#             print('после вызова функции')
#
#         return wrap
#
#
# @MyDecorator('test2')
# def add(a, b):
#     print(a, b)
#
#
# add(2, 5)
#
# class Power:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res ** self.name
#
#         return wrap
#
#
# @Power(3)
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 2))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ДЕСКРИПТОР
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person('Ivan', 'Petrov')
# print(p.name.get())
#
# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
# p = Person('Ivan', 'Petrov')
# print(p.name)
# print(p.surname)
#
# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst = MyList()
# lst.append(10)
# lst.append(20)
# print(lst, lst.get_length())
#
# class MyMetaclass(type):
#     def __new__(mcs, name, base, attr):
#         print('Создание нового объекта', name)
#         return super(MyMetaclass, mcs).__new__(mcs, name, base, attr)
#
#     def __init__(cls, name, base, attr):
#         print('Инициализатор класса', name)
#         super(MyMetaclass, cls).__init__(name, base, attr)
#
#
# class Student(metaclass=MyMetaclass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student('Анна')
# print('Имя студента:', stud.get_name())
# print('Тип объекта Student:', type(stud))
# print('ТИп класса Student:', type(Student))

# import pyt.rect
# from pyt import rect
# from pyt import *
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = rect.Square(10)
# s2 = rect.Square(20)
#
# t1 = rect.Triangle(1, 2, 3)
# t2 = rect.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())

# from car import electrocar
#
# e_car = electrocar.ElectroCar('Tesla', 'T', '2018', 99000)
# e_car.show_car()
# e_car.description_battery()

# import json
#
#
# data = {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "sky daving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 6
#          },
#         {
#             "firstName": "Bob",
#             "age": 8
#          }
#     ]
# }

# with open('data_file.json', 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open('data_file.json', 'r') as fw:
#     data1 = json.load(fw)
#     print(data1)

# json_string = json.dumps(data, sort_keys=True)
# data1 = json.loads(json_string)
# print(data1)
#
# x = {'name': 'Виктор'}
# y = {'name': 'Виктор'}
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))
#
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(personal_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(personal_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         c = ''
#         for i in self.marks:
#             c += str(i) + ', '
#         return f'Student {self.name}: {c[:-2]}'
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({'name': stud.name, 'marks': stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         c = ''
#         for i in self.students:
#             c += str(i) + '\n'
#         return f'Группа {self.group}\n{c}'
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def change_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_lst = []
#             for i in group.students:
#                 stud_lst.append([i.name, i.marks])
#             tmp = {'Students': stud_lst}
#             data.append(tmp['Students'])
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_group(cls, file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# print(my_group)
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
# # print(st1)
# # st1.add_marks(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(2, 5)
# # print(st1)
# # print(st1.average_mark())
#
# group22 = [st2]
# my_group2 = Group(group22, 'ГК Web')
# print(my_group2)
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)
#
# # Student.dump_to_json(st1, 'student.json')
# # Student.dump_to_json(st2, 'student.json')
# # Student.load_from_file('student.json')
#
# Group.dump_group('group.json', my_group2)
# Group.dump_group('group.json', my_group)
# Group.upload_group('group.json')
#
# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
#
# # print(todos[:10])
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_completed = top_users[0][1]
# print(max_completed)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_completed:
#         break
#     users.append(str(user))
#
# print(users)
#
# max_users = ' and '.join(users)
#
# s = 's' if len(users) > 1 else ''
# print(f'user{s} {max_users} completed {max_completed} TODOs ')
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo["userId"]) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_data_file.json', 'w') as data_file:
#     filter_todos = list(filter(keep, todos))
#
#     json.dump(filter_todos, data_file, indent=2)
#
# with open('filtered_data_file.json', 'r') as fw:
#     data = json.load(fw)
#     print(data)
#

# CSV (Comma Separated Volues)

# import csv

# with open('data.csv') as r_file:
#     file_reader = csv.reader(r_file, delimiter=',')
#     count = 0
#
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         else:
#             print(f'\t{row[0]} - {row[1]}. Родился в {row[2]} году')
#         count += 1
#     print(f'Всего в файле {count} строки.')
#
#
#
# with open('data.csv') as r_file:
#     fieldnames = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=';', fieldnames=fieldnames)
#     count = 0
#
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         print(f'\t{row["Имя"]} - {row["Профессия"]}. Родился в {row["Год рождения"]} году')
#         count += 1
#     print(f'Всего в файле {count } строки.')

# with open('student.csv', mode='w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', '9 класс', '15'])
#     writer.writerow(['Саша', '5 класс', '12'])
#     writer.writerow(['Маша', '11 класс', '18'])
#
# from bs4 import BeautifulSoup
# import re


# def get_copywriter(tag):
#     whoise = tag.find('div', class_='whois')
#     if 'Copywriter' in whoise:
#         return tag
#     return None
# def get_salary(s):
#     pattern = r'\d+'
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# # row = soup.find('div', class_='name').text
# # row = soup.find_all('div', class_='name')
# # row = soup.find_all('div', {'data-set': 'salary'})
# # row = soup.find('div', text='Alena').parent # обращаешься к родительскому уровню
# # row = soup.find('div', text='Alena').find_parent(class_='row')
# # row = soup.find('div', id='whois3').find_next_sibling() # поиск следующей строки
# # row = soup.find('div', id='whois3').find_previous_sibling() # поиск предыдущей строки
# # copywriter = []
# # row = soup.find_all('div', class_='row')
# # for i in row:
# #     cw = get_copywriter(i)
# #     if cw:
# #         copywriter.append(cw)
# # print(copywriter)
# salary = soup.find_all('div', {'data-set': 'salary'})
# for i in salary:
#     get_salary(i.text)
#
# import requests
#
# r = requests.get('https://ru.wordpress.org/')
# print(r)
#
# import requests
# from bs4 import BeautifulSoup
#
#
# #
# #
# # def get_html(url):
# #     r = requests.get(url)
# #     return r.text
# #
# # def get_page_data(html):
# #     soup = BeautifulSoup(html, 'lxml')
# #
# #     elements = soup.find_all('article', class_="plugin-card")
# #     print(len(elements))
# #
# # def main():
# #     url = 'https://ru.wordpress.org/plugins/browse/blocks/'
# #     get_page_data(get_html(url))
# #
# #
# # if __name__ == '__main__':
# #     main()

# 2:15
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     # p1 = soup.find('header', id='masthead').find('p', class_='site-title').text
#     s = soup.find_all()
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()
#
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#
#     elements = soup.find_all('div', class_="theme")
#     print(len(elements))
#
#
# def main():
#     url = 'https://ru.wordpress.org/themes/'
#     get_page_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
#
# from parser import Parser
#
#
# def main():
#     pars = Parser('https://www.ixbt.com/live/index/type/news/',
#                   'news.txt')
#     pars.run()
#
# if __name__ == '__main__':
#     main()

#
# import socket
# from Work.view import index, blog
#
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page not found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found</h3>'
#     if code == 405:
#         return '<h1>405</h1><h3>Method Allowed</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     header, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (header + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#
#         print(f'Клиент: {addr} => \n{request.decode("utf-8")}')
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#
#
# if __name__ == '__main__':
#     run()
#
# import sqlite3 as sq
#
# # con = sq.connect('profile.db')
# # cur = con.cursor()
# #
# # cur.execute('''
# # ''')
# #
# # con.close()
#
# with sq.connect('profile.db') as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE users")
# cur.execute('''CREATE TABLE IF NOT EXISTS users(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# sum REAL,
# date TEXT
# )''')

# ============================================================
# HomeWork на 18.05.2022
# import csv
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open('data2.csv', 'a', encoding="utf-8") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator='\r')
#         writer.writerow((data['name'],
#                          data['description'],
#                          data['price']
#                          ))
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#
#     elements = soup.find_all('a', class_="css-5l099z ewrty961")
#     for elem in elements:
#         name = elem.find('div', class_="css-17lk78h e3f4v4l2").text
#         des = elem.find('div', class_="css-1fe6w6s e162wx9x0").text
#         price = elem.find('div', class_="css-1dv8s3l eyvqki91").text
#
#         data = {
#             'name': name,
#             'description': des,
#             'price': price
#         }
#
#         write_csv(data)
#
#
# def main():
#     url = 'https://auto.drom.ru/toyota/camry/generation7/restyling0/'
#     get_page_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
# ========================================================================
# HomeWork на 23.05.2022

# ============================================================
# HomeWork на 18.05.2022
# import csv
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open('data2.csv', 'a', encoding="utf-8") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator='\r')
#         writer.writerow((data['name'],
#                          data['description'],
#                          data['price']
#                          ))
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#
#     elements = soup.find_all('a', class_="css-5l099z ewrty961")
#     for elem in elements:
#         name = elem.find('div', class_="css-17lk78h e3f4v4l2").text
#         des = elem.find('div', class_="css-1fe6w6s e162wx9x0").text
#         price = elem.find('div', class_="css-1dv8s3l eyvqki91").text
#
#         data = {
#             'name': name,
#             'description': des,
#             'price': price
#         }
#
#         write_csv(data)
#
#
# def main():
#     url = 'https://auto.drom.ru/toyota/camry/generation7/restyling0/'
#     get_page_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
# ========================================================================
# import sqlite3 as sq
# with sq.connect('user2.db') as con:
#     cur = con.cursor()
#         # cur.execute('''CREATE TABLE IF NOT EXISTS person(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # phone BLOB NOT NULL DEFAULT +79099000000,
#     # age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
#     # email TEXT UNIQUE
#     # )''')
#     # cur.execute('''
#     # ALTER TABLE person
#     # RENAME TO person_table;
#     # ''')
#     cur.execute('''
#     DROP TABLE person_table
#     ''')
# ALTER TABLE person_table
# DROP COLUMN home_address;
# ''')
# ALTER TABLE person_table
# RENAME COLUMN address TO home_address;
# ''')
#import sqlite3 as sq

# with sq.connect('db_4.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5;
#     ''')
#
#     res = cur.fetchone()
#     res2 = cur.fetchmany(2)
#     print(res)
#     print(res2)

# cars = [
#     ('Chevrolet', 54000),
#     ('Daewoo', 34000),
#     ('Lada', 52000),
#     ('Honda', 27000),
#     ('Toyota', 24000)
# ]
# def read_ava(n):
#     try:
#         with open(f'{n}.png', 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     ''')
#
#     cur.execute('SELECT ava FROM users LIMIT 1')
#     img = cur.fetchone()['ava']
#
#     write_ava('out.png', img)

# img = read_ava(1)
# if img:
#     binary = sq.Binary(img)
#     cur.execute('INSERT INTO users VALUES("Илья", ?, 1000)', (binary,))
# cur.execute('SELECT model, price FROM cars')
# print(con.row_factory)
# rows = cur.fetchall()
# rows = cur.fetchone()
# rows = cur.fetchmany(5)
# print(rows)
# for res in cur:
#     print(res['model'])
# cur.execute('INSERT INTO cars VALUES(NULL, "Запорожец", 1000)')
# last_row_id = cur.lastrowid # id последней записи
# buy_car_id = 2 # переменная - авто который купит покупатель
# cur.execute('INSERT INTO cost VALUES("Илья", ?, ?)', (last_row_id, buy_car_id))

# cur.executescript('''
# DELETE FROM cars WHERE model LIKE 'B%';
# UPDATE cars SET price = price + 100;
# ''')
# cur.execute('UPDATE cars SET price = :Price WHERE model LIKE "B%"', {'Price:0'})
# cur.executemany('INSERT INTO cars VALUES(NULL, ?, ?)', cars)
# cur.execute('INSERT INTO cars VALUES(1, "Renault", 22000)')
# cur.execute('INSERT INTO cars VALUES(2, "Volvo", 29000)')
# cur.execute('INSERT INTO cars VALUES(3, "Mers", 57000)')
# cur.execute('INSERT INTO cars VALUES(4, "Bentley", 35000)')
# cur.execute('INSERT INTO cars VALUES(5, "Audi", 52000)')
# for car in cars:
#     cur.execute('INSERT INTO cars VALUES(NULL, ?, ?)', car)
# con = None
# try:
#     con = sq.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS cars(
#          car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#          model TEXT,
#          price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, "Audi", 52000);
#     UPDATE cars SET price = price + 100;
#     ''')
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print('Ошибка выполнения запроса')
# finally:
#     if con:
#         con.close()

# with sq.connect('cars.db') as con:
#     cur = con.cursor()

    # with open('sql_dump.sql', 'w') as f:
    #     for sql in con.iterdump():
    #         f.write(sql)

    # with open('sql_dump.sql', 'r') as f:
    #     sql = f.read()
    #     cur.executescript(sql)

# data = [('car', 'машина'), ('house', 'дом'), ('tree', 'дерево', ('color', 'цвет'))]
# con = sq.connect(':memory:')
# with con:
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS dict(
#     eng TEXT,
#     rus TEXT)''')
#
#     cur.executemany('INSERT INTO dict VALUES(?, ?)', data)
#
#     cur.execute('SELECT rus FROM dict WHERE eng LIKE "c%"')
#     print(cur.fetchall())





