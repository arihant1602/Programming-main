import FactorialFunction as ff 

import random
print("Enter the length of array")
arrayLen = int(input())
nums = []
print("Enter the array")
for i in range(arrayLen):
    inputs = int(input())
    nums.append(inputs)
newArray = []
while len(newArray) < ff.factorial(arrayLen):
    tempArray = random.sample(nums, arrayLen)
    if tempArray in newArray:
        continue
    else:
        newArray.append(tempArray)
print(newArray)
 