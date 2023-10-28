# from numpy import random
# # n=random.normal(size=(2,3))
# n=random.normal(loc=1,scale=2,size=(2,3))
# print(n)

#visualization
import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns
# sns.distplot(random.normal(size=(2,3)))
# sns.distplot(random.normal(size=1000))
sns.distplot(random.normal(size=1000),hist=False)
plt.show()



# will give different histogram
'''
# sns.distplot(random.normal(size=(2,3)))
# sns.distplot(random.normal(size=1000))
'''
