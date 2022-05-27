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
