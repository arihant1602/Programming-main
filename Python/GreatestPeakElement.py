from InputArray import arrayInput
a = []
greatest = 0
arrayInput(a)
highest = 0
if len(a) == 1:
    print(f"The greatest peak element is {a[0]}")
else:
    for i in range(1, (len(a)) - 1):
        if (a[i] > a[i + 1] and a[i] > a[i-1]) and a[i] > greatest:
            greatest = a[i]
        if (a[i] > highest):
            highest = a[i]
        if a[i+1] > highest:
            highest = a[i+1]
        if a[i-1] > highest:
            highest = a[i-1]
    if greatest == 0:
        print(f"The greatest peak element is {highest}")
    else:
        print(f"The greatest peak element is {greatest}")
