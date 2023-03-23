import re
print("Enter the string")
string = input()
names = re.findall(r'\w\w\w+', string)
ages = re.findall(r'\d+', string)
myDict = {}
j = 0
for i in names:
    myDict[i] = ages[j]
    j += 1
print(myDict)
