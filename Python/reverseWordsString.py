string = input("Enter the string\n")
words = ""
count = 0
for i in string.split(" "):
    count += 1
    words += i[::-1]
    if count == len(string.split()):
        break
    words += " "
print(words)