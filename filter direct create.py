import numpy as np
a=np.array([41,42,43,44])
x=a>42
print(x)
print(a[x])

b=np.array([1,2,3,4,5,6,7,8,9,10])
x=b%2==0
y=b%2==1
print(x)
print(b[x])
print(y)
print(b[y])

#o/p
'''
[False  True False  True False  True False  True False  True]
[ 2  4  6  8 10]
[ True False  True False  True False  True False  True False]
[1 3 5 7 9]
'''