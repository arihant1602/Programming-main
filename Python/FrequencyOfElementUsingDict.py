from InputArray import arrayInput
a = []
arrayInput(a)
myDict = {}
for i in a:
    if i in myDict.keys():
        myDict[i] += 1
    else:
        myDict[i] = 1
for i in a:
    if myDict[i] == 1:
        print("--------",endl,i)
        break

print(myDict)
