from numpy import random
print(random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100)))


print(random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5)))
# Same example as above, but return a 2-D array with 3 rows, each containing 5 values.