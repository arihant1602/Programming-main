print("Enter the number")
n = int(input())
j = 0;
for i in range( 2 , n/2 ):
    if n % i != 0:
        j += 1;
if j > 0:
    print("Composite")
else:
    print("Prime")
