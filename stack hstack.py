import numpy as np   #1D-array
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.hstack((a,b)))

# O/P: [1 2 3 4 5 6]


import numpy as np  # 2-D array
a=np.array([[1,2,3],[11,12,13]])
b=np.array([[4,5,6],[14,15,16]])
print(np.hstack((a,b)))
# O/P:
# [[ 1  2  3  4  5  6]
#  [11 12 13 14 15 16]]