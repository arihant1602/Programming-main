# abCDeFghiJKLMnO
# abeghinCDFJKLM

def lful(str):
    new1 = ""
    new2 = ""
    for i in str:
        if i.upper() == i:
            new1 += i
        elif i.lower() == i:
            new2 += i
        else:
            print("invalid input")
            return 0
    return (new2+new1)

print(lful("abCDeFghiJKLMnO"))