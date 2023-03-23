ls = []
print("Enter the length of list")
lslen = int(input())
print("Enter the list")
for i in range(lslen):
    ipt = input()
    ls.append(ipt)
print("Enter the pattern")
pat = input()
print("Enter the length of prefix")
prLen = int(input())
j = 0
count = 0
for i in ls:
    if pat[:prLen] == ls[j][:prLen]:
        count += 1
    j += 1
print(count)
