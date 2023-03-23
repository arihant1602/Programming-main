print("Enter the length of array")
arrayLen = int(input())
print("Enter the array")
a = []
t = []
flag = 0
for i in range(arrayLen):
    x = int(input())
    a.append(x)
print("-------------")
for i in range(arrayLen-1):
    for j in range(i+1,arrayLen):
        if a[i] == a[j]:
            print(a[i])
            flag = 1
            break
    if flag == 1:
        break   

