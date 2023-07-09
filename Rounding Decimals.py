'''
truncation
fix
rounding
floor
ceil
'''

# truncation & fix
import numpy as np
print(np.trunc([-3.1666,3.6667]))
print(np.fix([-3.1666,3.6667]))
# O/P:[-3.  3.]


'''rounding'''
print(np.round(3.1756,2))  #3.18


'''floor'''
print(np.floor([-2.1666,3.6667]))


'''ceil'''
print(np.ceil([-3.666,3.1666,3.1,3.100]))