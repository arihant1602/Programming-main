def myFunc(**kwargs):
    for a,b in kwargs.items():
        print(a," ",b)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

myFunc(brand = "Ford",
  model = "Mustang",
  year = "1964")
