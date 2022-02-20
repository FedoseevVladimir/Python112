# 1
print()
color = ['red', 'green', 'blue']
color_num = ['#FF0000', '#008000', '#0000FF']
c = dict(zip(color, color_num))
print(c)  # {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
print()

# 2
a = {i: i * i * i for i in range(1, 11)}
print(a)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
print()

# 3
d1 = ['color', 'fruit', 'pet']
d2 = ['blue', 'apple', 'dog']
d = {x: y for x, y in zip(d1, d2)}
print(d)  # {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
print()


# 4


def mi_n(s):
    return min(s)


print(mi_n([10, 9]))  # 9
print(mi_n([2, 3, 4]))  # 2
print(mi_n([3, 5, 10, 6]))  # 3
print()

# 5
a = [3, 5, 10, 6, 3]


def su_m(s):
    c = a[0]
    d = len(a) + 1
    for elem in range(d):
        print(c, end=' ')
        c += a[elem + 1]


print(su_m(a))
# Traceback (most recent call last):
#     c += a[elem + 1]
# IndexError: list index out of range
# 3 8 18 24 27
# значения выдаёт, но с ошибкой, я понимаю, что, когда цикл доходит до последнего
# элемента, то сослаться на несуществующий a[elem + 1] он не может и выдает ошибку,
# пытался как то это наладить, никак не удалось :(