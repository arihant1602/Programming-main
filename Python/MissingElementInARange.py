print("Enter length of array")
arrayLen = int(input())
a = []
print("Enter the range of numbers")
rangeStart = int(input())
rangeEnd = int(input())
print("Enter the array")
for i in range(arrayLen):
    x = int(input())
    a.append(x)
for i in range(rangeStart,rangeEnd+1):
    if i in a:
        continue
    else:
        print(i)