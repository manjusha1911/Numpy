# By default the left most index is returned,
#  but we can give side='right' to return the right most index instead.
import numpy as np
a=np.array([6,7,8,9,2])
print(np.searchsorted(a,7,side="right"))