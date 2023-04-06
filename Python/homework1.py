def strlen(str):
    a = 0
    for i in str:
        a += 1
    return a




def username(email):
    usr = email[0:(email.find('@'))]
    return usr




def checkPallindrome(str):
    if str == str[::-1]:
        return True
    return False




def toTitle(str):
    arr = str.split(" ")
    newLs = []
    newStr = ""
    for i in arr:
        if ord(i[0]) >= 97 and ord(i[0]) <= 122:
            newStr += chr((ord(i[0])) - 32)
            newStr += i[1:]
        else:
            newStr = i
        newLs.append(newStr)
        newStr = ""
    return (" ".join(newLs))




def triangle(layers):
    if layers:
        print(1,end="")
        layers -= 1
    for i in range(1,layers+1):
        print("")
        a = 1
        while i:
            print(a, end="")
            a += 1
            i -= 1
        while a:
            print(a, end="")
            a -= 1
    print("")
        



s = "Sample string and some sample text"

print(strlen(s))
print(username("arihant@gmail.com"))
triangle(5)
print(checkPallindrome(s))
print(toTitle(s))
