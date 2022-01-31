# voron = int(input("Input voron: "))
# if voron == 1:
#     print(voron,"Ворона")
# elif voron == 2 or 3 or 4:
#     print(voron,"вороны")
# elif voron == 5 or 6 or 7 or 8 or 9:
#     print(voron,"ворон")
# else:
#     print("ошибка ввода данных")


# true if (условие) else false - тернарное выражение

# a, b = 0, 20
# print("делить нельзя" if a == 0 else (b/a))


# try: - если не может выполниться то выполняется except
# (то есть если ошибка то читает код дальше)
#     print("код смещенный на одну табуляцию")
# except (ValueError, ZeroDivisionError): (вид исключения, можно писать несколько в скобках)
#     print("код не работает!")
#     print("не делится на ноль!")
# else:   - если код не выдает ошибку, то есть отрабатывает когда НЕ отрабатываеT except
#     print("Все норамально работает")
# finally: - выполнятся всегда, не зависимо выполнился код выше или нет
#     print("конец программы")


# 1 вариант
# a = input("Введите первое число:")
# b = input("Введите второе число:")
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(a + b)

# 2 вариант
# a = input("Введите первое число:")
# b = input("Введите второе число:")
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
#     b = str(b)
# finally:
#     print(a + b)


# ЦИКЛЫ
# i = 2
# while i < 21:
#     print("i =", i)
#     i += 2
#
# выводит только четные числа
# i = 0
# while i<20:
#     i+=1
#     if(i%2==0):
#         print(i)

# n = int(input("Укажите количесво символов: "))
# i = 0
# while i < n:
#     # выводит звездочки в одну строку
#     print("*", end="")
#     i+=1
#
# n = int(input("Укажите количесво символов: "))
# i = 0
# while i < n:
#     # выводит звездочки по одной в каждой строке
#     print("*")
#     i+=1


# цикл выводит сумму нечетных чисел в заданном диапозоне
# n = int(input("Введите начало диапазона: "))
# m = int(input("Введите конец диапазона: "))
# s = 0
# while n <= m:
#     if n % 2 != 0:
#         s += n
#     n += 1
# print(s)

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")
#
# Завершить цикл на i = 5!
# i = 0
# while i < 10:
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")
#
#
# Цикл с пропуском цифры три
# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# так же выведет числа до 5
# i = 0
# while True:
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# бесконечный цикл пока не введешь положительное число
# while True:
#     n = int(input("Введите положительное число: "))
#     if not n > 0:
#         break


# запрашивает числа, умнажает их друг на друга, пока пользователь не введет 0
# res = int(input("Введите число: "))
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print("Результат: ", res)


# выводит таблицу умножения
# i=1
# while i < 10:
#     print(" ", end='\n')
#
#     j=1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end='\t' )
#         j += 1
#     i += 1


# выводит звездочки по диагонали
# i=0
# c=" "
# d='*'
# while i<1:
#     j=0
#     while j<5:
#         print(c*j,d)
#         j+=1
#     i+=1


# как работает фор
# for i in "Hello!":
#     print(i)

# i = 1
# for color in 'red', 'green', 'yellow':
#     print(i, "color: ", color)
#     i =+ 1

# range(start, stop, step)


# for i in range(2, 9, 3):
#     print(i, end="")


# выводит только числа кратные введенному числу
# n = int(input("Введите число: "))
# for i in range(1, n):
#     if n % i == 0:
#         print(i, end=" ")


# выводит 11 22 33 44 55 66 77 88 99
# i=1
# for i in range(10, 100, i):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#
# else:
#     print('done')


# выводит по запросу символы с кол-вом и типом и ориентацией
# num = int(input("число символов?"))
# symb = input("тип символа?")
# orient = int(input("ориентация линии?(0 - горизонтальная, 1 - вертикальная)"))
# if orient == 0:
#     i = 0
#     while i < num:
#         print(symb, end="")
#         i+=1
# elif orient == 1:
#     i = 0
#     while i < num:
#         print(symb)
#         i += 1
# else:
#     print("Нужно вводить 0 или 1!!!!!!")


# выводит последовательность чисел в кол-ве запрошенном у пользователя
# num1 = int(input("Введите количество чисел последовательности:"))
# i = 0
# while i <= num1:
#     print("Введите число:")
#     i += 1


