print("Enter the size of array")
arrayLen = int(input())
arr = []
print("Enter the array")
for i in range(arrayLen):
    x = int(input())
    arr.append(x)
commonDif = arr[arrayLen-1] - arr[arrayLen-2]
for i in range(arrayLen-1):
    if arr[i+1] - arr[i] < commonDif:
        commonDif = a[i+1] - a[i]
for i in range(arrayLen-1):
    if arr[i+1] - arr[i] == 2*commonDif:
        print(arr[i]+commonDif)
    