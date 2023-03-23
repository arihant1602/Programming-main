from collections import *
print("Enter the sentence")
sent = input()
a = sent.split()
print(Counter(a))


















'''
counter = defaultdict(int)
word = ""
for i in range(len(sent)):
    if i == len(sent)-1:
        word += sent[i]
        counter[word] += 1
    elif sent[i] == " ":
        counter[word] += 1
        word = ""
    else:
        word += sent[i]
print(counter)
'''