print("Enter Length Of List")
listLen = int(input())
print("Enter the list")
a = []
for i in range(listLen):
    ipt = input()
    a.append(ipt)
print("Enter no of elements to rotate by")
rotate = int(input())
a = a[listLen-rotate:]+a[:listLen-rotate]
print(a)
a = a[-(listLen-rotate):]+a[:-(listLen-rotate)]
print(a)
