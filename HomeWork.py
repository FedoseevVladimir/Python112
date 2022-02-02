# print("Hello World, I'am on GitHub")
# sep=""   убирает пробелы

def hello(name, word):  # аргументы
    print("Hello, ", name, ". Say ", word, sep="")


hello("Irina", "hi")  # параметры
hello("Ivan", "hello")


def get_sum(a, b):
    print(a + b)


x = 2
y = 5
get_sum(x, y)
get_sum("abc", "def")  # если слова то делается конкатенация
get_sum(2.5, 4.3)
# get_sum(2.5, "4.5")  # разные типы данных нельзя складывать
