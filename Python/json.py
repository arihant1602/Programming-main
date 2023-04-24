import json
a = [1,2,3,4,5]
ab = {
    'name':'arihant',
    'age':'16',
    'city':'mbd'
}

class mine:
    def __init__(self,fname,lname,age,city):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.city = city

obj = mine('Arihant', 'Pratap Singh', '16', 'Moradabad')

def func(obj):
    return "My name is {} {} and age is {} and I live in {}.".format(obj.fname,obj.lname,obj.age,obj.city)

with open("sample.json", 'w') as f:
    json.dump(obj, f, default=func)

with open("sample.json", 'r') as f:
    print(json.load(f))