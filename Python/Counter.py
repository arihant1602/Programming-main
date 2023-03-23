from collections import Counter
'''
o = Counter('Hello World!')
print(o)
ok = Counter([ 1, 2, 3, 54, 54, 54, 1, 2, 1])
print(ok)
print(o['l'])

oki = Counter(a = 4, b = 3, c = 4)
print(list(oki.elements()))
print(oki.most_common(1))
l = [ 'a', 'b', 'a', 'a', 'a', 'a', 'b', 'c']
oki.subtract(l)
print(oki)
oki.update(l)
print(oki)
oki.clear()
print(oki)
'''
var1 = Counter(a = 4, b = 2, c = 6)
var2 = Counter(a = 2, b = 4, c = 3, d = 1)
print(var1 + var2)
print(var1 - var2)
print(var1 | var2)
print(var1 & var2)
