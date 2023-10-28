import numpy as np
a=np.array([1,2,3,4,5])
x=a.copy()
y=a.view()
print(x.base)
print(y.base)

#o/p
'''
None
[1 2 3 4 5]
'''