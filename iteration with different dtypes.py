import numpy as np
a=np.array([1,2,3,4,5])
for i in np.nditer(a,flags=["buffered"],op_dtypes=['S']):
    print(i)