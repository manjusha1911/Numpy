'''
Slicing arrays
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1

'''


import numpy as np    #positive index
a=np.array([1,2,3,4,5,6,7])
print(a[1:5])
print(a[4:])
print(a[:4])
print(a[-3:-1])   #negative index

print(a[1:5:2])   #step
print(a[::2])

#Slicing 2-D Arrays 
import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[1,:4])


print(a[0:,0])   #at a time specific index values from  2d array
print(a[0:,3])

#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

print(a[: ,0:3])
print(a[:, 2:])