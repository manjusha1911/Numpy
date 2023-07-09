# splitting 3 parts:

import numpy as np
a=np.array([1,2,3,4,5,6])
print(np.array_split(a,3))
# O/P :[array([1, 2]), array([3, 4]), array([5, 6])]


# Splitting 4 parts:

import numpy as np  
a=np.array([1,2,3,4,5,6])
print(np.array_split(a,4))
# O/P :[array([1, 2]), array([3, 4]), array([5]), array([6])]


a=np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(np.array_split(a,3))  #Split the 2-D array into three 2-D arrays.
#O/P
'''
[array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]]), array([[ 9, 10],
       [11, 12]])]
'''

# Split the 2-D array into three 2-D arrays along rows.
a=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(np.array_split(a,3,axis=1))

#O/P
'''
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
'''