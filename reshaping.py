import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a.reshape(2,5))
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
'''
print(a.reshape(5,2))

# o/p
'''
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]]
'''