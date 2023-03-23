def myFunction(a1, a2, a3):
    percentage = (a1+a2+a3)/3
    return percentage
percentages = []
for i in range(5):
    print(f"Enter marks of student {i} of 3 subjects")
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    percentage_of_3 = myFunction(a1, a2, a3)
    percentages.append(percentage_of_3)
print(percentages)
