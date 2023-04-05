s = "My name is Arihant"


# 3 included, 10 not included
print(s[3:10])

a = (s + " ")*5

print(a)

print('pune' < 'delhi')

strlen = len(s)

print(strlen)

print(max(s))

print(sorted(s, reverse=True))

print(s.title())

# s.capitalize()
# s.upper()
# s.lower()
# s.swapcase()
# s.find('Ari')
# s.index('z') agar cheez nahi hai toh error throw karega
# s.startswith("My") => True
# s.endswith("hant") => True

name = "Arihant"
age = 15
print("My name is {} and i am {} years old.".format(name,age))
print("My name is {1} and i am {0} years old.".format(age,name))

# s.isdigit()
# s.isalpha()
# s.isalnum()

print(s.split('n'))

