import numpy as np
a=np.array([1,2,3])
b=np.array([1,2,3])
print(sum([a,b]))
print(np.sum([a,b],axis=1))
print(np.cumsum(a))