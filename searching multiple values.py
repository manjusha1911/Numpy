import numpy as np
a=np.array([1,3,5,7])
print(np.searchsorted(a,[2,4,6]))

# O/P:[1 2 3]
# The return value is an array: [1 2 3] 
# containing the three indexes 
# where 2, 4, 6 would be inserted in the original array to maintain the order.


