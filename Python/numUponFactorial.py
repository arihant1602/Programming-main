def factorial(num):
    fact = 1
    while num:
        fact *= num
        num -= 1
    return fact


def numByFactorialAP(num):
    result = 0.0
    while num:
        result += num/(factorial(num))
        num -= 1
    return result


print(numByFactorialAP(3))