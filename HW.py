print('Задание 1 элементы первой строки которые отсутствуют во второй строке')
a = 'Python'
print('Первая строка: ', a)
b = 'Programming language'
print('Вторая строка: ', b)
print('Искомыми буквами являются: ')
c = set(a) - set(b)
for i in c:
    print(i, end=' ')

print('\n\nЗадание 2 выводит количество гласных в строке')
d = 'Hello world'
print(d)


def vowels(x):
    count = 0
    set_d = list(d)
    vowels_str = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in x:
        if i in vowels_str:
            count += 1
    return count


print('Numbers of vowels: ', vowels(d))

print('\n\nЗадание 3 общие элементы двух строк')
str1 = 'test'
print('Первая строка: ', str1)
str2 = 'string'
print('Вторая строка: ', str2)
letter = set(str1) | set(str2)
print('Искомые буквы: ')
for i in letter:
    print(i, end=' ')

print('\n\nЗадание 4 только уникальные элементы двух строк')
str3 = 'hello'
print('Первая строка: ', str3)
str4 = 'world'
print('Вторая строка: ', str4)
letter1 = set(str3) | set(str4)
letter2 = set(str3) & set(str4)
l = letter1 - letter2
print('Искомые буквы: ')
for i in l:
    print(i, end=' ')
