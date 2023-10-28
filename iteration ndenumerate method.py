
#1-D array
import numpy as np
a=np.array([1,2,3])
for x,y in np.ndenumerate(a):
    print(x,y)
"""
(0,) 1
(1,) 2
(2,) 3
"""

# 2-D array
b=np.array([[1,2,3,4],[5,6,7,8]])
for indx,x in np.ndenumerate(b):
    print(indx,x)
#o/p
'''
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8
'''
