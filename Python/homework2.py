def ratRevUpsideDown(layers):
    for i in range(layers):
        t = layers - i + 1
        while t:
            t -= 1
            if t:
                print(t,end="")
        print("")


def horizontalIsosceles(layers_vertical):
    for i in range(layers_vertical+1):
        print("a"*i)
    while i:
        i -= 1
        print("a"*i)


def verticalIsosceles(layers):
    for i in range(layers+1):
        print(" "*(layers-i), "a"*((2*i)-1))


def ratRev(layers):
    for i in range(1,layers+1):
        while i:
            print(i, end="")
            i -= 1
        print("")



print("")
ratRevUpsideDown(5)
print("")
horizontalIsosceles(5)
print("")
verticalIsosceles(5)
print("")
ratRev(5)