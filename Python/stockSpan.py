a = []
count = 0
top = -10000
stack = [0]
span = [1]
print("Enter the length of list")
lslen = int(input())
print("Enter the list")
for i in range(lslen):
    ipt = int(input())
    a.append(ipt)
print(a)
tmp = 0
for i in range(1,lslen):
    while len(stack) != 0 and a[stack[-1]] <= a[i]:
        stack.pop()
    print(stack)
    if len(stack) == 0:
        span.append(i + 1)
    else:
        span.append(i - stack[-1])
    stack.append(i)
print(span)
    
