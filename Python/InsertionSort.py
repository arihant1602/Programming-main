print("Enter length of array")
arrlen = int(input())
a = []
print("Enter the list")
for i in range(arrlen):
    ipt = int(input())
    a.append(ipt)
i = 1
print(arrlen)

for i in range(1, 5):
    x = a[i]
    j = i - 1
    while j >= 0 and x < a[j]:
        print("adsad")
        a[j+1] = a[j]
        j -= 1
    a[j+1] = x

'''
for i in range(1, len(a)):
    x = a[i]
    j=i-1
    while j >= 0 and x < a[j] :
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = x    
    '''
print(a)