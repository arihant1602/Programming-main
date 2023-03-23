print("Input the length of array")
arrl = int(input())
k = 0
a = []

i = 0
print("Input the array")
for i in range(arrl):
    temp = str(input())
    a.append(temp)

for i in a:
    if len(i) == 3:
        print(i)
        k += 1
    
print(f"There are {k} such elements")