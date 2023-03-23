lst = []
temp = []
print("Enter the length of list")
lsLen = int(input())
print("Enter the list")
for i in range(lsLen):
    ipt = input()
    lst.append(ipt)
setL = set(lst)
count = 0
for i in lst:
    temp.append(i)
    temp2 = list(set(temp))
    temp2.sort()
    if setL is set(temp): 
        count = min(len(temp), count)
        temp.clear()
        count = 0
    else:
        count += 1
print(count)