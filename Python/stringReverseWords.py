def reverseWords(str):
    new = []
    print(str.split())
#    str = str.strip() <= space hatata hai
    for i in str.split():
        print(i)
        i = (i.lower())[:-1] + (i[-1].upper())
        new.append(i[::-1])
    return (" ".join(new))

print(reverseWords("Hello and my name is Arihant"))

string = "Hello and my name is Arihant"
string = string.replace("my", "your")
print(string)

listt = [*range(100,1000, 100)]
print(listt)