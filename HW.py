# 1
a = [3, 6, 8, 9, 1, 2]
print(list(map(lambda x: x * a.index(x) ** 3, a)))  # [0, 6, 64, 243, 64, 250]
print()
# 2
b = [3, -4, -6, 7, -8, 3, -12, 4, 7]
s = list(filter(lambda x: x < 0, b))
print(s)
print(abs(sum(s)))
print()
# 3
nums = [3, 5, 7, 3, 9, 5, 7, 2]
print(list(map(lambda x: x ** 2, nums)))
print(list(map(lambda x: x ** 3, nums)))
print()


# 4
def func_compute(n):
    def inner(x):
        return n * x

    return inner


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))
print()
