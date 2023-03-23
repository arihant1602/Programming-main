print("Enter the number")
num = int(input())
x = 0
flag = True
while(flag):
    power = 2 ** x
    if power == num:
        flag = False
    elif power > num:
        x -= 1
        flag = False
    else:
        x += 1
while(a):
    bnum = 1 * (10 ** (x+1))
    
print(x)