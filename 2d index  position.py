import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[0,1:3])#From the first element, slice elements from index 1 to index 3 
# O/p
# [2 3]
print(a[0:3,3])#From both elements, return index 2

# O/p
# [4 9]

print(a[0:2,1:4])

# o/p
# [[2 3 4]
#  [7 8 9]]