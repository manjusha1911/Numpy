import numpy as np
a=np.array([4,2,3])
print(np.prod(a)) #24

a=np.array([4,2,3])
b=np.array([1,2,1])
print(np.prod([a,b]))

print(np.prod([a,b],axis=1))
