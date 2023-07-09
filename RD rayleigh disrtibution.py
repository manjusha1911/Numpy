from numpy import random
# print(random.rayleigh(scale=2,size=(2,3)))


# Visualization of Rayleigh Distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(size=1000),hist=False)
plt.show()