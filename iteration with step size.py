import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(a[:,::2]):
    print(i)  #o/p:1,3,5,7
for x in np.nditer(a[1:,::2]):
    print(x)  #o/p:5,7