# проверка на палиндром (читается задом наперед одинково 1331, aabccbaa)
# n1 = int(input("Введите целое число: "))
# p1 = n1
# res = 0
# while n1 != 0:
#     d = n1 % 10
#     res = res * 10 + d
#     n1 = int(n1 / 10)
# if res == p1:
#     print("Число " + str(p1) + " - палиндром")
# else:
#     print("Число " + str(p1) + " - не палиндром")

# print("Число -", p1, (" -" if res == p1 else " -не"), "палиндром")


# нечетные числа в заданном диапазоне
# a = int(input("Начало диапозона: "))
# b = int(input("Конец диапозона: "))
# i = 0
# import time
# for i in range(a, b + 1):
#     if(i % 2 != 0):
#         print(i, end=" ")
#         time.sleep(0.4)


# выводит чередующиеся символы по вертикали
# a = input("первый символ: ")
# b = input("Второй символ: ")
# import time
# for i in range(5):
#     for i in range(8):
#         print(a, end="")
#         time.sleep(0.3)
#         print(b, end="")
#         time.sleep(0.3)
#     print(" ")


# выводит звездочки
# *   *   *   *
#  *   *   *   *
# *   *   *   *
#  *   *   *   *
# *   *   *   *
# for i in range(1,):
#    for j in range(1,9):
#        if i % 2 == 0:
#            if j % 2 == 0:
#                print("*", end=' ')
#            else:
#                print(" ", end=' ')
#        else:
#            if j % 2 != 0:
#                print("*", end=' ')
#            else:
#                print(" ", end=' ')
#    print()


# игра угадай число
# прочитав условие думал будет сложнее, но вроде всё получилось и работает
# import random
# a = random.randint(1,10)
# c = 0
# while c<99:
#     b = int(input('Введите число от 1 до 10: '))
#     c+=1
#     if 0<b<a:
#         print("Загаданное число больше")
#     elif 0<b>a:
#         print("Загаданное число меньше")
#     elif b == 0:
#         print("Остановлено")
#         break
#     elif b == a:
#         print("Вы угадали число с " + str(c) + " попыток")
#         break


# сформировал символ из количества символов, запрошенных у пользователя
# так же сформировал пустую ячейку такого же размера
# а как их печатать по вертикали и следующую строку
# сделать с символами в обратном порядке (с пустой клетки) не могу додуматься
# a = int(input("Введите размер поля: "))
# b = int(input("Введите количество символов: "))
# for i in range(a):
#     for i in range(a):
#         for i in range(b):
#             for i in range(b):
#                 print("*", end="")
#                 print(" ", end="")
#             print(" ")
#         for i in range(b):
#             for i in range(b):
#                 print(" ", end="")
#                 print(" ", end="")
#             print(" ")


# выводит чередующиеся символы по вертикали
# мне кажется я как то не так задание понял, но сделал как понял..
# a = input("первый символ: ")
# b = input("Второй символ: ")
# import time
# for i in range(5):
#     for i in range(8):
#         print(a, end="")
#         time.sleep(0.1)
#         print(b, end="")
#         time.sleep(0.1)
#     print(" ")


# нечетные числа в заданном диапазоне
# a = int(input("Начало диапозона: "))
# b = int(input("Конец диапозона: "))
# i = 0
# import time
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         print(i, end=" ")
#         time.sleep(0.1)

# игра угадай число
# прочитав условие думал будет сложнее, но вроде всё получилось и работает
# import random
# a = random.randint(1,10)
# c = 0
# while c<99:
#     b = int(input('Введите число от 1 до 10: '))
#     c+=1
#     if 0<b<a:
#         print("Загаданное число больше")
#     elif 0<b>a:
#         print("Загаданное число меньше")
#     elif b == 0:
#         print("Остановлено")
#         break
#     elif b == a:
#         print("Вы угадали число с " + str(c) + " попыток")
#         break


# пустой квадрат из звездочек
# w=int(input('Width: '))
# h=int(input('Hight: '))
# for i in range(h):
#     for j in range(w):
#         if i==0 or j==0 or i==(h-1) or j==(w-1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# В ПИТОНЕ МАССИВЫ НАЗЫВАЮТ СПИСКАМИ
# массив [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([i for i in range(10)])

