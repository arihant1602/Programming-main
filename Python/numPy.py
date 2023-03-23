import numpy as np 

a = np.array([1,2,3,4])
print(a)

arr = np.arange(0,10,2)
#arr = arr(+,-,/,x,**)arr 
#arr = np.sqrt(arr)
print(arr)

ar = np.zeros(25).reshape(5,5)  #ones
#ar = ar.reshape(5,5)
print(ar)

ary = np.linspace(0, 6, 4) 
print(ary)
#pehli dono values ke beech me equal difference wale 3rd value numbers

ari = np.random.rand(5,3)
#ari = np.random.randint(1,10)
#print(arr[:3,:3])
print(ari)

aro = np.arange(10)
aro[:5] = 9
#c = arr.copy()
print(aro)


b = np.hstack((arr , aro))
#np.vstack
print(b)