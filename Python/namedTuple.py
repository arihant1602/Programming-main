from collections import namedtuple
a = namedtuple('a2', ['name', 'age', 'city', 'country'])
b = a('arihant', 15, 'Moradabad', 'India')
print(b)
print(b[1])
print(b.age)