# только четные числа в массиве
# print([i for i in range(10) if i % 2 ==0])

# print([letter * 2 for letter in "Banana"])
# ['BB', 'aa', 'nn', 'aa', 'nn', 'aa']


# len - длина
# nums = [8, 3, 5, 6, 9]
# print(nums[-1])
# nums[-1] = 253
# nums[0] += 100
# print(nums)
# print("Длина списка: ", len(nums))

# s = list("Hello")
# # ['H', 'e', 'l', 'l', 'o']
# print(s)

# n = [5, 1] * 6
# # [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]
# print(n)

# n = list(range(2, 10))
# # [2, 3, 4, 5, 6, 7, 8, 9]
# print(n)

# n = list(range(2, 10))
# n2 = [2, 3, 4, 5, 6, 7, 8, 9]
# print(n)
# print(n2)
# # if n is n2 - проверяет списки по айди
# if n is n2:
#     print("Списки равны")
# else:
#     print("Списки не равны")
# # Списки равны

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# # [1, 4, 9, 16, 25]
# print(a)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# # b += a
# # print(b)
# # [4, 5, 1, 2, 3]
# print(c)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("=>"))
# print(a)
# # [0, 0, 0, 0, 0]
# # =>5
# # =>2
# # =>5
# # =>54
# # =>34
# # [5, 2, 5, 54, 34]

# a = [int(input()) for i in range(int(input()))]
# print(a)
# # 4
# # 1
# # 2
# # 3
# # 4
# # [1, 2, 3, 4]

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# # n: 3
# # -> 1
# # -> 2
# # -> 3
# # [1, 2, 3]

# # сумма отрицательных чисел
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# c = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         c += a[i]
#     else:
#         pass
# print(c)

# 2:00 - 2:08 пересмотреть

# s = list(range(1,8)) # [1, 2, 3, 4, 5, 6, 7]
# print(s)
# print(s[::-1]) # [7, 6, 5, 4, 3, 2, 1]
# print(s[::2]) # [1, 3, 5, 7]
# print(s[1::2]) # [2, 4, 6]
# print(s[:1]) # [1]
# print(s[-1:]) # [7]
# print(s[3:4]) # [4]
# print(s[4:]) # [5, 6, 7]
# print(s[4:1:-1]) # [5, 4, 3]
# print(s[2:5]) # [3, 4, 5]


# # выводит элементы из списка с четными индексами
# # a = [int(input("-> ")) for i in range(int(input("n: ")))]
# a = [5, 1, 9, 7, 6, 3]
# print(a)
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")
# print(" ")
# # выводит элементы из списка, которые больше предыдущего
# # b = [int(input("-> ")) for i in range(int(input("n: ")))]
# b = [2, 9, 4, 6, 3, 5]
# print(b)
# for i in range(len(b)):
#     if b[i] > b[i - 1]:
#         print(b[i], end=" ")


# выводит элементы списка, которые встречаются только один раз
# c = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(c)
# for i in range(len(c)):
#     for j in range(len(c)):
#         if i != j and c[i] == c[j]:
#             break
#     else:
#         print(c[i], end=" ")


# print(dir(list)) # посмореть методы списка
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s.append(99) # добавляет один элемент в конец списка
# print(s)
# s.extend([11, 77 ,66]) # добавляет несколько элементов
# print(s)

# записать в список b все уникальные элементы
# b = []
# for i in range(len(s)):
#     if s[i] not in b:
#         b.append(s[i])
# print(b)


# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# c = []
# for i in range(1, 11):
#     c.append(i * i)
# print(c)


# d = []
# for i in range(1,11):
#     d.extend([i**2])
# print(d)

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# s.insert(2, 100) # добавляем элемент по индексу
# print(s)


# добавляем числа в список
# lst = []
# n = int(input("Кол во элементов списка: "))
# for num in range(n):
#     x = int(input("Число: "))
#     lst.append(x)
# print(lst)


# запрашиваем числа кратные 3 и добавляем их в список
# lst = []
# n = int(input("Кол во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         lst.extend([x])
#     else:
#         print(x, "не делится на 3 без остатка.")
# print(lst)


# добавляет в список "c" одинаковые элементы a and b
# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(j)
# print(c)
# [2, 1, 4, 3]


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c: # если элемент уже в списке, то пропускаем его добавление в список
#             continue
#         if i == j:
#             c.append(j)
# print(c)


