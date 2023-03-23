from collections import OrderedDict
from collections import defaultdict
dictNormal = {'name' : 'Arihant', 'age' : 15}
dictOrdered = OrderedDict({'name' : 'Arihant', 'age' : 15,'a' : '1', 'color' : 'blue'})
print(dictNormal)
print(dictOrdered)
print(dictNormal.values())
print(dictOrdered)
def func():
    return "None"
dictDefault = {"a" : 2, "b" : 1}
dictDefault = defaultdict(func)
print(dictDefault["a"])
dictDefault["d"] = 3
print(list(dictDefault.items()))
