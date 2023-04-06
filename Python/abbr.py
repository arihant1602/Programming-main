def abbreviation(str):
    arr = str.split()
    new = ""
    for i in arr:
        new += i[0].upper()
    return new

print(abbreviation("Delhi Public School"))