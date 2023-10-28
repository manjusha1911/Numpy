from math import log
import numpy as np
x=np.frompyfunc(log,2,1)
print(x(100,50))