# # выводит поочереди один элемент с первого списка и второй элемент с другого списка
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)
# [1, 11, 2, 22, 3, 33]


# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s[2:7] = []
# s.remove(3)# удаляет первый заданный элемент в списке
# last = s.pop(-3) # удаляет по индексу, а так же удаленный элемент можно куда то вывести
# s.clear() # полностью чистит список
# del s[:] # метод удаления списка
# del s # удалит s
# print(s)

# запрашивает список, и удаляет элемент по индексу
# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)


# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# num = s.count(2) # выводит сколько раз встречается цифра 2 в списке
# print(num)
# print(s)
# выведете элементы которые встречаются только один раз

# for i in s:
#     if s.count(i) == 1:
#         print(i, end=" ")


# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# ind = s.index(2, 5) # возвращает положение(индекс) первого попавшегося элемента X(2) списка
# print(ind)

# a = [1, 2, 3]
# a_copy = a.copy() # создаёт независимую копию списка, с другим айди
# print("a = ", a)
# a.append(20)
# print("a = ", a)
# print("a = ", a_copy)


# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s.reverse() # разворачивает список
# print(s)


# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s.sort() # сортирует по возрастанию
# print(s)
# s.sort(reverse=True) # сортирует по убыванию
# print(s)

# s.sort() - изменяет исходный список
# st = sorted(s) - сортирует список, но не меняет исходный
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# st = sorted(s, reverse=True) # встроенная функция сортировки
# print(st)


# запрашивает список, и удаляет элемент который введет пользователь
# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# print("Введите число: ")
# k = int(input("k = "))
# a.remove(k)
# print(sorted(a, reverse=True))


# import random # импорт делается в самом верху ВСЕГДА print(random.random())
# from random import randint, randrange #  print(randint(0, 9))

# print(random.random())
# print(randint(0, 9)) # 9 включительно, обязательно 2 значения указываются
# print(randrange(0, 9)) # (start, stop, step) 9 не входит в диапазон
#
# import random as r # даёт псевдоним методу
# print(r.randint(1,9))


# # принимает массив, выводи его, выводит новый - только положительные,
# # выводит наибольший элемент списка
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# d = []
# m = 0
# print("Список:", a)
# for i in a:
#     if i > 0:
#         d.append(i)
# print("Новый список, состоящий из положительных элементов:", d)
# d.sort(reverse=True)
# m = d.pop(0)
# print("Наибольший элемент списка: ", m)


# # вставляет число "c" в список по индексу "k"
# b = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс: ")
# k = int(input("k = "))
# print("Введите значение: ")
# c = int(input("c = "))
# b.insert(k, c)
# print(b)


# # Заполнить список 10 случайными числами
# # и отсортировать от большего к меньшему
# from random import randint, randrange
# arr = []
# for i in range(1, 10):
#     arr.append(randint(1, 100))
# print(arr)
# arr.sort(reverse=True)
# print(arr)


# # запрашивает список и проверяет есть ли введенное число в списке
# f = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите число:")
# ch = int(input("ch = "))
# for i in range(len(f)):
#     if f[i] == ch:
#         print("Число присутствует в элементах списка")


# from random import randint
# # принимает массив, выводи его, выводит новый - только положительные,
# # выводит наибольший элемент списка
# print("ЗАДАНИЕ 1")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# d = []
# m = 0
# print("Список:", a)
# for i in a:
#     if i > 0:
#         d.append(i)
# print("Новый список, состоящий из положительных элементов:", d)
# d.sort(reverse=True)
# m = d.pop(0)
# print("Наибольший элемент списка: ", m)
#
# print("ЗАДАНИЕ 2")
# # вставляет число "с" в список по индексу "k"
# b = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс: ")
# k = int(input("k = "))
# print("Введите значение: ")
# c = int(input("c = "))
# b.insert(k, c)
# print(b)
#
# print("ЗАДАНИЕ 3")
# # Заполнить список 10 случайными числами
# # и отсортировать от большего к меньшему
# arr = []
# for i in range(1, 10):
#     arr.append(randint(1, 100))
# print(arr)
# arr.sort(reverse=True)
# print(arr)
#
# print("ЗАДАНИЕ 4")
# # запрашивает список и проверяет есть ли введенное число в списке
# print("Введите элементы списка:")
# f = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите число:")
# ch = int(input("ch = "))
# for i in range(len(f)):
#     if f[i] == ch:
#         print("Число присутствует в элементах списка")
# import random as r
# city_list = ["Moscow", "NSK", "Sochi", "SPB"]
#
# print(r.choice(city_list))
#
# s = [55, 66, 77, 88, 99]
# print(r.choice(s))# выводит случайный элемент
#
# s3 = [20, 30 , 40, 50, 60, 70, 80, 90]
# print(r.choices(s3, k=5))#выводит k = случайных элементов
#
# r.shuffle(s3)# перемешывает список
# print(s3)

