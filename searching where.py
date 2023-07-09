import numpy as np
a=np.array([1,2,3,4,5,4,5,6,5,7,5])
print(np.where(a==5))
# O/P 
# (array([ 4,  6,  8, 10]),)


# indexes where the values are even
import numpy as np
a = np.array([2,1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(a%2 == 0)
print(x)
# O/P:(array([0, 2, 4, 6, 8]),)



#  indexes where the values are odd
import numpy as np
a= np.array([2,1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(a%2 != 0)
print(x)
# O/P:(array([1, 3, 5, 7]),)


