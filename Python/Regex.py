import re
# \d -> digit
# \w -> alphanumeric
# \s -> space
pat = 'phone'
text = "This is a phone no 777-888-9876 twice phone"
match = re.search(pat, text)
matches = re.findall(pat, text)
print(match.span())
print(match.start())
print(match.end())
print(matches)
for i in re.finditer(pat, text):
    print(i.span())
phone = re.search(r'\d\d\d-\d\d\d-\d{4}', text)
print(phone.group())
print(re.findall(r'...at', "the cat sat on mat and wore hat"))
print(re.findall(r'[^\d]',"tahsdunauond 3qdsioa 1 iadsn 3"))
# * -> 0 or more times
# ? -> 1 or 0 times
# + -> 1 or more times
