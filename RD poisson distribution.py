from numpy import random
# print(random.poisson(lam=4,size=10))

# Visualization of Poisson Distribution

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.poisson(lam=2,size=1000),kde=False)
# plt.show() 


# Normal and Poisson Distribution

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.normal(loc=50,scale=7,size=1000),hist=False,label='normal')
# sns.distplot(random.poisson(lam=50,size=1000),hist=False,label='poisson')
# plt.show()


# Binomial and Poisson Distribution

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=1000,p=0.01,size=1000),hist=False,label='binomial')
sns.distplot(random.poisson(lam=10,size=1000),hist=False,label='poisson')
plt.show()