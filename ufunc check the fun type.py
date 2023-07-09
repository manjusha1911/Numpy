import numpy as np
# print(type(np.add))   #O/P <class 'numpy.ufunc'>
print(type(np.concatenate)) 


if type(np.add)==np.ufunc:
    print("add is ufunc")
else:
    print("add is not")