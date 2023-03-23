import numpy as np 
ar = np.zeros(10)
arr = np.ones(5) + 4
print(arr)
arr = np.linspace(1, 20, 10)
print(arr)
arr = np.arange(25)
print(arr.sum(axis=0))
b = arr > 10
c = arr[b]
# c = arr[arr>10]
print(b)
print(c)