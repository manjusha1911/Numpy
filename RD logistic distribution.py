# Visualization of Logistic Distribution


from numpy import random
# print(random.logistic(loc=1,scale=2,size=(2,3)))
import matplotlib.pyplot as plt
import seaborn as sns
# sns.distplot(random.logistic(size=1000),hist=False)
# plt.show()


sns.distplot(random.normal(scale=2,size=1000),hist=False,label='normal')
sns.distplot(random.logistic(size=1000),hist=False,label='logestic')
plt.show()