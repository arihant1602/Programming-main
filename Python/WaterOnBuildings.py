a = []
print("Enter the length of list")
lslen = int(input())
print("Enter the list")
for i in range(lslen):
    x = int(input())
    a.append(x)
print(a)
left = []
right = []
for i in range(lslen):
    if i == 0:
        left.append(a[i])
    elif a[i] > left[i-1]:
        left.append(a[i])
    elif a[i] < left[i-1]:
        left.append(left[i-1])
print(left)
water = []
for i in range(lslen):
    right.append(0)
    water.append(0)
for i in range(lslen - 1, -1, -1):
    if i == lslen - 1:
        right[i] = a[i]
    elif a[i] > right[i+1]:
        right[i] = a[i]
    elif a[i] < right[i+1]:
        right[i] = right[i+1]
print(right)
for i in range(lslen):
    water[i] = min(right[i], left[i]) - a[i]
print(water)
maxarea = 0
for i in water:
    if i == 0:
        summ = 0
    else:
        summ += i
        if   summ > maxarea:
            maxarea = summ
print(maxarea)