# print(round(r.uniform(10.5, 25.5), 2))# генерирует число в заданном диапазоне от 10.5 до 25.5
# round округляет число до символом после точки 2 например 16.65

# mas = [i for i in range(10)]# сгенерировать список из 10 чисел
# print(mas)
#
# mas1 = [r.randint(0, 100) for i in range(10)]# 10 чисел в установленном диапозоне
# print(mas1)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))# длина списка
# print(min(lst))# минимальное значение элемента
# print(max(lst))# максимальное значение элемента
# print(sum(lst))# сумма текущих элементов списка

# генерирует список из 10 чисел, вычисляет макс значение и переносит его вначало
# n = [randint(0, 100) for i in range(10)]
# print(n)
# m = max(n)
# print(m)
# n.remove(m)
# n.insert(0, m)
# print(n)
# import math
# import random
# import time
# from random import randint

# n = [randint(-20, 20) for i in range(10)]
# print(n)
# n.sort(reverse=True)
# print(n)

# n = [randint(0, 100) for i in range(10)]
# print(n)
# k = min(n)
# print(k)
# a = n.index(k)
# print("Index: ", a)
# del n[:a]
# print(n)

# проверить есть ли в списке
# x = list('1a2b3')
# print(x)
# print('a' in x)# есть ли в списке
# print('a' not in x)# нету в списке

# # Проверяет пустой ли список
# lst = []
# if len(lst) == 0:
#     print("Список пустой")
#
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")


# n1 = 5
# n2 = 4
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Не повторяющиеся элементы списка а и b", c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Только повторяющиеся: ", c)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(matrix)  # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(matrix[1][2])  # 7
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col], end="\t\t")
#     print()
#
# for row in matrix:
#     for col in row:
#         print(col, end="\t\t")
#     print()
# squared = [[col ** 2 for col in row] for row in matrix]
# for row in squared:
#     for col in row:
#         print(col, end="\t\t")
#     print()

# w, h = 5, 3
# s = [[0 for col in range(w)] for row in range(h)]
# for row in s:
#     for col in row:
#         print(col, end="\t\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# mas = [
#     [2, 5, 8],
#     [5, 8, 2],
#     [8, 7, 1],
#     [0, 7, 1],
#     [9, 11, 6]
# ]
#
# for row in mas:
#     for col in row:
#         print(col, end="\t\t")
#     print()
#
# for i in range(len(mas)):
#     if i % 2 == 0:  # ПРОВЕРЯЕТ ЧЕТНАЯ СТРОКА ИЛИ НЕТ
#         mas[i].sort(reverse=True)
#     else:
#         mas[i].sort()
#
# for row in mas:
#     for col in row:
#         print(col, end="\t\t")
#     print()

# # список + сумма
# n = [randint(0, 100) for i in range(20)]
# print(n)
# print("Сумма: ", sum(n))


# mas = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# for row in mas:
#     for col in row:
#         print(col, end="\t")
#     print()
#
# mas1 = [[0 for j in range(len(mas))] for i in range(len(mas[0]))]
# for j in range(len(mas)):
#     for i in range(len(mas[0])):
#         mas1[i][j] = mas[j][i]
# print(mas1)

# import random as r
# from random import randint

# сгенерировать 10 уникальных чисел
# a = list()
# for i in range(50):  # 1 вариант
# while len(a) != 10:  # 2 вариант, этот лучше
#     w = r.randint(0, 9)
#     if w not in a:
#         a.extend([w])
# print(a)#  [3, 0, 1, 7, 6, 2, 4, 5, 9, 8]


