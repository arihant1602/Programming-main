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