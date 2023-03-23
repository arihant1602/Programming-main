print("Enter the string")
ipt = input()
stack = []
ns = []
for i in range(len(ipt)):
    if ipt[i] == ")":
        ns.append("(")
    elif ipt[i] == "}":
        ns.append("{")
    elif ipt[i] == "]":
        ns.append("[")
    else:
        ns.append(ipt[i])
print(ns)
print(ns[-1])
stack.append(ns[-1])
print(stack[-1])
for i in range(len(ns)-1):
    if len(ns) == 0:
        break
    if stack[-1] == ns[-1]:
        stack.pop()
        ns.pop()
        stack.append(ns[-1])
    else:
        stack.append(ns[-1])
        ns.pop()

print(stack)