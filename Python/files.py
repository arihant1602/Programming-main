'''
l = ["Hellooo", "Again hello", "Return of Hello"]

f = open('sample.txt', 'w')
f.write("Helloooo\n")
f.write("How u")
f.writelines(l)
f.close()

f = open('sample.txt', 'a')
f.write("\nApeeeennnd")
f.close()

f = open('sample.txt', 'r')
print(f.readline())
print(f.read(10))
print(f.readlines())
f.close()

with open('sample.txt', 'r') as f:
    print(f.read())
'''
with open("Python/Parenthesis.jpeg", "rb") as f:
    with open('pic.jpeg', 'wb') as fb:
        fb.write(f.read()) 

a = [1,2,3,4,5]
with open("sample.txt", "w") as f:
    f.write(str(a))

ab = {
    'name':'arihant',
    'age':'16',
    'city':'mbd'
}

with open("sample.txt", 'a') as f:
    f.write("\n")
    f.write(str(ab))

with open("sample.txt", 'r') as f:
    print(f.read())

