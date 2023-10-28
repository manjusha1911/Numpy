import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in a:
    print(i)

# o/p
'''
[[1 2 3]
 [4 5 6]]
[[ 7  8  9]
 [10 11 12]]
'''

b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in b:
    for y in x:
        for z in y:
            print(z)
# b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# for i in np.nditer(b):
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
11
12
'''