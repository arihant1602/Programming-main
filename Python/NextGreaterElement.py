a = []
print("Enter length of list")
listlen = int(input())
print("Enter list")
for i in range(listlen):
    ipt = int(input())
    a.append(ipt)
i = 0
'''
while i < listlen:
    j = i + 1
    while j < listlen:
        if a[j] > a[i]:
            a[i] = a[j]
            break
        j += 1
    else:
        a[i] = -1
    i += 1
'''
print(a)