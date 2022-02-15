# 1
a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
b = {'name': 'Kelly', 'salary': 8000}
for key in list(iter(a)):
    for keys in b.keys():
        if key == keys:
            del a[key]
print(a)
print(b)

# 2
a['location'] = a.pop('city')
print()
print(a)
