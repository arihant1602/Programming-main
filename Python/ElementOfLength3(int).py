print("Input the length of array")
arrl = int(input())
count = 0
a = []
elementCount = 0
i = 0
print("Input the array")
for i in range(arrl):
    temp = int(input())
    a.append(temp)
i = 0
print("-----------------------")
for i in a:
    temp2 = i
    while temp2 > 0:
        temp2 = int(temp2/10)
        count += 1
    if count == 1:
        print(i)
        elementCount += 1
    count = 0
print(f"There are {elementCount} such elements")