# # Генерирует матрицу и считает произведение чисел больших 0
# w, h = 6, 6
# matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
# print(matrix)
# c = 1
# for row in matrix:
#     for col in row:
#         if col > 0:
#           c += 1
#         print(col, end="\t\t")
#     print()
# print("->>", c)


# # меняет сроки местами 1 с 2, 3 с 4 и тд
# w, h = 6, 6
# matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#     for col in row:
#         print(col, end="\t\t")
#     print()
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         row = matrix[row + 1]
#     else:
#         row = matrix[row - 1]
#     for col in row:
#         print(col, end="\t\t")
#     print()

# 1   2   3   4   5
# 8   9   10  11  12
# 15  16  17  18  19
# 22  23  24  25  26
# 29  30  31
# days = [d for d in range(1, 32)]
# print(days)
# weeks = [days[i:i+5] for i in range(0, len(days), 7)]
# print(weeks)
# for row in weeks:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# from math import *

# print(sqrt(2))
# print(floor(3.8))  # округление в меньшую сторону 3
# print(ceil(3.2))  # округление в большую сторону 4
# print(pi)

# rad = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * rad, 2))

# lst = [1, 5, 3, 8.4]
# print(sum(lst))
# print(fsum(lst))
# print(degrees(3.14159))  # перевод из радиан в градусы
# print(radians(180))  # из градусов в радианы
# print(cos(radians(60)))
# print(sin(radians(60)))


# # найти гипотенузу 2-х катетов
# a = int(input('Катет 1: '))
# b = int(input('Катет 2: '))
#
# print('Гипотенуза равна: ', sqrt((a**2)+(b**2)))

# import time
# seconds = time.time()
# print(seconds)
# local_time = time.ctime(seconds)
# print(local_time)
# res = time.localtime(seconds)
# print(res)
# print(res.tm_hour)
#
# print(time.strftime("Today is %B %d, %Y"))  # Today is January 27, 2022
# # в папке 7 есть все эти модули как пишутся и что означают
# print(time.strftime("Today is %B %d, %Y", time.localtime(1111111111)))  # Today is March 18, 2005
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(1111111111)))  # 03/18/2005, 08:58:31

# pause = 5
# print("Program started...")
# time.sleep(pause)  # ОСТАНАВЛИВАЕТ ВЫПОЛНЕНИЕ ПРОГРАММЫ НА ЗАДАННОЕ ЧИСЛО СЕКУНД
# print(pause, "seconds")

# text = input("Название: ")
# t = float(input("Через сколько минут: "))
# t *= 60
# time.sleep(t)
# print(text)


#  СОЗДАЕТ МАТРИЦУ И ВЫВОДИТ МИНИМАЛЬНЫЙ ЭЛЕМЕНТ МАТРИЦЫ
# from random import randint
# x = int(input("Размерность массива: "))
# print("Массив из случайных чисел от 1 до 100:")
# matrix = [[randint(1, 100) for i in range(x)] for j in range(x)]
# min1 = matrix[0][0]
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#     print()
# for i in range(x):
#     for j in range(x):
#         if matrix[i][j] < min1:
#             min1 = matrix[i][j]
# print("Минимальный элемент массива: ", min1)


#  СОЗДАЕТ МАТРИЦУ, СОЗДАЕТ ОТДЕЛЬНЫЙ СПИСОК И МЕНЯЕТ ВСЕ
#  НЕЧЕТНЫЕ СТРОКИ МАТРИЦЫ НА ОТДЕЛЬНЫЙ СПИСОК
# from random import randint
# print("Массив из случайных чисел от 1 до 100:")
# m = [[randint(1, 10) for i in range(6)] for j in range(6)]
# for row in m:
#     for col in row:
#         print(col, end="\t")
#     print()
# n = [randint(1, 10) for i in range(6)]
# print(n)
# for row in range(len(m)):
#     if row % 2 == 0:
#         row = n
#     else:
#         row = m[row]
#     for col in row:
#         print(col, end="\t")
#     print()


# import time
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# result = finish - start
# print(result)

import time
import locale #  ПЕРЕВОДИТ ПОД НУЖНУЮ СТРАНУ
locale.setlocale(locale.LC_ALL, "") #  РОССИЯ
print(time.strftime("Сегодня: %B %d, %Y", time.localtime())) #  Сегодня: Январь 31, 2022

