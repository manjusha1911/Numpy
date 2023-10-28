import numpy as np
b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in b:
    print(i)

    #o/p
    '''
    [1 2 3 4 5]
    [ 6  7  8  9 10]
    '''
c=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in c:
    for y in x:
        print(y)
# for i in np.nditer(c):
#     print(i)

#o/p
'''
1
2
3
4
5
6
7
8
9
10
'''