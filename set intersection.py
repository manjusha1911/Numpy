import numpy as np
a=np.array([1,2,3,4,5,11])
b=np.array([1,20,30,4,50,11])
print(np.intersect1d(a,b,assume_unique=True))