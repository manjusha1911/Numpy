import numpy as np
a=np.array([41,42,43,44])
l=[]
for element in a:
    if element>42:
        l.append(True)
    else:
        l.append(False)
print(l)
print(a[l])
