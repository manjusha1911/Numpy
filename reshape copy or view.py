import numpy as np
a=np.array([1,2,3,4,5,6,7,8])
print(a.reshape(2,4).base)  #o/p [1 2 3 4 5 6 7 8]
# returns the original array, so it is a view.