# 1
def decorator_sr(func):
    def wrapper(*args):
        val1 = func(*args)
        val = val1 / len(args)
        print('Cумма чисел ', *args, '=', val1)
        print('Ср.арифм: ', *args, '=', val)

    return wrapper


@decorator_sr
def summa(*args):
    c = 0
    for k in args:
        c += k
    return c


summa(2, 3, 3, 4)
# Cумма чисел  2 3 3 4 = 12
# Ср.арифм:  2 3 3 4 = 3.0
print()


# 2
def change_char_to_str(w, old, new):
    s2 = ''
    g = 0
    while g < len(w):
        if w[g] == old and g % 2 == 0:
            s2 = s2 + new
        else:
            s2 = s2 + w[g]
        g += 1
    return s2


str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный'
str2 = change_char_to_str(str1, 'N', 'P')
print('str1 = ', str1)
print('str2 = ', str2)
# str1 =  Я изучаю Nython. Мне нравится Nython. Nython очень интересный
# str2 =  Я изучаю Nython. Мне нравится Python. Python очень интересный
print()


# 3
def del_letter(x, arr):
    for j in arr:
        if x == arr.index(j):
            pass
        else:
            print(j, end='')


s = '0123456789'
print('s = ', end='')
for i in s:
    print(i, end='')
print()
print('s2 = ', end='')
del_letter(5, s)
# s = 0123456789
# s2 = 012346789
print()
print()


# 4
def func1(x, arr):
    x = str(x)
    for j in arr:
        if x != j:
            print(j, end='')


s = '132333435363738393'
print('s = ', end='')
for i in s:
    print(i, end='')
print()
print('s2 = ', end='')
func1(3, s)
# s = 132333435363738393
# s2 = 12456789
