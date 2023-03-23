from collections import Counter
from InputArray import arrayInput
a = []
arrayInput(a)
b = list(Counter(a))
print(b)
