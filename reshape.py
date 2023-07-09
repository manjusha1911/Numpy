# NumPy Array Reshaping
'''
Reshaping arrays
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.

'''


# Reshape From 1-D to 2-D.................................
import numpy as np    
# a=np.array([1,2,3,4,30,40,50,78,90,10,11,13])
# # b=a.reshape(4,3)
# # print(b)
# print(a.reshape(4,3))
# #P/O
# # [[ 1  2  3]
# #  [ 4 30 40]
# #  [50 78 90]
# #  [10 11 13]]


# '''Reshape From 1-D to 3-D...........................'''
# # The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
# import numpy as np

# a= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# print(a.reshape(2,3,2))






x=np.array([1,2,3,4])
# print(x.reshape(2,2))

y=np.linspace(10,100,9,endpoint="")
print(y)