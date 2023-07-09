import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a.shape) #o/p: (2,5)


import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
    #O/P
# [[[[[1 2 3 4]]]]]
# shape of array : (1, 1, 1, 1, 4)

'''
Integers at every index tells 
about the number of elements the corresponding dimension has.
In the example above at index-4 we have value 4,
 so we can say that 5th ( 4 + 1 th) dimension has 4 elements.

'''
