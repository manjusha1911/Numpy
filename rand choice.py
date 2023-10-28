from numpy import random
print(random.choice([3,5,7,9]))

print(random.choice([3,5,7,9],size=(3,5)))
#o/p random values(o/p will be changed every time)
'''
[[9 5 5 9 3]
 [7 5 5 7 9]
 [7 5 5 9 3]]
'''