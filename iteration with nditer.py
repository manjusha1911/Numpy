import numpy as np
a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for i in np.nditer(a):
    print(i)

#o/p
'''
1
2
3
4
5
6
7
8
'''