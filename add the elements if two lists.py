x=[1,2,3,4]   #list
y=[5,6,7,8]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)

import numpy as np
a=[1,2,3,4]
b=[5,6,7,8]
print(np.add(a,b))