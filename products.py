import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,73,8])
print(np.prod(a)) #Products
print(np.prod([a,b])) # product of two arrays:
print(np.prod([a,b],axis=1)) #Product Over an Axis


c=np.array([5,6,7,8])
print(np.cumprod(c))
