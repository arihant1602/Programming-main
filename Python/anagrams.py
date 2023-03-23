words = []
print("Enter the length of list")
lsLen = int(input())
print("Enter the list")
for i in range(lsLen):
    ipt = input()
    words.append(ipt)
print("Enter the word to look anagrams for")
check = input()
check = list(check)
count = 0
for i in words:
    flag = True
    temp = list(i)
    for x in check:
        if x not in temp:
            flag = False
            break
        temp.remove(x)
    if flag and not temp:
        count += 1
print(count)
