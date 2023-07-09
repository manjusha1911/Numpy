from numpy import random
# print(random.uniform(size=(2,3)))

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=1000),hist=False,label='uniform')
plt.show()