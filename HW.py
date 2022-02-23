def func(figure_type='figure', **data):
    res = 1
    if figure_type == 'rhombus':
        res = (data['d1'] * data['d2']) / 2
        return res
    elif figure_type == 'square':
        res = data['a'] * data['a']
        return res
    elif figure_type == 'trapezoid':
        res = 0.5 * ((data['a'] + data['b']) * data['h'])
        return res
    elif figure_type == 'circle':
        res = 3.14 * (data['r'] ** 2)
        return res
    else:
        a = 'invalid data'
        return a


print(func(figure_type='rhombus', d1=10, d2=8))
print(func(figure_type='square', a=5))
print(func(figure_type='trapezoid', a=12, b=3, h=6))
print(func(figure_type='circle', r=18))
print(func(figure_type='unknown', a=1, b=2, c=3))

# выводит:
# 40.0
# 25
# 45.0
# 1017.36
# invalid data
