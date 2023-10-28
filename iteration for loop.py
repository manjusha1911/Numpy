import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
for i in a:
    print(i)
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

b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in b:
    print(i)

#o/p
'''
[1 2 3 4 5]
[ 6  7  8  9 10]
'''

b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in b:
    for x in i:
        print(x)
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