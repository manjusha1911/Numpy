import numpy as np
a=np.array([1,2,3,4,5])
c=a.copy()
a[0]=50
print(a)
print(c)

#o/p
'''
[50  2  3  4  5]
[1 2 3 4 5]
'''

a=np.array([1,2,3,4,5])
v=a.view()
a[0]=50
print(a)
print(v)

#o/p
'''
[50  2  3  4  5]
[50  2  3  4  5]
'''
